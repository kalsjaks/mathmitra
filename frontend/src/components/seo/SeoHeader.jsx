import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Sparkles, Menu, X, ArrowRight, BookOpen, Compass, Shapes, HelpCircle, Calculator } from 'lucide-react';

const NAV_LINKS = [
  { path: '/ssc-maths-formulas', label: 'All 14 Formulas', icon: BookOpen },
  { path: '/algebra-formulas', label: 'Algebra', icon: Calculator },
  { path: '/geometry-formulas', label: 'Geometry', icon: Shapes },
  { path: '/trigonometry-formulas', label: 'Trigonometry', icon: Compass },
  { path: '/ssc-important-questions', label: 'Important Questions', icon: HelpCircle },
];

export default function SeoHeader() {
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
        {/* Logo & Brand */}
        <Link to="/" className="flex items-center gap-2.5 group">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-[#c01e2e] to-rose-500 flex items-center justify-center text-white font-black text-lg shadow-sm group-hover:scale-105 transition-transform">
            M
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-slate-900 tracking-tight text-base sm:text-lg group-hover:text-[#c01e2e] transition-colors">
                Math Mitra
              </span>
              <span className="text-[11px] font-semibold text-rose-700 bg-rose-50 px-1.5 py-0.5 rounded border border-rose-150">
                గణిత మిత్ర
              </span>
            </div>
            <p className="text-[10px] text-slate-500 font-medium hidden sm:block">
              10th SSC Maths Companion • AP & Telangana
            </p>
          </div>
        </Link>

        {/* Desktop Nav Links */}
        <nav className="hidden lg:flex items-center gap-1">
          {NAV_LINKS.map((item) => {
            const isActive = location.pathname === item.path;
            const Icon = item.icon;
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 ${
                  isActive
                    ? 'bg-rose-50 text-[#c01e2e] border border-rose-200/80 shadow-2xs'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-[#c01e2e]' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </Link>
            );
          })}
        </nav>

        {/* Right CTA */}
        <div className="flex items-center gap-2.5">
          <Link
            to="/?tab=solver"
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-gradient-to-r from-[#c01e2e] to-[#a81926] text-white text-xs font-bold shadow-sm hover:shadow-md hover:brightness-110 active:scale-95 transition-all"
          >
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>Open AI Solver</span>
            <ArrowRight className="w-3 h-3 ml-0.5" />
          </Link>

          {/* Mobile menu toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100 focus:outline-hidden"
            aria-label="Toggle navigation menu"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-slate-200 bg-white px-4 py-3 space-y-1 shadow-lg animate-fade-in">
          <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider px-2 py-1">
            SSC Revision Guides
          </div>
          {NAV_LINKS.map((item) => {
            const isActive = location.pathname === item.path;
            const Icon = item.icon;
            return (
              <Link
                key={item.path}
                to={item.path}
                onClick={() => setMobileMenuOpen(false)}
                className={`w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold transition-all ${
                  isActive
                    ? 'bg-rose-50 text-[#c01e2e] font-extrabold border border-rose-200'
                    : 'text-slate-700 hover:bg-slate-50'
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? 'text-[#c01e2e]' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </Link>
            );
          })}
          <div className="pt-2 border-t border-slate-100">
            <Link
              to="/?tab=solver"
              onClick={() => setMobileMenuOpen(false)}
              className="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl bg-[#c01e2e] text-white text-xs font-bold shadow-xs"
            >
              <Sparkles className="w-4 h-4 text-amber-300" />
              <span>Launch MathMitra Solver</span>
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
