# Amoura - Virtual AI Companion

A virtual AI companion app inspired by the movie "Her". Create a personalized companion and experience genuine, emotionally intelligent conversations through a beautiful messenger interface.

Built with Next.js, TypeScript, Tailwind CSS, and Claude (Anthropic) API.

## Features

- **Companion Creation**: Customize your companion's name, gender, age, personality, appearance, and interests
- **Intelligent Conversations**: Powered by Claude for emotionally rich, contextual dialogue that feels genuine
- **Photo Sharing**: Your companion sends contextual "photos" — beautifully rendered scene cards based on conversation context
- **Relationship Progression**: The relationship evolves through stages (new, getting to know, comfortable, close, deep connection) based on conversation depth
- **Streaming Responses**: Real-time typing with streamed responses for a natural texting feel
- **Conversation Memory**: Messages persist in localStorage across sessions
- **Mobile-First Design**: Responsive messenger UI that works on all devices
- **19+ Mature Content**: Adult themes handled tastefully — genuine emotional connection, not explicit content

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **AI**: Anthropic Claude API (claude-sonnet-4-5)
- **Storage**: localStorage (client-side persistence)

## Getting Started

### Prerequisites

- Node.js 18+
- An Anthropic API key ([get one here](https://console.anthropic.com/))

### Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create a `.env.local` file with your API key:
   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```

3. Start the dev server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000)

## How It Works

1. **Onboarding**: Create your companion by choosing their name, gender, personality type (warm, playful, intellectual, adventurous), appearance, and interests
2. **Chat**: Your companion sends a natural first message, and the conversation begins
3. **Photos**: The companion naturally shares "photos" during conversation — these render as atmospheric scene cards with descriptions and mood lighting
4. **Progression**: As you exchange more messages over time, the relationship stage evolves, changing how your companion interacts with you

## Architecture

```
src/
├── app/
│   ├── api/chat/route.ts    # Streaming chat API endpoint
│   ├── layout.tsx            # Root layout with metadata
│   ├── page.tsx              # Main page (setup vs chat routing)
│   └── globals.css           # Global styles
├── components/
│   ├── ChatWindow.tsx        # Main chat container with streaming
│   ├── CompanionSetup.tsx    # 5-step onboarding wizard
│   ├── MessageBubble.tsx     # Message rendering with photo parsing
│   ├── PhotoMessage.tsx      # Atmospheric photo card component
│   ├── ProfileHeader.tsx     # Chat header with status
│   └── TypingIndicator.tsx   # Animated typing dots
├── lib/
│   ├── companion.ts          # System prompt builder & personality presets
│   └── storage.ts            # localStorage persistence
└── types/
    └── index.ts              # TypeScript interfaces
```
