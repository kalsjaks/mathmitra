import React from 'react';

export default function MascotLogo({ className = "w-14 h-14" }) {
  return (
    <div className={`relative flex items-center justify-center ${className}`}>
      <svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full drop-shadow-md">
        {/* Colorful Open Book */}
        {/* Left Book Page (Warm Gold / Orange) */}
        <path
          d="M 50 68 C 38 60, 20 60, 10 65 L 10 82 C 22 77, 38 77, 50 85 Z"
          fill="#F59E0B"
        />
        {/* Right Book Page (Vibrant Sky Blue / Cyan) */}
        <path
          d="M 50 68 C 62 60, 80 60, 90 65 L 90 82 C 78 77, 62 77, 50 85 Z"
          fill="#0EA5E9"
        />
        {/* Book Spine / Cover Base (Fresh Green & Emerald) */}
        <path
          d="M 10 82 C 22 77, 38 77, 50 85 C 62 77, 78 77, 90 82 L 88 88 C 76 83, 62 83, 50 90 C 38 83, 24 83, 12 88 Z"
          fill="#10B981"
        />
        {/* Center Page Divider */}
        <path d="M 50 68 L 50 86" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" opacity="0.6" />

        {/* Cute AI Math Robot Sitting On The Book */}
        {/* Robot Head Outer */}
        <rect x="28" y="24" width="44" height="38" rx="14" fill="#3B82F6" />
        <rect x="30" y="26" width="40" height="34" rx="12" fill="#2563EB" />

        {/* Robot Screen Face */}
        <rect x="34" y="31" width="32" height="24" rx="8" fill="#1E293B" />

        {/* Friendly Glowing Blue Eyes */}
        <circle cx="43" cy="42" r="3.5" fill="#38BDF8" />
        <circle cx="57" cy="42" r="3.5" fill="#38BDF8" />
        {/* Little eye sparkles */}
        <circle cx="44.5" cy="40.5" r="1.2" fill="#FFFFFF" />
        <circle cx="58.5" cy="40.5" r="1.2" fill="#FFFFFF" />

        {/* Happy smile line */}
        <path d="M 47 48 Q 50 51 53 48" stroke="#38BDF8" strokeWidth="1.8" strokeLinecap="round" />

        {/* Cute Head Antenna / Pencil tip */}
        <path d="M 50 14 L 50 24" stroke="#F59E0B" strokeWidth="3.5" strokeLinecap="round" />
        <circle cx="50" cy="13" r="4.5" fill="#F59E0B" />
        <circle cx="50" cy="13" r="2" fill="#FEF08A" />

        {/* Side Earphone Details */}
        <rect x="25" y="34" width="4" height="12" rx="2" fill="#F59E0B" />
        <rect x="71" y="34" width="4" height="12" rx="2" fill="#F59E0B" />
      </svg>
    </div>
  );
}
