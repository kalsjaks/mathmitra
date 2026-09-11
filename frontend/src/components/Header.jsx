import React from 'react';
import MascotLogo from './MascotLogo';
import { Globe, GraduationCap, ZoomIn, ZoomOut, Home, BookOpen, Target, FileText, Users, CheckCircle2 } from 'lucide-react';

export default function Header({
  lang,
  setLang,
  fontSize,
  setFontSize,
  onGoHome,
  showHomeButton = true,
  currentTab = 'solver',
  setCurrentTab,
}) {
  const navTabs = [
    {
      id: 'solver',
      labelEn: 'Solve Math',
      labelTe: 'లెక్కలు సాధించు',
      icon: BookOpen,
      badge: 'Interactive',
    },
    {
      id: 'formulas',
      labelEn: 'Formulas to Byheart',
      labelTe: 'ముఖ్య సూత్రాలు',
      icon: CheckCircle2,
      badge: '14 Chapters',
    },
    {
      id: 'examprep',
      labelEn: 'How to Pass SSC',
      labelTe: 'పాస్ గ్యారెంటీ (40+)',
      icon: Target,
      badge: '40+ Marks',
    },
    {
      id: 'pastpapers',
      labelEn: 'Past Board Papers',
      labelTe: 'పాత ప్రశ్నాపత్రాలు',
      icon: FileText,
      badge: 'AP & TS',
    },
    {
      id: 'teacher',
      labelEn: 'Teacher Portal',
      labelTe: 'ఉపాధ్యాయుల విభాగం',
      icon: Users,
    },
  ];

  return (
    <header className="sticky top-0 z-40 bg-[#fbfbf9]/95 backdrop-blur-md border-b border-[#edece8] shadow-xs transition-all">
      {/* Top Bar */}
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-2.5 flex items-center justify-between gap-3">
        {/* Mascot Logo & Title */}
        <div
          className="flex items-center gap-2.5 cursor-pointer hover:opacity-90 transition-opacity"
          onClick={onGoHome}
          title="Go to Home Screen"
        >
          <MascotLogo className="w-10 h-10" />
          <div>
            <div className="flex items-center gap-2">
              <span className="text-lg sm:text-xl font-black tracking-tight text-slate-800">
                SSC Math Mitra
              </span>
              <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800">
                గణిత మిత్ర
              </span>
            </div>
            <p className="text-[11px] text-slate-500 font-medium">
              10th Class SSC • Telangana & Andhra Pradesh
            </p>
          </div>
        </div>

        {/* Controls: Home, Font Sizer, English/Telugu Language Switcher */}
        <div className="flex items-center gap-2 sm:gap-2.5">
          {/* Home Button */}
          {showHomeButton && (
            <button
              onClick={onGoHome}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-100 text-xs font-semibold text-slate-700 transition-all cursor-pointer"
              title="Return to Home Screen"
            >
              <Home className="w-3.5 h-3.5 text-rose-600" />
              <span className="hidden sm:inline">{lang === 'te' ? 'హోమ్' : 'Home'}</span>
            </button>
          )}

          {/* Font Size Adjusters */}
          <div className="hidden sm:flex items-center bg-slate-100 rounded-lg p-0.5 border border-slate-200">
            <button
              onClick={() => setFontSize(Math.max(14, fontSize - 2))}
              className="p-1 text-slate-600 hover:text-amber-700 rounded cursor-pointer"
              title="Smaller Font"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <span className="text-[11px] font-bold px-1.5 text-slate-600">{fontSize}px</span>
            <button
              onClick={() => setFontSize(Math.min(22, fontSize + 2))}
              className="p-1 text-slate-600 hover:text-amber-700 rounded cursor-pointer"
              title="Larger Font"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Language Switcher: Only English / Telugu */}
          <button
            onClick={() => setLang(lang === 'en' ? 'te' : 'en')}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl border border-amber-300 bg-amber-50 hover:bg-amber-100 text-amber-900 text-xs font-bold transition-all cursor-pointer shadow-2xs"
          >
            <Globe className="w-3.5 h-3.5 text-amber-700" />
            <span>{lang === 'en' ? 'తెలుగు' : 'English'}</span>
          </button>
        </div>
      </div>

      {/* Navigation Tabs Bar */}
      <div className="border-t border-[#edece8] bg-white/70 overflow-x-auto scrollbar-none">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 flex items-center gap-1 sm:gap-2 py-1.5 min-w-max">
          {navTabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = currentTab === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => setCurrentTab(tab.id)}
                className={`flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                  isActive
                    ? 'bg-[#c01e2e] text-white shadow-2xs'
                    : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-amber-300' : 'text-slate-400'}`} />
                <span>{lang === 'te' ? tab.labelTe : tab.labelEn}</span>
                {tab.badge && (
                  <span
                    className={`text-[9px] px-1.5 py-0.2 rounded-full font-bold ml-0.5 ${
                      isActive
                        ? 'bg-white/20 text-white'
                        : 'bg-slate-100 text-slate-500'
                    }`}
                  >
                    {tab.badge}
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>
    </header>
  );
}
