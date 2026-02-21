import Anthropic from "@anthropic-ai/sdk";
import { buildSystemPrompt } from "@/lib/companion";
import { ChatRequest, Message } from "@/types";

const client = new Anthropic();

export async function POST(request: Request) {
  try {
    const body: ChatRequest = await request.json();
    const { message, companion, history, relationshipStage } = body;

    if (!message || !companion) {
      return Response.json({ error: "Missing required fields" }, { status: 400 });
    }

    const systemPrompt = buildSystemPrompt(
      companion,
      relationshipStage,
      history.length
    );

    // Build message history for Claude (last 50 messages for context window management)
    const recentHistory = history.slice(-50);
    const messages: Array<{ role: "user" | "assistant"; content: string }> =
      recentHistory
        .filter((m: Message) => m.content.trim().length > 0)
        .map((m: Message) => ({
          role: m.role,
          content: m.content,
        }));

    // Add current message
    messages.push({ role: "user", content: message });

    // Ensure messages alternate correctly — merge consecutive same-role messages
    const cleanedMessages: Array<{
      role: "user" | "assistant";
      content: string;
    }> = [];
    for (const msg of messages) {
      if (
        cleanedMessages.length > 0 &&
        cleanedMessages[cleanedMessages.length - 1].role === msg.role
      ) {
        cleanedMessages[cleanedMessages.length - 1].content +=
          "\n" + msg.content;
      } else {
        cleanedMessages.push({ ...msg });
      }
    }

    // Ensure first message is from user
    if (cleanedMessages.length > 0 && cleanedMessages[0].role !== "user") {
      cleanedMessages.shift();
    }

    const stream = client.messages.stream({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      system: systemPrompt,
      messages: cleanedMessages,
    });

    // Create a ReadableStream from the Anthropic stream
    const readableStream = new ReadableStream({
      async start(controller) {
        try {
          for await (const event of stream) {
            if (
              event.type === "content_block_delta" &&
              event.delta.type === "text_delta"
            ) {
              const data = JSON.stringify({ text: event.delta.text });
              controller.enqueue(
                new TextEncoder().encode(`data: ${data}\n\n`)
              );
            }
          }
          controller.enqueue(
            new TextEncoder().encode(`data: ${JSON.stringify({ done: true })}\n\n`)
          );
          controller.close();
        } catch (error) {
          const errorMessage =
            error instanceof Error ? error.message : "Stream error";
          controller.enqueue(
            new TextEncoder().encode(
              `data: ${JSON.stringify({ error: errorMessage })}\n\n`
            )
          );
          controller.close();
        }
      },
    });

    return new Response(readableStream, {
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      },
    });
  } catch (error) {
    const errorMessage =
      error instanceof Error ? error.message : "Internal server error";
    return Response.json({ error: errorMessage }, { status: 500 });
  }
}
