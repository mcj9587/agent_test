"use client";

import { CompanionProfile } from "@/types";

interface TypingIndicatorProps {
  companion: CompanionProfile;
}

export default function TypingIndicator({ companion }: TypingIndicatorProps) {
  return (
    <div className="flex items-end gap-2 animate-fade-in">
      {/* Avatar */}
      <div
        className="w-7 h-7 rounded-full flex items-center justify-center text-xs text-white flex-shrink-0"
        style={{
          background: `linear-gradient(135deg, ${companion.gradientFrom}, ${companion.gradientTo})`,
        }}
      >
        {companion.name[0]}
      </div>

      {/* Typing bubble */}
      <div className="bg-surface-800 rounded-2xl rounded-bl-sm px-5 py-3.5">
        <div className="flex gap-1.5 items-center">
          <div
            className="w-2 h-2 rounded-full bg-surface-400 animate-typing-dot"
            style={{ animationDelay: "0ms" }}
          />
          <div
            className="w-2 h-2 rounded-full bg-surface-400 animate-typing-dot"
            style={{ animationDelay: "200ms" }}
          />
          <div
            className="w-2 h-2 rounded-full bg-surface-400 animate-typing-dot"
            style={{ animationDelay: "400ms" }}
          />
        </div>
      </div>
    </div>
  );
}
