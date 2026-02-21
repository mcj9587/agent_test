"use client";

import { useState, useRef, useEffect, useCallback } from "react";
import {
  Message,
  CompanionProfile,
  ConversationState,
  ChatRequest,
} from "@/types";
import {
  saveState,
  generateId,
  getRelationshipStage,
} from "@/lib/storage";
import MessageBubble from "./MessageBubble";
import ProfileHeader from "./ProfileHeader";
import TypingIndicator from "./TypingIndicator";

interface ChatWindowProps {
  state: ConversationState;
  onStateChange: (state: ConversationState) => void;
  onReset: () => void;
}

export default function ChatWindow({
  state,
  onStateChange,
  onReset,
}: ChatWindowProps) {
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [showProfile, setShowProfile] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  const companion = state.companion!;
  const messages = state.messages;

  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping, scrollToBottom]);

  // Auto-resize textarea
  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.style.height = "auto";
      inputRef.current.style.height = `${Math.min(inputRef.current.scrollHeight, 120)}px`;
    }
  }, [input]);

  // Send initial greeting when conversation starts
  useEffect(() => {
    if (messages.length === 0 && companion) {
      sendGreeting();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function sendGreeting() {
    setIsTyping(true);

    try {
      const greetingRequest: ChatRequest = {
        message: `[System: This is the very first message. ${companion.name} is reaching out for the first time. Send a natural, warm opening message — like a first text to someone you've just started talking to. Be yourself. Keep it casual and intriguing.]`,
        companion,
        history: [],
        relationshipStage: "new",
      };

      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(greetingRequest),
      });

      if (!response.ok) throw new Error("Failed to get greeting");

      const reader = response.body?.getReader();
      if (!reader) throw new Error("No reader");

      let fullText = "";
      const decoder = new TextDecoder();

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split("\n");

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            try {
              const data = JSON.parse(line.slice(6));
              if (data.text) fullText += data.text;
              if (data.done) break;
            } catch {
              // Skip malformed lines
            }
          }
        }
      }

      if (fullText.trim()) {
        const greetingMessage: Message = {
          id: generateId(),
          role: "assistant",
          content: fullText.trim(),
          timestamp: Date.now(),
        };

        const newState: ConversationState = {
          ...state,
          messages: [greetingMessage],
        };
        onStateChange(newState);
        saveState(newState);
      }
    } catch (error) {
      console.error("Greeting error:", error);
    } finally {
      setIsTyping(false);
    }
  }

  async function sendMessage() {
    const text = input.trim();
    if (!text || isTyping) return;

    setInput("");
    if (inputRef.current) {
      inputRef.current.style.height = "auto";
    }

    // Add user message
    const userMessage: Message = {
      id: generateId(),
      role: "user",
      content: text,
      timestamp: Date.now(),
      status: "sent",
    };

    const updatedMessages = [...messages, userMessage];
    const daysMet = Math.floor(
      (Date.now() - state.createdAt) / (1000 * 60 * 60 * 24)
    );
    const newRelationshipStage = getRelationshipStage(
      updatedMessages.length,
      daysMet
    );

    let updatedState: ConversationState = {
      ...state,
      messages: updatedMessages,
      relationshipStage: newRelationshipStage,
      daysMet,
    };
    onStateChange(updatedState);
    saveState(updatedState);

    // Get AI response
    setIsTyping(true);

    try {
      const chatRequest: ChatRequest = {
        message: text,
        companion,
        history: updatedMessages,
        relationshipStage: newRelationshipStage,
      };

      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(chatRequest),
      });

      if (!response.ok) throw new Error("Failed to send message");

      const reader = response.body?.getReader();
      if (!reader) throw new Error("No reader");

      let fullText = "";
      const decoder = new TextDecoder();

      // Stream the response
      const assistantMessage: Message = {
        id: generateId(),
        role: "assistant",
        content: "",
        timestamp: Date.now(),
      };

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split("\n");

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            try {
              const data = JSON.parse(line.slice(6));
              if (data.text) {
                fullText += data.text;
                assistantMessage.content = fullText;

                // Update state with streaming content
                const streamState: ConversationState = {
                  ...updatedState,
                  messages: [...updatedMessages, { ...assistantMessage }],
                };
                onStateChange(streamState);
              }
              if (data.done) break;
              if (data.error) {
                console.error("Stream error:", data.error);
                break;
              }
            } catch {
              // Skip malformed lines
            }
          }
        }
      }

      // Mark user message as read
      userMessage.status = "read";

      // Final state update
      if (fullText.trim()) {
        assistantMessage.content = fullText.trim();
        const finalState: ConversationState = {
          ...updatedState,
          messages: [...updatedMessages, assistantMessage],
        };
        onStateChange(finalState);
        saveState(finalState);
      }
    } catch (error) {
      console.error("Send error:", error);
      // Add error message
      const errorMessage: Message = {
        id: generateId(),
        role: "assistant",
        content:
          "sorry, something went wrong on my end. can you try again? \u{1F615}",
        timestamp: Date.now(),
      };
      const errorState: ConversationState = {
        ...updatedState,
        messages: [...updatedMessages, errorMessage],
      };
      onStateChange(errorState);
      saveState(errorState);
    } finally {
      setIsTyping(false);
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  // Group consecutive messages from the same sender
  function shouldShowAvatar(index: number): boolean {
    if (messages[index].role === "user") return false;
    if (index === 0) return true;
    return messages[index - 1].role !== messages[index].role;
  }

  return (
    <div className="h-screen flex flex-col bg-surface-950">
      {/* Header */}
      <ProfileHeader
        companion={companion}
        isTyping={isTyping}
        onProfileClick={() => setShowProfile(!showProfile)}
        onReset={onReset}
      />

      {/* Profile panel */}
      {showProfile && (
        <div className="bg-surface-900 border-b border-surface-800 p-6 animate-fade-in">
          <div className="max-w-lg mx-auto">
            <div className="flex items-center gap-4 mb-4">
              <div
                className="w-16 h-16 rounded-full flex items-center justify-center text-2xl text-white font-medium"
                style={{
                  background: `linear-gradient(135deg, ${companion.gradientFrom}, ${companion.gradientTo})`,
                }}
              >
                {companion.name[0]}
              </div>
              <div>
                <h3 className="text-white font-medium text-lg">
                  {companion.name}
                </h3>
                <p className="text-surface-400 text-sm">
                  {companion.age} years old
                </p>
                <p className="text-surface-500 text-xs mt-1 capitalize">
                  {state.relationshipStage.replace(/_/g, " ")} &middot;{" "}
                  {messages.length} messages
                </p>
              </div>
            </div>
            <p className="text-surface-300 text-sm leading-relaxed mb-3">
              {companion.appearance}
            </p>
            <div className="flex flex-wrap gap-1.5">
              {companion.interests.map((interest) => (
                <span
                  key={interest}
                  className="px-3 py-1 rounded-full text-xs bg-surface-800 text-surface-300 border border-surface-700"
                >
                  {interest}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Messages */}
      <div
        ref={chatContainerRef}
        className="flex-1 overflow-y-auto px-4 py-4 space-y-2"
      >
        {/* Date header */}
        {messages.length > 0 && (
          <div className="text-center py-2">
            <span className="text-surface-500 text-xs bg-surface-900/50 px-3 py-1 rounded-full">
              {new Date(messages[0].timestamp).toLocaleDateString([], {
                weekday: "long",
                month: "long",
                day: "numeric",
              })}
            </span>
          </div>
        )}

        {messages.map((msg, index) => (
          <MessageBubble
            key={msg.id}
            message={msg}
            companion={companion}
            showAvatar={shouldShowAvatar(index)}
          />
        ))}

        {isTyping && messages.length > 0 && (
          <TypingIndicator companion={companion} />
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input area */}
      <div className="bg-surface-950 border-t border-surface-800/50 px-4 py-3">
        <div className="flex items-end gap-3 max-w-3xl mx-auto">
          {/* Attachment button (decorative) */}
          <button className="text-surface-400 hover:text-surface-300 transition-colors p-2 mb-0.5">
            <svg
              className="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M12 4.5v15m7.5-7.5h-15"
              />
            </svg>
          </button>

          {/* Text input */}
          <div className="flex-1 relative">
            <textarea
              ref={inputRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={`Message ${companion.name}...`}
              className="w-full bg-surface-800 rounded-2xl px-4 py-3 text-white placeholder-surface-500 focus:outline-none focus:ring-1 focus:ring-surface-600 resize-none text-[15px] leading-relaxed max-h-30 overflow-y-auto"
              rows={1}
              disabled={isTyping}
            />
          </div>

          {/* Send button */}
          <button
            onClick={sendMessage}
            disabled={!input.trim() || isTyping}
            className={`p-2.5 rounded-full transition-all duration-200 mb-0.5 ${
              input.trim() && !isTyping
                ? "bg-primary-500 text-white hover:bg-primary-600 shadow-lg shadow-primary-500/20"
                : "bg-surface-800 text-surface-500"
            }`}
          >
            <svg
              className="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
}
