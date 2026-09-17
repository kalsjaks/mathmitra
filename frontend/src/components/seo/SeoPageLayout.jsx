import React from 'react';
import { Link } from 'react-router-dom';
import SeoHead from './SeoHead';
import SeoHeader from './SeoHeader';
import MathRenderer from '../MathRenderer';
import { 
  Sparkles, 
  ArrowRight, 
  BookOpen, 
  CheckCircle2, 
  HelpCircle, 
  Share2, 
  ChevronRight, 
  Calculator, 
  Heart,
  FileText
} from 'lucide-react';

export default function SeoPageLayout({ pageData }) {
  if (!pageData) return null;

  const {
    title,
    description,
    canonicalUrl,
    badge,
    h1,
    subtitle,
    updatedDate,
    tableOfContents = [],
    sections = [],
    faqs = []
  } = pageData;

  // Build JSON-LD structured data for FAQ Schema
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    'mainEntity': faqs.map((faq) => ({
      '@type': 'Question',
      'name': faq.q,
      'acceptedAnswer': {
        '@type': 'Answer',
        'text': faq.a,
      },
    })),
  };

  const handleShare = async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title,
          text: description,
          url: window.location.href,
        });
      } catch (err) {
        console.log('Share dismissed');
      }
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('Link copied to clipboard!');
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#fbfbf9] text-slate-800 antialiased selection:bg-[#c01e2e] selection:text-white">
      {/* 1. Dynamic SEO Metadata */}
      <SeoHead
        title={title}
        description={description}
        canonicalUrl={canonicalUrl}
        jsonLd={jsonLd}
      />

      {/* 2. Top Navigation Bar */}
      <SeoHeader />

      {/* 3. Main Article Body */}
      <main className="flex-1 max-w-5xl w-full mx-auto px-4 sm:px-6 py-8 space-y-8 animate-fade-in">
        {/* Breadcrumb Navigation */}
        <nav aria-label="Breadcrumb" className="flex items-center gap-1.5 text-xs text-slate-500 font-medium">
          <Link to="/" className="hover:text-[#c01e2e] transition-colors">Home</Link>
          <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
          <span className="text-slate-400">SSC Resources</span>
          <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
          <span className="text-slate-800 font-semibold truncate max-w-xs">{badge}</span>
        </nav>

        {/* Hero Section */}
        <header className="relative bg-gradient-to-br from-rose-900 via-[#991b1b] to-[#7f1d1d] rounded-3xl p-6 sm:p-10 text-white shadow-md overflow-hidden">
          <div className="absolute -right-12 -bottom-12 w-64 h-64 bg-white/5 rounded-full blur-2xl pointer-events-none" />
          <div className="relative z-10 space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/15 text-rose-100 backdrop-blur-md border border-white/20">
              <Sparkles className="w-3.5 h-3.5 text-amber-300" />
              <span>{badge}</span>
            </div>

            <h1 className="text-2xl sm:text-4xl font-black text-white leading-tight tracking-tight">
              {h1}
            </h1>

            <p className="text-sm sm:text-base text-rose-100/90 leading-relaxed font-normal">
              {subtitle}
            </p>

            {/* Meta tags / Quick Info */}
            <div className="pt-2 flex flex-wrap items-center gap-4 text-xs text-rose-200">
              <span className="flex items-center gap-1">
                <FileText className="w-3.5 h-3.5" />
                <span>Updated: {updatedDate}</span>
              </span>
              <span>&bull;</span>
              <span>SCERT Telangana & AP State Board</span>
              <span>&bull;</span>
              <button
                onClick={handleShare}
                className="flex items-center gap-1 text-white hover:text-amber-200 font-bold underline cursor-pointer"
              >
                <Share2 className="w-3.5 h-3.5" />
                <span>Share Guide</span>
              </button>
            </div>

            {/* Quick Action Buttons */}
            <div className="pt-4 flex flex-wrap items-center gap-3">
              <Link
                to="/?tab=solver"
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white text-[#991b1b] font-bold text-xs sm:text-sm shadow-md hover:bg-rose-50 transition-all hover:scale-[1.02] active:scale-95 cursor-pointer"
              >
                <Calculator className="w-4 h-4 text-[#c01e2e]" />
                <span>Solve Any SSC Problem with AI</span>
              </Link>
              <Link
                to="/?tab=formulas"
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs sm:text-sm backdrop-blur-md border border-white/20 transition-all cursor-pointer"
              >
                <BookOpen className="w-4 h-4 text-amber-300" />
                <span>Open Formulas App</span>
              </Link>
            </div>
          </div>
        </header>

        {/* Quick Table of Contents Card */}
        {tableOfContents.length > 0 && (
          <div className="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-2xs">
            <h2 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-[#c01e2e]" />
              <span>In This Revision Guide</span>
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-semibold text-slate-700">
              {tableOfContents.map((item, idx) => (
                <div key={idx} className="flex items-center gap-2 py-1">
                  <span className="w-5 h-5 rounded-full bg-rose-50 text-[#c01e2e] flex items-center justify-center font-bold text-[11px] flex-shrink-0">
                    {idx + 1}
                  </span>
                  <span className="truncate">{item}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Content Sections */}
        <div className="space-y-8">
          {sections.map((sec, idx) => (
            <section
              key={sec.id || idx}
              id={sec.id}
              className="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200/80 shadow-2xs space-y-4"
            >
              <div className="flex items-center gap-2.5 pb-3 border-b border-slate-100">
                <span className="w-7 h-7 rounded-xl bg-rose-50 text-[#c01e2e] flex items-center justify-center font-black text-xs">
                  {idx + 1}
                </span>
                <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight">
                  {sec.heading}
                </h2>
              </div>

              {/* Render Section Math and Markdown */}
              <div className="prose prose-slate max-w-none">
                <MathRenderer content={sec.content} />
              </div>
            </section>
          ))}
        </div>

        {/* FAQs Section */}
        {faqs.length > 0 && (
          <section className="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200/80 shadow-2xs space-y-5">
            <div className="flex items-center gap-2.5 pb-2 border-b border-slate-100">
              <HelpCircle className="w-5 h-5 text-[#c01e2e]" />
              <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight">
                Frequently Asked Questions (FAQs)
              </h2>
            </div>

            <div className="space-y-4">
              {faqs.map((faq, idx) => (
                <div key={idx} className="bg-slate-50/70 rounded-xl p-4 border border-slate-200/60">
                  <h3 className="text-sm sm:text-base font-bold text-slate-900 flex items-start gap-2 mb-1.5">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                    <span>{faq.q}</span>
                  </h3>
                  <p className="text-xs sm:text-sm text-slate-600 leading-relaxed pl-6">
                    {faq.a}
                  </p>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Bottom Interactive CTA Banner */}
        <section className="bg-gradient-to-r from-amber-50 via-rose-50 to-orange-50 rounded-3xl p-6 sm:p-8 border border-rose-200/60 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-5">
          <div className="space-y-1.5 text-center sm:text-left">
            <span className="text-[11px] font-bold uppercase tracking-wider text-rose-700 bg-white px-2.5 py-1 rounded-full border border-rose-200 shadow-2xs">
              Math Mitra AI Practice
            </span>
            <h3 className="text-lg sm:text-xl font-black text-slate-900">
              Stuck on a tricky 10th Class problem?
            </h3>
            <p className="text-xs sm:text-sm text-slate-600 max-w-lg">
              Solve any AP or TS textbook exercise problem step-by-step with reasons in Telugu and English.
            </p>
          </div>

          <Link
            to="/?tab=solver"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-[#c01e2e] hover:bg-[#a81926] text-white font-bold text-xs sm:text-sm shadow-md transition-all hover:scale-105 active:scale-95 flex-shrink-0 cursor-pointer"
          >
            <Sparkles className="w-4 h-4 text-amber-300" />
            <span>Open AI Solver Now</span>
            <ArrowRight className="w-4 h-4 ml-1" />
          </Link>
        </section>
      </main>

      {/* 4. Footer */}
      <footer className="border-t border-[#edece8] bg-[#f7f6f2] py-8 mt-12">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-4 text-xs text-slate-600">
            <div className="flex items-center gap-2 font-bold text-slate-800">
              <span>SSC Math Mitra • గణిత మిత్ర</span>
              <span>&bull;</span>
              <span className="font-normal text-slate-500">AP & Telangana Class 10</span>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <Link to="/ssc-maths-formulas" className="hover:text-[#c01e2e] transition-colors">14 Formulas</Link>
              <span>&bull;</span>
              <Link to="/algebra-formulas" className="hover:text-[#c01e2e] transition-colors">Algebra</Link>
              <span>&bull;</span>
              <Link to="/geometry-formulas" className="hover:text-[#c01e2e] transition-colors">Geometry</Link>
              <span>&bull;</span>
              <Link to="/trigonometry-formulas" className="hover:text-[#c01e2e] transition-colors">Trigonometry</Link>
              <span>&bull;</span>
              <Link to="/ssc-important-questions" className="hover:text-[#c01e2e] transition-colors">Important Questions</Link>
            </div>
          </div>

          <div className="pt-3 border-t border-slate-200/60 flex flex-col sm:flex-row items-center justify-between gap-2 text-[11px] text-slate-500">
            <p>© {new Date().getFullYear()} Math Mitra. Designed for Telangana & Andhra Pradesh 10th Class Students.</p>
            <p className="flex items-center gap-1">
              <span>Empowering students to achieve 10/10 GPA</span>
              <Heart className="w-3 h-3 text-rose-500 fill-rose-500 ml-1" />
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
