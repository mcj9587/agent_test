"use client";

import { CompanionProfile } from "@/types";

interface ProfileHeaderProps {
  companion: CompanionProfile;
  isTyping: boolean;
  onProfileClick: () => void;
  onReset: () => void;
}

export default function ProfileHeader({
  companion,
  isTyping,
  onProfileClick,
  onReset,
}: ProfileHeaderProps) {
  return (
    <div className="bg-surface-950/80 backdrop-blur-xl border-b border-surface-800/50 px-4 py-3 flex items-center gap-3 sticky top-0 z-10">
      {/* Back / Reset */}
      <button
        onClick={onReset}
        className="text-surface-400 hover:text-white transition-colors p-1"
        title="New companion"
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
            d="M15.75 19.5L8.25 12l7.5-7.5"
          />
        </svg>
      </button>

      {/* Avatar */}
      <button
        onClick={onProfileClick}
        className="relative flex-shrink-0"
      >
        <div
          className="w-10 h-10 rounded-full flex items-center justify-center text-white font-medium"
          style={{
            background: `linear-gradient(135deg, ${companion.gradientFrom}, ${companion.gradientTo})`,
          }}
        >
          {companion.name[0].toUpperCase()}
        </div>
        {/* Online indicator */}
        <div className="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 bg-green-500 rounded-full border-2 border-surface-950" />
      </button>

      {/* Name & Status */}
      <button onClick={onProfileClick} className="flex-1 text-left">
        <div className="text-white font-medium text-sm">{companion.name}</div>
        <div className="text-xs">
          {isTyping ? (
            <span className="text-primary-400">typing...</span>
          ) : (
            <span className="text-green-400">online</span>
          )}
        </div>
      </button>

      {/* Call buttons (decorative) */}
      <div className="flex items-center gap-3">
        <button className="text-surface-400 hover:text-white transition-colors p-1">
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
              d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"
            />
          </svg>
        </button>
        <button className="text-surface-400 hover:text-white transition-colors p-1">
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
              d="m15.75 10.5 4.72-4.72a.75.75 0 011.28.53v11.38a.75.75 0 01-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25h-9A2.25 2.25 0 002.25 7.5v9a2.25 2.25 0 002.25 2.25z"
            />
          </svg>
        </button>
      </div>
    </div>
  );
}
