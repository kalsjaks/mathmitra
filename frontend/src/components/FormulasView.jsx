import React, { useState, useEffect } from 'react';
import { BookOpen, Sparkles, ChevronDown, ChevronUp, Award, Lightbulb, Search } from 'lucide-react';
import { fetchFormulas } from '../services/api';
import MathRenderer from './MathRenderer';

export default function FormulasView({ lang = 'en' }) {
  const [formulasData, setFormulasData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [openChapterId, setOpenChapterId] = useState(1);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    loadFormulas();
  }, []);

  const loadFormulas = async () => {
    setLoading(true);
    try {
      const data = await fetchFormulas();
      if (data && data.chapters) {
        setFormulasData(data.chapters);
      }
    } catch (e) {
      console.error('Failed to load formulas', e);
    } finally {
      setLoading(false);
    }
  };

  const filteredChapters = formulasData.filter((ch) => {
    const q = searchQuery.toLowerCase();
    const nameEn = ch.name_en?.toLowerCase() || '';
    const nameTe = ch.name_te || '';
    return nameEn.includes(q) || nameTe.includes(q);
  });

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-[#b91c1c] via-[#991b1b] to-[#7f1d1d] rounded-3xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-2xl space-y-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/20 text-red-100 backdrop-blur-md">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>{lang === 'te' ? '10వ తరగతి SSC ముఖ్య సూత్రాలు' : 'Formulas to Byheart • 14 Chapters'}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            {lang === 'te' ? 'ముఖ్యమైన గణిత సూత్రాలు & సులువైన ట్రిక్స్' : 'All 14 Chapters Formulas & Key Notes'}
          </h2>
          <p className="text-xs sm:text-sm text-red-100/90 leading-relaxed">
            {lang === 'te'
              ? 'పరీక్షల్లో గరిష్ట మార్కులు సాధించడానికి ప్రతి అధ్యాయం నుండి ఖచ్చితంగా గుర్తుంచుకోవలసిన సూత్రాలు మరియు షార్ట్‌కట్ చిట్కాలు.'
              : 'Every formula, condition, and mnemonic you need to remember for SSC Board Exams, with Telugu translations and step tips.'}
          </p>
        </div>
      </div>

      {/* Search Bar */}
      <div className="flex items-center gap-2 bg-white rounded-2xl p-3 border border-slate-200 shadow-2xs">
        <Search className="w-4 h-4 text-slate-400 ml-2" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder={lang === 'te' ? 'అధ్యాయం పేరు వెతకండి (ఉదా: వాస్తవ సంఖ్యలు, Trigonometry)...' : 'Search chapter formulas (e.g. Real Numbers, Trigonometry)...'}
          className="w-full bg-transparent text-xs sm:text-sm outline-hidden text-slate-800 placeholder:text-slate-400"
        />
        {searchQuery && (
          <button
            onClick={() => setSearchQuery('')}
            className="text-xs text-slate-400 hover:text-slate-600 px-2 py-1"
          >
            {lang === 'te' ? 'రద్దు' : 'Clear'}
          </button>
        )}
      </div>

      {/* Loading State */}
      {loading ? (
        <div className="text-center py-12 text-slate-500">
          <div className="inline-block w-8 h-8 border-4 border-rose-600 border-t-transparent rounded-full animate-spin mb-3"></div>
          <p className="text-xs font-bold">{lang === 'te' ? 'సూత్రాలు లోడ్ అవుతున్నాయి...' : 'Loading 14-Chapter Formulas...'}</p>
        </div>
      ) : (
        /* Chapters Accordion */
        <div className="space-y-4">
          {filteredChapters.map((ch) => {
            const isOpen = openChapterId === ch.id;
            return (
              <div
                key={ch.id}
                className="bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden transition-all hover:border-rose-300"
              >
                {/* Chapter Title Bar */}
                <button
                  onClick={() => setOpenChapterId(isOpen ? null : ch.id)}
                  className="w-full px-5 py-4 flex items-center justify-between text-left hover:bg-slate-50 transition-colors cursor-pointer"
                >
                  <div className="flex items-center gap-3">
                    <span className="w-8 h-8 rounded-xl bg-rose-100 text-rose-900 font-black text-xs sm:text-sm flex items-center justify-center flex-shrink-0">
                      {ch.id}
                    </span>
                    <div>
                      <h3 className="text-sm sm:text-base font-bold text-slate-800">
                        {lang === 'te' ? `${ch.name_te} (${ch.name_en})` : `${ch.name_en} (${ch.name_te})`}
                      </h3>
                      <div className="flex items-center gap-2 mt-0.5 text-[11px] text-slate-500 font-medium">
                        <span className="px-2 py-0.5 rounded-full bg-slate-100 text-slate-700">
                          {ch.category}
                        </span>
                        <span>•</span>
                        <span className="text-rose-700 font-bold flex items-center gap-1">
                          <Award className="w-3 h-3 text-rose-600" />
                          {ch.weightage}
                        </span>
                      </div>
                    </div>
                  </div>

                  <div className="p-1 rounded-lg text-slate-400 hover:text-slate-700">
                    {isOpen ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                  </div>
                </button>

                {/* Chapter Formula Details */}
                {isOpen && (
                  <div className="p-5 border-t border-slate-100 bg-slate-50/50 space-y-4">
                    {/* Formulas List */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                      {ch.formulas?.map((f, idx) => (
                        <div
                          key={idx}
                          className="p-4 rounded-xl bg-white border border-slate-200/80 shadow-2xs space-y-2 hover:border-rose-300 transition-colors"
                        >
                          <div className="flex items-center justify-between">
                            <span className="text-xs font-bold text-slate-800">
                              {lang === 'te' && f.title_te ? f.title_te : f.title_en}
                            </span>
                            <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-rose-50 text-rose-800 border border-rose-200">
                              Formula #{idx + 1}
                            </span>
                          </div>

                          {/* Equation Rendered */}
                          <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100 overflow-x-auto text-center my-1.5">
                            <MathRenderer content={`$$${f.latex}$$`} />
                          </div>

                          {/* Note / Tip */}
                          <p className="text-[11px] text-slate-600 leading-relaxed">
                            {lang === 'te' && f.note_te ? f.note_te : f.note_en}
                          </p>
                        </div>
                      ))}
                    </div>

                    {/* Mnemonic / Teacher Tip */}
                    {ch.mnemonic && (
                      <div className="p-3.5 rounded-xl bg-amber-50 border border-amber-200 flex items-start gap-2.5 text-xs text-amber-900">
                        <Lightbulb className="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" />
                        <div>
                          <span className="font-bold">
                            {lang === 'te' ? 'గుర్తుంచుకోవడానికి సులువైన ట్రిక్ (Mnemonic): ' : 'Quick Memory Tip: '}
                          </span>
                          <span>{ch.mnemonic}</span>
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
