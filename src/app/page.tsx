"use client";

import { useState, useEffect } from "react";
import { CompanionProfile, ConversationState } from "@/types";
import { loadState, saveState, clearState } from "@/lib/storage";
import CompanionSetup from "@/components/CompanionSetup";
import ChatWindow from "@/components/ChatWindow";

export default function Home() {
  const [state, setState] = useState<ConversationState | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Load saved state on mount
  useEffect(() => {
    const saved = loadState();
    if (saved && saved.companion) {
      setState(saved);
    }
    setIsLoading(false);
  }, []);

  function handleCompanionCreated(companion: CompanionProfile) {
    const newState: ConversationState = {
      messages: [],
      companion,
      relationshipStage: "new",
      daysMet: 0,
      createdAt: Date.now(),
    };
    setState(newState);
    saveState(newState);
  }

  function handleStateChange(newState: ConversationState) {
    setState(newState);
  }

  function handleReset() {
    if (
      window.confirm(
        "Start over with a new companion? Your current conversation will be lost."
      )
    ) {
      clearState();
      setState(null);
    }
  }

  // Loading state
  if (isLoading) {
    return (
      <div className="min-h-screen bg-surface-950 flex items-center justify-center">
        <div className="text-center animate-fade-in">
          <div className="text-4xl mb-4">{"\ud83d\udc8c"}</div>
          <div className="text-surface-400 text-sm">Loading...</div>
        </div>
      </div>
    );
  }

  // No companion set up yet — show setup
  if (!state || !state.companion) {
    return <CompanionSetup onComplete={handleCompanionCreated} />;
  }

  // Chat view
  return (
    <ChatWindow
      state={state}
      onStateChange={handleStateChange}
      onReset={handleReset}
    />
  );
}
