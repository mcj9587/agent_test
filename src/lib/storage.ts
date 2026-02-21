import { ConversationState, CompanionProfile, Message } from "@/types";

const STORAGE_KEY = "amoura_state";

export function loadState(): ConversationState | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    return JSON.parse(raw) as ConversationState;
  } catch {
    return null;
  }
}

export function saveState(state: ConversationState): void {
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch {
    // Storage full or unavailable
  }
}

export function clearState(): void {
  if (typeof window === "undefined") return;
  localStorage.removeItem(STORAGE_KEY);
}

export function getRelationshipStage(
  messageCount: number,
  daysMet: number
): ConversationState["relationshipStage"] {
  if (messageCount < 10) return "new";
  if (messageCount < 30 || daysMet < 2) return "getting_to_know";
  if (messageCount < 80 || daysMet < 5) return "comfortable";
  if (messageCount < 200 || daysMet < 14) return "close";
  return "deep_connection";
}

export function generateId(): string {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
}
