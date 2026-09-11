import React from 'react';
import MascotLogo from './MascotLogo';
import { ArrowRight, Globe, Sparkles, BookOpen, CheckCircle2, Target, FileText, Users } from 'lucide-react';

export default function HomeScreen({ onStart, onNavigateTab, lang, setLang }) {
  return (
    <section className="relative w-full min-h-[92vh] bg-gradient-to-b from-[#c01e2e] via-[#a81926] to-[#88131e] text-white flex flex-col justify-between px-4 sm:px-8 py-6 sm:py-10 shadow-xl rounded-b-[2.5rem]">
      {/* Background pattern */}
      <div className="absolute inset-0 opacity-10 pointer-events-none bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:20px_20px]" />

      {/* Top Header Row */}
      <div className="relative z-10 flex items-center justify-between max-w-5xl mx-auto w-full">
        {/* Mascot Logo and Title */}
        <div className="flex items-center gap-3">
          <MascotLogo className="w-14 h-14 sm:w-16 sm:h-16" />
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl sm:text-2xl lg:text-3xl font-black tracking-tight">
                SSC Math Mitra
              </h1>
              <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-white/20 text-amber-200 backdrop-blur-md">
                గణిత మిత్ర
              </span>
            </div>
            <p className="text-xs sm:text-sm text-red-100 font-medium">
              {lang === 'te' ? '10వ తరగతి విద్యార్థుల కోసం సులువైన గైడ్' : 'Your friendly math guide for SSC students'}
            </p>
          </div>
        </div>

        {/* English / Telugu Switcher */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => setLang(lang === 'en' ? 'te' : 'en')}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/20 hover:bg-white/30 text-white text-xs font-bold transition-all border border-white/30 cursor-pointer shadow-xs"
          >
            <Globe className="w-3.5 h-3.5 text-amber-300" />
            <span>{lang === 'en' ? 'తెలుగు (Telugu)' : 'English'}</span>
          </button>
        </div>
      </div>

      {/* Main Center Area: Students Photo + Welcoming Start Card */}
      <div className="relative z-10 max-w-5xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-8 items-center my-6">
        {/* Left Side: Indian School Students Image */}
        <div className="lg:col-span-6 flex justify-center">
          <div className="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/25 max-w-md w-full aspect-[4/3] group">
            <img
              src="/students_hero.jpg"
              alt="Students Studying Mathematics"
              className="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent flex items-end p-4 sm:p-5">
              <p className="text-xs sm:text-sm font-semibold text-white/95 leading-snug">
                {lang === 'te'
                  ? 'ప్రభుత్వ & ప్రైవేట్ పాఠశాలల విద్యార్థుల కోసం ఉచిత మ్యాథ్స్ గైడ్'
                  : 'Empowering SSC students to solve math step-by-step with joy!'}
              </p>
            </div>
          </div>
        </div>

        {/* Right Side: Simple Welcoming Information & Big START Button */}
        <div className="lg:col-span-6 flex flex-col items-center lg:items-start text-center lg:text-left space-y-4">
          <div className="space-y-2">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/20 text-white text-xs font-bold backdrop-blur-md">
              <Sparkles className="w-3.5 h-3.5 text-amber-300" />
              <span>{lang === 'te' ? 'నేరుగా ఓపెన్ చేయండి • 100% ఉచితం' : 'No Login Required • 100% Free'}</span>
            </span>

            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white leading-tight">
              {lang === 'te' ? (
                <>
                  గణితాన్ని సులభంగా <br className="hidden sm:inline" />
                  <span className="text-amber-300">నేర్చుకోండి & సాధించండి!</span>
                </>
              ) : (
                <>
                  Learn & Solve Math <br className="hidden sm:inline" />
                  <span className="text-amber-300">the Simple Way!</span>
                </>
              )}
            </h2>

            <p className="text-xs sm:text-sm text-red-100 max-w-md leading-relaxed">
              {lang === 'te'
                ? 'పాఠ్యపుస్తకం నుండి ఏదైనా ప్రశ్న ఎంచుకోండి లేదా టైప్ చేయండి / మైక్ ద్వారా అడగండి. ఉపాధ్యాయుల లాంటి సులువైన వివరణ పొందండి.'
                : 'Pick any topic from your 10th Class textbook, or type / speak any problem to get teacher-guided step-by-step explanations.'}
            </p>
          </div>

          {/* THE BIG, PROMINENT "START SOLVING" BUTTON */}
          <button
            onClick={() => onStart ? onStart() : onNavigateTab('solver')}
            className="w-full sm:w-auto min-w-[260px] py-4 px-8 rounded-2xl sm:rounded-3xl bg-amber-400 hover:bg-amber-300 text-slate-900 font-black text-lg sm:text-xl shadow-xl hover:shadow-amber-500/40 hover:-translate-y-0.5 active:translate-y-0 transition-all flex items-center justify-center gap-3 cursor-pointer border-b-4 border-amber-600"
          >
            <span>{lang === 'te' ? 'లెక్కలు సాధించండి ➔' : 'Start Solving Math ➔'}</span>
          </button>
        </div>
      </div>

      {/* QUICK FEATURE LAUNCHPAD CARDS (Direct Access to All 4 Features) */}
      <div className="relative z-10 max-w-5xl mx-auto w-full pt-4 pb-2">
        <div className="text-center mb-3">
          <span className="text-xs font-bold text-red-100 uppercase tracking-wider">
            {lang === 'te' ? 'ముఖ్యమైన విభాగాలు (డైరెక్ట్ ఓపెన్):' : 'Explore Core Sections (1-Click Access):'}
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {/* Card 1: Solver */}
          <button
            onClick={() => onNavigateTab ? onNavigateTab('solver') : onStart()}
            className="p-4 rounded-2xl bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-left transition-all hover:-translate-y-0.5 cursor-pointer flex flex-col justify-between space-y-2 group shadow-2xs"
          >
            <div className="w-9 h-9 rounded-xl bg-amber-400/20 text-amber-300 flex items-center justify-center">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white group-hover:text-amber-300 transition-colors">
                {lang === 'te' ? '1. లెక్కల సాధన' : '1. Solve Math'}
              </h4>
              <p className="text-[11px] text-red-100/80 mt-0.5">
                {lang === 'te' ? 'పాఠ్యపుస్తక ప్రశ్నలు & వాయిస్ ఇన్పుట్' : 'Textbook picker & voice solver'}
              </p>
            </div>
          </button>

          {/* Card 2: Formulas to Byheart */}
          <button
            onClick={() => onNavigateTab ? onNavigateTab('formulas') : onStart()}
            className="p-4 rounded-2xl bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-left transition-all hover:-translate-y-0.5 cursor-pointer flex flex-col justify-between space-y-2 group shadow-2xs"
          >
            <div className="w-9 h-9 rounded-xl bg-emerald-400/20 text-emerald-300 flex items-center justify-center">
              <CheckCircle2 className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white group-hover:text-emerald-300 transition-colors">
                {lang === 'te' ? '2. ముఖ్య సూత్రాలు' : '2. Formulas to Byheart'}
              </h4>
              <p className="text-[11px] text-red-100/80 mt-0.5">
                {lang === 'te' ? '14 అధ్యాయాల సూత్రాలు & ట్రిక్స్' : 'All 14 chapters formulas & notes'}
              </p>
            </div>
          </button>

          {/* Card 3: How to Pass SSC (40+ Marks) */}
          <button
            onClick={() => onNavigateTab ? onNavigateTab('examprep') : onStart()}
            className="p-4 rounded-2xl bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-left transition-all hover:-translate-y-0.5 cursor-pointer flex flex-col justify-between space-y-2 group shadow-2xs"
          >
            <div className="w-9 h-9 rounded-xl bg-teal-400/20 text-teal-300 flex items-center justify-center">
              <Target className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white group-hover:text-teal-300 transition-colors">
                {lang === 'te' ? '3. పాస్ గ్యారెంటీ (40+)' : '3. Pass Guarantee (40+)'}
              </h4>
              <p className="text-[11px] text-red-100/80 mt-0.5">
                {lang === 'te' ? '15 ఖచ్చితంగా వచ్చే ప్రశ్నలు' : '15 must-pass questions & plan'}
              </p>
            </div>
          </button>

          {/* Card 4: Past Papers & Teacher Portal */}
          <button
            onClick={() => onNavigateTab ? onNavigateTab('pastpapers') : onStart()}
            className="p-4 rounded-2xl bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-left transition-all hover:-translate-y-0.5 cursor-pointer flex flex-col justify-between space-y-2 group shadow-2xs"
          >
            <div className="w-9 h-9 rounded-xl bg-indigo-400/20 text-indigo-300 flex items-center justify-center">
              <FileText className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white group-hover:text-indigo-300 transition-colors">
                {lang === 'te' ? '4. బోర్డు పరీక్ష పేపర్లు' : '4. Past Board Papers'}
              </h4>
              <p className="text-[11px] text-red-100/80 mt-0.5">
                {lang === 'te' ? 'గత సంవత్సరాల ప్రశ్నాపత్రాలు' : 'AP & TS SSC previous papers'}
              </p>
            </div>
          </button>
        </div>
      </div>

      {/* Bottom Subtle Note */}
      <div className="relative z-10 text-center text-xs text-red-200/80 pt-2 pb-1">
        <span>Telangana & Andhra Pradesh SSC 10th Class Mathematics</span>
      </div>
    </section>
  );
}
