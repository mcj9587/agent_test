export interface CompanionProfile {
  name: string;
  personality: string;
  interests: string[];
  appearance: string;
  age: string;
  style: "warm" | "playful" | "intellectual" | "adventurous";
  gender: "female" | "male" | "nonbinary";
  gradientFrom: string;
  gradientTo: string;
  emoji: string;
}

export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: number;
  photo?: PhotoContent;
  status?: "sending" | "sent" | "read";
}

export interface PhotoContent {
  description: string;
  scene: string;
  mood: string;
}

export interface ConversationState {
  messages: Message[];
  companion: CompanionProfile | null;
  relationshipStage: RelationshipStage;
  daysMet: number;
  createdAt: number;
}

export type RelationshipStage =
  | "new"
  | "getting_to_know"
  | "comfortable"
  | "close"
  | "deep_connection";

export interface ChatRequest {
  message: string;
  companion: CompanionProfile;
  history: Message[];
  relationshipStage: RelationshipStage;
}
