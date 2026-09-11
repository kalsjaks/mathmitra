import React, { useState, useEffect } from 'react';
import { Target, CheckCircle, Calendar, Sparkles, AlertTriangle, ArrowRight, BookOpen } from 'lucide-react';
import { fetchExamPrep } from '../services/api';

export default function ExamPrepView({ onSolveQuery, lang = 'en' }) {
  const [examData, setExamData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('guaranteed'); // 'guaranteed' | 'high_yield' | 'plan'

  useEffect(() => {
    loadExamData();
  }, []);

  const loadExamData = async () => {
    setLoading(true);
    try {
      const data = await fetchExamPrep();
      setExamData(data);
    } catch (e) {
      console.error('Failed to load exam prep data', e);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="text-center py-16 text-slate-500">
        <div className="inline-block w-8 h-8 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin mb-3"></div>
        <p className="text-xs font-bold">{lang === 'te' ? 'పరీక్ష ప్రణాళిక లోడ్ అవుతోంది...' : 'Loading 40+ Marks Passing Strategy...'}</p>
      </div>
    );
  }

  if (!examData) return null;

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Top Banner: 40+ Marks Guarantee */}
      <div className="bg-gradient-to-r from-emerald-600 via-teal-700 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-2xl space-y-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/20 text-emerald-100 backdrop-blur-md">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>{lang === 'te' ? '100% పాస్ గ్యారెంటీ ప్రణాళిక' : '100% Passing Blueprint • 40+ Marks'}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            {lang === 'te' ? examData.title_te : examData.title_en}
          </h2>
          <p className="text-xs sm:text-sm text-emerald-100/90 leading-relaxed font-medium">
            {lang === 'te' ? examData.slogan_te : examData.slogan_en}
          </p>
        </div>
      </div>

      {/* Navigation Sub-Tabs */}
      <div className="flex flex-wrap items-center gap-2 p-1.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <button
          onClick={() => setActiveTab('guaranteed')}
          className={`flex-1 min-w-[160px] py-2.5 px-4 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeTab === 'guaranteed'
              ? 'bg-emerald-600 text-white shadow-xs'
              : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          <Target className="w-4 h-4" />
          <span>{lang === 'te' ? '15 ఖచ్చితంగా వచ్చే ప్రశ్నలు' : '15 Must-Pass Questions'}</span>
        </button>

        <button
          onClick={() => setActiveTab('high_yield')}
          className={`flex-1 min-w-[160px] py-2.5 px-4 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeTab === 'high_yield'
              ? 'bg-emerald-600 text-white shadow-xs'
              : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          <BookOpen className="w-4 h-4" />
          <span>{lang === 'te' ? 'ముఖ్యమైన అధ్యాయాలు (High Yield)' : 'Top High-Yield Chapters'}</span>
        </button>

        <button
          onClick={() => setActiveTab('plan')}
          className={`flex-1 min-w-[160px] py-2.5 px-4 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeTab === 'plan'
              ? 'bg-emerald-600 text-white shadow-xs'
              : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          <Calendar className="w-4 h-4" />
          <span>{lang === 'te' ? '5 రోజుల రివిజన్ ప్లాన్' : '5-Day Fast Track Plan'}</span>
        </button>
      </div>

      {/* TAB 1: 15 GUARANTEED QUESTIONS */}
      {activeTab === 'guaranteed' && (
        <div className="space-y-3">
          <div className="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-900 flex items-start gap-2.5">
            <AlertTriangle className="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" />
            <div>
              <p className="font-bold">
                {lang === 'te'
                  ? 'ఈ 15 మోడల్ ప్రశ్నలను సాధిస్తే చాలు, 40 మార్కులతో సులభంగా పాస్ అవ్వచ్చు!'
                  : 'Mastering these 15 recurring question types guarantees 40+ marks in the SSC Board Examination!'}
              </p>
              <p className="text-[11px] text-amber-800 mt-0.5">
                {lang === 'te'
                  ? 'ప్రతి ప్రశ్న పక్కనున్న "సాధించండి" బటన్ నొక్కి వెంటనే పూర్తి స్టెప్-బై-స్టెప్ సొల్యూషన్ చూడండి.'
                  : 'Click "Solve This" on any question to instantly view the step-by-step teacher solution.'}
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
            {examData.guaranteed_questions?.map((item, idx) => (
              <div
                key={idx}
                className="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs hover:border-emerald-300 transition-all flex flex-col justify-between space-y-3"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-800 border border-emerald-200">
                      Q#{idx + 1} • {item.chapter}
                    </span>
                    <span className="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                      {item.marks}
                    </span>
                  </div>

                  <h4 className="text-xs sm:text-sm font-bold text-slate-800">
                    {lang === 'te' && item.topic_te ? item.topic_te : item.topic_en}
                  </h4>

                  <p className="text-[11px] text-slate-600 bg-slate-50 p-2.5 rounded-xl border border-slate-100 font-mono">
                    {item.typical_question}
                  </p>

                  <p className="text-[11px] text-emerald-800 font-medium">
                    💡 <span className="font-bold">{lang === 'te' ? 'పరీక్ష చిట్కా: ' : 'SSC Tip: '}</span>
                    {lang === 'te' && item.tip_te ? item.tip_te : item.tip_en}
                  </p>
                </div>

                <button
                  onClick={() => onSolveQuery(item.typical_question)}
                  className="w-full py-2 px-3 rounded-xl bg-emerald-50 hover:bg-emerald-600 text-emerald-700 hover:text-white text-xs font-bold border border-emerald-200 hover:border-emerald-600 transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-2xs"
                >
                  <span>{lang === 'te' ? 'దీనిని సాధించండి' : 'Solve This Problem'}</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 2: HIGH-YIELD CHAPTERS */}
      {activeTab === 'high_yield' && (
        <div className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {examData.high_yield_chapters?.map((ch, idx) => (
              <div
                key={idx}
                className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs space-y-3"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-800 font-black text-xs flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <h3 className="text-sm font-bold text-slate-800">
                      {lang === 'te' && ch.name_te ? `${ch.name_te} (${ch.name_en})` : `${ch.name_en} (${ch.name_te})`}
                    </h3>
                  </div>
                  <span className="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                    {ch.weightage}
                  </span>
                </div>

                <div className="space-y-1 text-xs text-slate-600">
                  <p className="font-semibold text-slate-700">
                    {lang === 'te' ? 'ఖచ్చితంగా వచ్చే అంశాలు:' : 'Must-practice topics:'}
                  </p>
                  <ul className="list-disc list-inside space-y-1 text-[11px] text-slate-600 pl-1">
                    {ch.must_practice?.map((p, pIdx) => (
                      <li key={pIdx}>{p}</li>
                    ))}
                  </ul>
                </div>

                <div className="p-2.5 rounded-xl bg-slate-50 border border-slate-100 text-[11px] text-slate-700">
                  <span className="font-bold text-emerald-800">{lang === 'te' ? 'లక్ష్యం: ' : 'Target: '}</span>
                  <span>{ch.target_marks}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: 5-DAY STUDY PLAN */}
      {activeTab === 'plan' && (
        <div className="space-y-3">
          {examData.five_day_plan?.map((day, idx) => (
            <div
              key={idx}
              className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-4"
            >
              <div className="flex items-start gap-3">
                <span className="px-3 py-1.5 rounded-xl bg-teal-100 text-teal-900 font-extrabold text-xs flex-shrink-0">
                  Day {day.day}
                </span>
                <div>
                  <h4 className="text-sm font-bold text-slate-800">{day.focus}</h4>
                  <p className="text-xs text-slate-500 mt-0.5">{day.chapters}</p>
                  <p className="text-[11px] text-emerald-800 font-medium mt-1">
                    🎯 {lang === 'te' ? 'లక్ష్యం: ' : 'Daily Target: '}{day.target}
                  </p>
                </div>
              </div>

              <div className="text-right flex-shrink-0">
                <span className="inline-block text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
                  +{day.estimated_marks} Marks
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
