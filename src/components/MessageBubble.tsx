"use client";

import { Message, CompanionProfile, PhotoContent } from "@/types";
import PhotoMessage from "./PhotoMessage";

interface MessageBubbleProps {
  message: Message;
  companion: CompanionProfile;
  showAvatar: boolean;
}

// Parse [PHOTO: desc | mood | action] tags from message content
function parseMessageContent(content: string): Array<
  | { type: "text"; text: string }
  | { type: "photo"; photo: PhotoContent }
> {
  const parts: Array<
    { type: "text"; text: string } | { type: "photo"; photo: PhotoContent }
  > = [];
  const photoRegex = /\[PHOTO:\s*([^|\]]+?)(?:\s*\|\s*([^|\]]+?))?(?:\s*\|\s*([^|\]]+?))?\s*\]/g;

  let lastIndex = 0;
  let match;

  while ((match = photoRegex.exec(content)) !== null) {
    // Add text before the photo
    const textBefore = content.slice(lastIndex, match.index).trim();
    if (textBefore) {
      parts.push({ type: "text", text: textBefore });
    }

    parts.push({
      type: "photo",
      photo: {
        description: match[1]?.trim() || "",
        mood: match[2]?.trim() || "warm soft light",
        scene: match[3]?.trim() || match[1]?.trim() || "",
      },
    });

    lastIndex = match.index + match[0].length;
  }

  // Add remaining text
  const remaining = content.slice(lastIndex).trim();
  if (remaining) {
    parts.push({ type: "text", text: remaining });
  }

  // If nothing was parsed, return original content as text
  if (parts.length === 0 && content.trim()) {
    parts.push({ type: "text", text: content.trim() });
  }

  return parts;
}

function formatTime(timestamp: number): string {
  return new Date(timestamp).toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function MessageBubble({
  message,
  companion,
  showAvatar,
}: MessageBubbleProps) {
  const isUser = message.role === "user";
  const parts = parseMessageContent(message.content);

  return (
    <div
      className={`flex items-end gap-2 animate-slide-up ${
        isUser ? "flex-row-reverse" : "flex-row"
      }`}
    >
      {/* Avatar (companion only) */}
      {!isUser && (
        <div className="flex-shrink-0 w-7">
          {showAvatar ? (
            <div
              className="w-7 h-7 rounded-full flex items-center justify-center text-[10px] text-white font-medium"
              style={{
                background: `linear-gradient(135deg, ${companion.gradientFrom}, ${companion.gradientTo})`,
              }}
            >
              {companion.name[0]}
            </div>
          ) : (
            <div className="w-7" />
          )}
        </div>
      )}

      {/* Message content */}
      <div
        className={`flex flex-col gap-1.5 max-w-[75%] ${
          isUser ? "items-end" : "items-start"
        }`}
      >
        {parts.map((part, i) => {
          if (part.type === "photo") {
            return (
              <PhotoMessage
                key={i}
                photo={part.photo}
                companion={companion}
              />
            );
          }

          return (
            <div
              key={i}
              className={`px-4 py-2.5 text-[15px] leading-relaxed whitespace-pre-wrap break-words ${
                isUser
                  ? "bg-primary-600 text-white rounded-2xl rounded-br-sm"
                  : "bg-surface-800 text-surface-100 rounded-2xl rounded-bl-sm"
              }`}
            >
              {part.text}
            </div>
          );
        })}

        {/* Timestamp & status */}
        <div
          className={`flex items-center gap-1 text-[10px] text-surface-500 px-1 ${
            isUser ? "flex-row-reverse" : ""
          }`}
        >
          <span>{formatTime(message.timestamp)}</span>
          {isUser && message.status && (
            <span>
              {message.status === "sending"
                ? "\u23f3"
                : message.status === "read"
                  ? "\u2713\u2713"
                  : "\u2713"}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}
