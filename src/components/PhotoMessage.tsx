"use client";

import { PhotoContent, CompanionProfile } from "@/types";

interface PhotoMessageProps {
  photo: PhotoContent;
  companion: CompanionProfile;
}

export default function PhotoMessage({ photo, companion }: PhotoMessageProps) {
  // Generate a deterministic gradient based on the scene description
  const hash = photo.scene
    .split("")
    .reduce((acc, char) => acc + char.charCodeAt(0), 0);
  const hueShift = hash % 60;

  // Mood-based color adjustments
  const moodColors: Record<string, { overlay: string; accent: string }> = {
    warm: { overlay: "from-amber-900/60 to-orange-900/40", accent: "amber" },
    golden: { overlay: "from-yellow-900/60 to-amber-900/40", accent: "yellow" },
    cozy: { overlay: "from-orange-900/60 to-red-900/40", accent: "orange" },
    romantic: { overlay: "from-rose-900/60 to-pink-900/40", accent: "rose" },
    dreamy: { overlay: "from-purple-900/60 to-indigo-900/40", accent: "purple" },
    peaceful: { overlay: "from-teal-900/60 to-cyan-900/40", accent: "teal" },
    energetic: { overlay: "from-red-900/60 to-orange-900/40", accent: "red" },
    night: { overlay: "from-indigo-900/70 to-slate-900/50", accent: "indigo" },
    morning: { overlay: "from-sky-900/50 to-amber-900/40", accent: "sky" },
    default: { overlay: "from-slate-900/60 to-gray-900/40", accent: "slate" },
  };

  const moodKey =
    Object.keys(moodColors).find((key) =>
      photo.mood.toLowerCase().includes(key)
    ) || "default";
  const colors = moodColors[moodKey];

  // Scene-based decorative elements
  const sceneIcons: Record<string, string> = {
    cafe: "\u2615",
    coffee: "\u2615",
    sunset: "\ud83c\udf05",
    beach: "\ud83c\udfd6\ufe0f",
    bed: "\ud83d\ude34",
    kitchen: "\ud83c\udf73",
    rain: "\ud83c\udf27\ufe0f",
    night: "\ud83c\udf19",
    garden: "\ud83c\udf3a",
    book: "\ud83d\udcda",
    music: "\ud83c\udfb6",
    mirror: "\ud83e\ude9e",
    window: "\ud83c\udf04",
    walk: "\ud83d\udeb6",
    park: "\ud83c\udf33",
    city: "\ud83c\udfd9\ufe0f",
    food: "\ud83c\udf74",
    wine: "\ud83c\udf77",
    candle: "\ud83d\udd6f\ufe0f",
    flower: "\ud83c\udf38",
    car: "\ud83d\ude97",
    bath: "\ud83d\udec1",
    snow: "\u2744\ufe0f",
    sun: "\u2600\ufe0f",
    star: "\u2b50",
    cat: "\ud83d\udc31",
    dog: "\ud83d\udc36",
  };

  const sceneIcon =
    Object.entries(sceneIcons).find(([key]) =>
      photo.scene.toLowerCase().includes(key)
    )?.[1] || "\ud83d\udcf7";

  return (
    <div className="relative overflow-hidden rounded-2xl w-72 aspect-[3/4] group cursor-pointer">
      {/* Base gradient — shifts based on content */}
      <div
        className="absolute inset-0"
        style={{
          background: `linear-gradient(135deg,
            hsl(${(340 + hueShift) % 360}, 40%, 20%) 0%,
            hsl(${(280 + hueShift) % 360}, 35%, 15%) 50%,
            hsl(${(220 + hueShift) % 360}, 30%, 12%) 100%)`,
        }}
      />

      {/* Atmospheric overlay */}
      <div
        className={`absolute inset-0 bg-gradient-to-b ${colors.overlay}`}
      />

      {/* Decorative circles (bokeh-like) */}
      <div className="absolute inset-0 overflow-hidden">
        <div
          className="absolute w-32 h-32 rounded-full opacity-10"
          style={{
            background: `radial-gradient(circle, ${companion.gradientFrom}40, transparent)`,
            top: "10%",
            right: "-10%",
          }}
        />
        <div
          className="absolute w-24 h-24 rounded-full opacity-10"
          style={{
            background: `radial-gradient(circle, ${companion.gradientTo}40, transparent)`,
            bottom: "20%",
            left: "-5%",
          }}
        />
        <div
          className="absolute w-16 h-16 rounded-full opacity-5"
          style={{
            background: `radial-gradient(circle, white, transparent)`,
            top: "40%",
            right: "20%",
          }}
        />
      </div>

      {/* Grain texture */}
      <div className="absolute inset-0 opacity-[0.03] mix-blend-overlay bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIj48ZmlsdGVyIGlkPSJhIj48ZmVUdXJidWxlbmNlIHR5cGU9ImZyYWN0YWxOb2lzZSIgYmFzZUZyZXF1ZW5jeT0iLjc1IiBzdGl0Y2hUaWxlcz0ic3RpdGNoIi8+PC9maWx0ZXI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsdGVyPSJ1cmwoI2EpIi8+PC9zdmc+')]" />

      {/* Content */}
      <div className="absolute inset-0 flex flex-col justify-between p-5">
        {/* Top: camera indicator */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-white/50 text-xs">
            <svg
              className="w-3.5 h-3.5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M6.827 6.175A2.31 2.31 0 015.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 00-1.134-.175 2.31 2.31 0 01-1.64-1.055l-.822-1.316a2.192 2.192 0 00-1.736-1.039 48.774 48.774 0 00-5.232 0 2.192 2.192 0 00-1.736 1.039l-.821 1.316z"
              />
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M16.5 12.75a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0z"
              />
            </svg>
            <span>Photo from {companion.name}</span>
          </div>
          <span className="text-2xl">{sceneIcon}</span>
        </div>

        {/* Center: large scene icon */}
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <div
              className="w-20 h-20 rounded-full mx-auto mb-4 flex items-center justify-center"
              style={{
                background: `linear-gradient(135deg, ${companion.gradientFrom}30, ${companion.gradientTo}30)`,
                border: `1px solid ${companion.gradientFrom}20`,
              }}
            >
              <span className="text-4xl opacity-80">{sceneIcon}</span>
            </div>
          </div>
        </div>

        {/* Bottom: description */}
        <div className="space-y-2">
          <p className="text-white/90 text-sm leading-relaxed font-light">
            {photo.description}
          </p>
          <p className="text-white/40 text-xs italic">{photo.mood}</p>
        </div>
      </div>

      {/* Edge vignette */}
      <div className="absolute inset-0 rounded-2xl shadow-[inset_0_0_40px_rgba(0,0,0,0.3)] pointer-events-none" />
    </div>
  );
}
