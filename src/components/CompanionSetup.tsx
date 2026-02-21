"use client";

import { useState } from "react";
import { CompanionProfile } from "@/types";
import {
  PERSONALITY_PRESETS,
  DEFAULT_APPEARANCES,
  getCompanionGradient,
} from "@/lib/companion";

interface CompanionSetupProps {
  onComplete: (companion: CompanionProfile) => void;
}

export default function CompanionSetup({ onComplete }: CompanionSetupProps) {
  const [step, setStep] = useState(0);
  const [name, setName] = useState("");
  const [gender, setGender] = useState<CompanionProfile["gender"]>("female");
  const [style, setStyle] =
    useState<CompanionProfile["style"]>("warm");
  const [appearance, setAppearance] = useState("");
  const [interests, setInterests] = useState<string[]>([]);
  const [customInterest, setCustomInterest] = useState("");
  const [age, setAge] = useState("25");

  const allInterests = [
    "Music",
    "Art",
    "Cooking",
    "Travel",
    "Reading",
    "Fitness",
    "Movies",
    "Photography",
    "Nature",
    "Gaming",
    "Fashion",
    "Science",
    "Philosophy",
    "Dancing",
    "Writing",
    "Yoga",
  ];

  const handleComplete = () => {
    const gradient = getCompanionGradient(style);
    const emojiMap = {
      warm: "\u2764\ufe0f",
      playful: "\u2728",
      intellectual: "\ud83d\udcda",
      adventurous: "\u26a1",
    };
    const companion: CompanionProfile = {
      name: name || "Alex",
      personality: PERSONALITY_PRESETS[style].personality,
      interests: interests.length > 0 ? interests : ["Music", "Travel", "Art"],
      appearance:
        appearance || DEFAULT_APPEARANCES[gender][0],
      age: age || "25",
      style,
      gender,
      gradientFrom: gradient.from,
      gradientTo: gradient.to,
      emoji: emojiMap[style],
    };
    onComplete(companion);
  };

  const toggleInterest = (interest: string) => {
    setInterests((prev) =>
      prev.includes(interest)
        ? prev.filter((i) => i !== interest)
        : [...prev, interest]
    );
  };

  const addCustomInterest = () => {
    if (customInterest.trim() && !interests.includes(customInterest.trim())) {
      setInterests((prev) => [...prev, customInterest.trim()]);
      setCustomInterest("");
    }
  };

  return (
    <div className="min-h-screen bg-surface-950 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Progress bar */}
        <div className="flex gap-2 mb-8">
          {[0, 1, 2, 3, 4].map((i) => (
            <div
              key={i}
              className={`h-1 flex-1 rounded-full transition-all duration-500 ${
                i <= step
                  ? "bg-gradient-to-r from-primary-400 to-primary-600"
                  : "bg-surface-800"
              }`}
            />
          ))}
        </div>

        {/* Step 0: Welcome */}
        {step === 0 && (
          <div className="animate-fade-in text-center">
            <div className="text-6xl mb-6">{"\ud83d\udc8c"}</div>
            <h1 className="text-3xl font-light text-white mb-3 tracking-wide">
              Amoura
            </h1>
            <p className="text-surface-300 mb-2 text-lg">
              Your AI companion awaits
            </p>
            <p className="text-surface-500 mb-10 text-sm leading-relaxed max-w-xs mx-auto">
              Create someone special to share your thoughts, your day, and your
              world with. A genuine connection, just for you.
            </p>
            <button
              onClick={() => setStep(1)}
              className="w-full py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl font-medium hover:from-primary-600 hover:to-primary-700 transition-all duration-300 shadow-lg shadow-primary-500/20"
            >
              Begin
            </button>
            <p className="text-surface-600 text-xs mt-4">
              For adults 19+. Focused on genuine connection.
            </p>
          </div>
        )}

        {/* Step 1: Name & Gender */}
        {step === 1 && (
          <div className="animate-fade-in">
            <h2 className="text-xl font-light text-white mb-1">
              Who would you like to meet?
            </h2>
            <p className="text-surface-400 text-sm mb-8">
              Give them a name and identity
            </p>

            <label className="block text-surface-300 text-sm mb-2">
              Their name
            </label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g. Sam, Luna, River..."
              className="w-full bg-surface-900 border border-surface-700 rounded-xl px-4 py-3 text-white placeholder-surface-500 focus:outline-none focus:border-primary-500 transition-colors mb-6"
              maxLength={20}
            />

            <label className="block text-surface-300 text-sm mb-3">
              Gender
            </label>
            <div className="grid grid-cols-3 gap-3 mb-6">
              {(["female", "male", "nonbinary"] as const).map((g) => (
                <button
                  key={g}
                  onClick={() => setGender(g)}
                  className={`py-3 rounded-xl border text-sm font-medium transition-all duration-200 ${
                    gender === g
                      ? "border-primary-500 bg-primary-500/10 text-primary-400"
                      : "border-surface-700 bg-surface-900 text-surface-300 hover:border-surface-600"
                  }`}
                >
                  {g === "female"
                    ? "Woman"
                    : g === "male"
                      ? "Man"
                      : "Non-binary"}
                </button>
              ))}
            </div>

            <label className="block text-surface-300 text-sm mb-2">
              Age
            </label>
            <input
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              min="19"
              max="60"
              className="w-full bg-surface-900 border border-surface-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary-500 transition-colors mb-8"
            />

            <button
              onClick={() => setStep(2)}
              className="w-full py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl font-medium hover:from-primary-600 hover:to-primary-700 transition-all"
            >
              Next
            </button>
          </div>
        )}

        {/* Step 2: Personality */}
        {step === 2 && (
          <div className="animate-fade-in">
            <h2 className="text-xl font-light text-white mb-1">
              What&apos;s {name || "their"} personality like?
            </h2>
            <p className="text-surface-400 text-sm mb-8">
              Choose what resonates with you
            </p>

            <div className="space-y-3">
              {(
                Object.entries(PERSONALITY_PRESETS) as [
                  CompanionProfile["style"],
                  (typeof PERSONALITY_PRESETS)[CompanionProfile["style"]],
                ][]
              ).map(([key, preset]) => (
                <button
                  key={key}
                  onClick={() => setStyle(key)}
                  className={`w-full text-left p-4 rounded-xl border transition-all duration-200 ${
                    style === key
                      ? "border-primary-500 bg-primary-500/10"
                      : "border-surface-700 bg-surface-900 hover:border-surface-600"
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <span className="text-xl">
                      {key === "warm"
                        ? "\u2764\ufe0f"
                        : key === "playful"
                          ? "\u2728"
                          : key === "intellectual"
                            ? "\ud83d\udcda"
                            : "\u26a1"}
                    </span>
                    <div>
                      <div
                        className={`font-medium text-sm ${style === key ? "text-primary-400" : "text-white"}`}
                      >
                        {preset.label}
                      </div>
                      <div className="text-surface-400 text-xs mt-0.5">
                        {preset.description}
                      </div>
                    </div>
                  </div>
                </button>
              ))}
            </div>

            <div className="flex gap-3 mt-8">
              <button
                onClick={() => setStep(1)}
                className="px-6 py-4 border border-surface-700 text-surface-300 rounded-2xl hover:bg-surface-800 transition-all"
              >
                Back
              </button>
              <button
                onClick={() => setStep(3)}
                className="flex-1 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl font-medium hover:from-primary-600 hover:to-primary-700 transition-all"
              >
                Next
              </button>
            </div>
          </div>
        )}

        {/* Step 3: Appearance */}
        {step === 3 && (
          <div className="animate-fade-in">
            <h2 className="text-xl font-light text-white mb-1">
              What does {name || "they"} look like?
            </h2>
            <p className="text-surface-400 text-sm mb-6">
              Choose a preset or write your own
            </p>

            <div className="space-y-3 mb-6 max-h-60 overflow-y-auto pr-1">
              {DEFAULT_APPEARANCES[gender].map((desc, i) => (
                <button
                  key={i}
                  onClick={() => setAppearance(desc)}
                  className={`w-full text-left p-4 rounded-xl border text-sm transition-all duration-200 ${
                    appearance === desc
                      ? "border-primary-500 bg-primary-500/10 text-primary-300"
                      : "border-surface-700 bg-surface-900 text-surface-300 hover:border-surface-600"
                  }`}
                >
                  {desc}
                </button>
              ))}
            </div>

            <label className="block text-surface-400 text-xs mb-2">
              Or describe them yourself
            </label>
            <textarea
              value={
                DEFAULT_APPEARANCES[gender].includes(appearance)
                  ? ""
                  : appearance
              }
              onChange={(e) => setAppearance(e.target.value)}
              placeholder="Describe their appearance, style, vibe..."
              className="w-full bg-surface-900 border border-surface-700 rounded-xl px-4 py-3 text-white placeholder-surface-500 focus:outline-none focus:border-primary-500 transition-colors resize-none h-20 text-sm"
              maxLength={300}
            />

            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setStep(2)}
                className="px-6 py-4 border border-surface-700 text-surface-300 rounded-2xl hover:bg-surface-800 transition-all"
              >
                Back
              </button>
              <button
                onClick={() => setStep(4)}
                className="flex-1 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl font-medium hover:from-primary-600 hover:to-primary-700 transition-all"
              >
                Next
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Interests */}
        {step === 4 && (
          <div className="animate-fade-in">
            <h2 className="text-xl font-light text-white mb-1">
              What is {name || "they"} into?
            </h2>
            <p className="text-surface-400 text-sm mb-6">
              Pick a few interests (or add your own)
            </p>

            <div className="flex flex-wrap gap-2 mb-4">
              {allInterests.map((interest) => (
                <button
                  key={interest}
                  onClick={() => toggleInterest(interest)}
                  className={`px-4 py-2 rounded-full text-sm transition-all duration-200 ${
                    interests.includes(interest)
                      ? "bg-primary-500/20 text-primary-400 border border-primary-500/50"
                      : "bg-surface-800 text-surface-300 border border-surface-700 hover:border-surface-600"
                  }`}
                >
                  {interest}
                </button>
              ))}
              {interests
                .filter((i) => !allInterests.includes(i))
                .map((interest) => (
                  <button
                    key={interest}
                    onClick={() => toggleInterest(interest)}
                    className="px-4 py-2 rounded-full text-sm bg-primary-500/20 text-primary-400 border border-primary-500/50"
                  >
                    {interest}
                  </button>
                ))}
            </div>

            <div className="flex gap-2 mb-8">
              <input
                value={customInterest}
                onChange={(e) => setCustomInterest(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && addCustomInterest()}
                placeholder="Add custom interest..."
                className="flex-1 bg-surface-900 border border-surface-700 rounded-xl px-4 py-2.5 text-white placeholder-surface-500 focus:outline-none focus:border-primary-500 transition-colors text-sm"
              />
              <button
                onClick={addCustomInterest}
                className="px-4 py-2.5 bg-surface-800 border border-surface-700 text-surface-300 rounded-xl hover:bg-surface-700 transition-colors text-sm"
              >
                Add
              </button>
            </div>

            <div className="flex gap-3">
              <button
                onClick={() => setStep(3)}
                className="px-6 py-4 border border-surface-700 text-surface-300 rounded-2xl hover:bg-surface-800 transition-all"
              >
                Back
              </button>
              <button
                onClick={handleComplete}
                className="flex-1 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl font-medium hover:from-primary-600 hover:to-primary-700 transition-all shadow-lg shadow-primary-500/20"
              >
                Meet {name || "Them"} {"\u2192"}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
