import React, { useState, useEffect } from 'react';
import { Target, CheckCircle2, Calendar, Sparkles, AlertTriangle, ArrowRight, BookOpen, Award, Check } from 'lucide-react';
import { fetchExamPrep } from '../services/api';

export default function ExamPrepView({ onSolveQuery, lang = 'en' }) {
  const [examData, setExamData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('plan'); // default to 'plan' as requested by user
  const [selectedDay, setSelectedDay] = useState(1);
  const [selectedChapterId, setSelectedChapterId] = useState(null);
  const [completedProblems, setCompletedProblems] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem('math_mitra_completed_plan') || '{}');
    } catch (e) {
      return {};
    }
  });

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

  const toggleProblemCompleted = (problemId) => {
    const updated = {
      ...completedProblems,
      [problemId]: !completedProblems[problemId]
    };
    setCompletedProblems(updated);
    try {
      localStorage.setItem('math_mitra_completed_plan', JSON.stringify(updated));
    } catch (e) {
      console.warn('Could not persist plan progress', e);
    }
  };

  if (loading) {
    return (
      <div className="text-center py-16 text-slate-500">
        <div className="inline-block w-8 h-8 border-4 border-rose-600 border-t-transparent rounded-full animate-spin mb-3"></div>
        <p className="text-xs font-bold">{lang === 'te' ? 'పరీక్ష ప్రణాళిక లోడ్ అవుతోంది...' : 'Loading 40+ Marks Passing Strategy...'}</p>
      </div>
    );
  }

  if (!examData) return null;

  // Active day object for the 5-day plan
  const activeDayPlan = examData.five_day_plan?.find(d => d.day === selectedDay) || examData.five_day_plan?.[0];
  const activeChapters = activeDayPlan?.chapters || [];
  const currentChapter = activeChapters.find(c => c.id === selectedChapterId) || activeChapters[0] || {};

  // Calculate day completion stats
  let totalDayQuestions = 0;
  let completedDayQuestions = 0;
  if (activeDayPlan?.chapters) {
    activeDayPlan.chapters.forEach(ch => {
      ch.questions?.forEach(q => {
        totalDayQuestions++;
        if (completedProblems[q.id]) completedDayQuestions++;
      });
    });
  }
  const dayProgressPercent = totalDayQuestions > 0 ? Math.round((completedDayQuestions / totalDayQuestions) * 100) : 0;

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Top Banner: 40+ Marks Guarantee */}
      <div className="bg-gradient-to-r from-[#b91c1c] via-[#991b1b] to-[#7f1d1d] rounded-3xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-2xl space-y-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/20 text-red-100 backdrop-blur-md">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>{lang === 'te' ? '100% పాస్ గ్యారెంటీ ప్రణాళిక' : '100% Passing Blueprint • 40+ Marks'}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            {lang === 'te' ? examData.title_te : examData.title_en}
          </h2>
          <p className="text-xs sm:text-sm text-red-100/90 leading-relaxed font-medium">
            {lang === 'te' ? examData.slogan_te : examData.slogan_en}
          </p>
        </div>
      </div>

      {/* Navigation Sub-Tabs */}
      <div className="flex flex-wrap items-center gap-2 p-1.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <button
          onClick={() => setActiveTab('plan')}
          className={`flex-1 min-w-[160px] py-2.5 px-4 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeTab === 'plan'
              ? 'bg-[#c01e2e] text-white shadow-xs'
              : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          <Calendar className="w-4 h-4" />
          <span>{lang === 'te' ? '5 రోజుల ఫాస్ట్ ట్రాక్ ప్లాన్ (14 చాప్టర్లు)' : '5-Day Fast Track Plan (All 14 Chapters)'}</span>
        </button>

        <button
          onClick={() => setActiveTab('guaranteed')}
          className={`flex-1 min-w-[160px] py-2.5 px-4 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeTab === 'guaranteed'
              ? 'bg-[#c01e2e] text-white shadow-xs'
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
              ? 'bg-[#c01e2e] text-white shadow-xs'
              : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          <BookOpen className="w-4 h-4" />
          <span>{lang === 'te' ? 'ముఖ్యమైన అధ్యాయాలు (High Yield)' : 'Top High-Yield Chapters'}</span>
        </button>
      </div>

      {/* TAB 1: 5-DAY FAST TRACK PLAN (ALL 14 CHAPTERS & 140 QUESTIONS) */}
      {activeTab === 'plan' && (
        <div className="space-y-5">
          {/* Day Selector Bar */}
          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            {examData.five_day_plan?.map((dayObj) => {
              const isSelected = selectedDay === dayObj.day;
              return (
                <button
                  key={dayObj.day}
                  onClick={() => {
                    setSelectedDay(dayObj.day);
                    setSelectedChapterId(null);
                  }}
                  className={`p-3 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between space-y-1.5 shadow-2xs ${
                    isSelected
                      ? 'bg-[#c01e2e] text-white border-[#a81926] shadow-md ring-2 ring-rose-200'
                      : 'bg-white hover:bg-rose-50 text-slate-800 border-slate-200'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className={`text-xs font-black px-2 py-0.5 rounded-md ${
                      isSelected ? 'bg-white/20 text-white' : 'bg-rose-100 text-rose-900 font-bold'
                    }`}>
                      Day {dayObj.day}
                    </span>
                    <span className={`text-[10px] font-bold ${
                      isSelected ? 'text-amber-200' : 'text-slate-500'
                    }`}>
                      {dayObj.target_marks?.split(' ')[0] || '+8M'}
                    </span>
                  </div>
                  <h4 className={`text-xs font-bold truncate ${isSelected ? 'text-white' : 'text-slate-800'}`}>
                    {lang === 'te' ? dayObj.theme_te : dayObj.theme_en}
                  </h4>
                  <p className={`text-[10px] truncate ${isSelected ? 'text-red-100' : 'text-slate-500'}`}>
                    {dayObj.chapters?.length || 0} {lang === 'te' ? 'అధ్యాయాలు • 10 ప్రశ్నలు' : 'Chapters • 10 Qs each'}
                  </p>
                </button>
              );
            })}
          </div>

          {/* Active Day Overview Card */}
          {activeDayPlan && (
            <div className="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-2xs space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-900">
                      Day {activeDayPlan.day} of 5
                    </span>
                    <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-900 border border-amber-200">
                      Target: {activeDayPlan.target_marks}
                    </span>
                  </div>
                  <h3 className="text-lg sm:text-xl font-black text-slate-900 mt-1">
                    {lang === 'te' ? activeDayPlan.title_te : activeDayPlan.title_en}
                  </h3>
                  <p className="text-xs text-slate-600 mt-0.5">
                    {lang === 'te' ? activeDayPlan.theme_te : activeDayPlan.theme_en} • {activeChapters.length} {lang === 'te' ? 'అధ్యాయాలు (ప్రతి అధ్యాయంలో 10 ముఖ్య ప్రశ్నలు)' : 'Chapters (10 Most Important Questions each)'}
                  </p>
                </div>

                {/* Progress for this Day */}
                <div className="sm:text-right flex-shrink-0">
                  <div className="text-xs font-bold text-slate-700">
                    {lang === 'te' ? 'నేటి సాధన పురోగతి:' : 'Daily Practice Progress:'}
                  </div>
                  <div className="text-sm font-black text-rose-700">
                    {completedDayQuestions} / {totalDayQuestions} {lang === 'te' ? 'పూర్తయ్యాయి' : 'Completed'} ({dayProgressPercent}%)
                  </div>
                  <div className="w-36 bg-slate-100 rounded-full h-2.5 mt-1.5 overflow-hidden border border-slate-200">
                    <div
                      className="bg-gradient-to-r from-rose-500 to-[#c01e2e] h-2.5 rounded-full transition-all duration-500"
                      style={{ width: `${dayProgressPercent}%` }}
                    />
                  </div>
                </div>
              </div>

              {/* Chapter Selector Tabs for Current Day */}
              <div>
                <div className="text-xs font-bold text-slate-500 mb-2 uppercase tracking-wider">
                  {lang === 'te' ? 'ఈ రోజు అధ్యాయాన్ని ఎంచుకోండి:' : 'Select Chapter to Practice:'}
                </div>
                <div className="flex flex-wrap gap-2">
                  {activeChapters.map((ch) => {
                    const isChSelected = (currentChapter.id === ch.id);
                    let chDoneCount = 0;
                    ch.questions?.forEach(q => {
                      if (completedProblems[q.id]) chDoneCount++;
                    });
                    const chTotal = ch.questions?.length || 10;

                    return (
                      <button
                        key={ch.id}
                        onClick={() => setSelectedChapterId(ch.id)}
                        className={`py-2 px-3.5 rounded-xl border text-xs font-bold transition-all cursor-pointer flex items-center gap-2 ${
                          isChSelected
                            ? 'bg-[#c01e2e] text-white border-[#c01e2e] shadow-2xs'
                            : 'bg-rose-50/60 hover:bg-rose-100 text-slate-800 border-rose-200'
                        }`}
                      >
                        <span>Ch {ch.id}: {lang === 'te' ? ch.name_te : ch.name_en}</span>
                        <span className={`text-[10px] px-1.5 py-0.2 rounded-md font-bold ${
                          isChSelected ? 'bg-white/20 text-white' : 'bg-white text-rose-800 border border-rose-200'
                        }`}>
                          {chDoneCount}/{chTotal}
                        </span>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* 10 Problems Grid for Selected Chapter */}
              {currentChapter && (
                <div className="pt-2 space-y-3">
                  <div className="flex items-center justify-between bg-rose-50/50 p-3 rounded-2xl border border-rose-100">
                    <span className="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                      <Award className="w-4 h-4 text-rose-600" />
                      <span>
                        Ch {currentChapter.id}: {lang === 'te' ? `${currentChapter.name_te} (${currentChapter.name_en})` : `${currentChapter.name_en} (${currentChapter.name_te})`}
                      </span>
                    </span>
                    <span className="text-xs font-extrabold text-rose-900 bg-white px-2.5 py-1 rounded-lg border border-rose-200">
                      Weightage: {currentChapter.weightage}
                    </span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                    {currentChapter.questions?.map((item, qIdx) => {
                      const isCompleted = !!completedProblems[item.id];
                      
                      // Mark pill styling
                      let markColor = 'bg-slate-100 text-slate-800 border-slate-200';
                      if (item.marks === '2 Marks') markColor = 'bg-rose-50 text-rose-800 border-rose-200';
                      if (item.marks === '4 Marks') markColor = 'bg-amber-50 text-amber-900 border-amber-200';
                      if (item.marks === '8 Marks') markColor = 'bg-red-100 text-red-900 border-red-300 font-extrabold';

                      return (
                        <div
                          key={item.id || qIdx}
                          className={`rounded-2xl p-4 sm:p-5 border transition-all flex flex-col justify-between space-y-3.5 ${
                            isCompleted
                              ? 'bg-rose-50/40 border-rose-300 shadow-2xs'
                              : 'bg-white border-slate-200 hover:border-rose-300 shadow-2xs'
                          }`}
                        >
                          <div className="space-y-2">
                            <div className="flex items-center justify-between gap-2">
                              <div className="flex items-center gap-1.5">
                                <span className={`text-[10px] font-bold px-2 py-0.5 rounded-md border ${markColor}`}>
                                  {item.marks}
                                </span>
                                <span className="text-[11px] font-bold text-slate-500">
                                  #{qIdx + 1}
                                </span>
                              </div>
                              <span className="text-[10px] font-semibold text-rose-900 bg-rose-50/80 px-2 py-0.5 rounded-md border border-rose-200 truncate max-w-[180px]">
                                {item.trend}
                              </span>
                            </div>

                            {/* Question Text in Primary Language */}
                            <h4 className="text-xs sm:text-sm font-bold text-slate-900 leading-snug">
                              {lang === 'te' ? item.q_te : item.q_en}
                            </h4>

                            {/* Secondary Language Translation */}
                            <p className="text-[11px] text-slate-500 italic leading-relaxed">
                              {lang === 'te' ? item.q_en : item.q_te}
                            </p>

                            {/* Concept Hint */}
                            {item.concept && (
                              <div className="text-[10px] font-medium text-slate-600 bg-slate-50 p-2 rounded-xl border border-slate-100">
                                <span className="font-bold text-rose-900">💡 Key Concept: </span>
                                <span>{item.concept}</span>
                              </div>
                            )}
                          </div>

                          {/* Action Controls: Checkbox & 1-Click Solve Button */}
                          <div className="flex items-center gap-2 pt-2 border-t border-slate-100">
                            <button
                              type="button"
                              onClick={() => toggleProblemCompleted(item.id)}
                              className={`py-2 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 border ${
                                isCompleted
                                  ? 'bg-emerald-600 text-white border-emerald-600 shadow-2xs'
                                  : 'bg-slate-50 hover:bg-slate-100 text-slate-600 border-slate-200'
                              }`}
                              title={isCompleted ? 'Mark as Incomplete' : 'Mark as Practiced'}
                            >
                              <Check className="w-3.5 h-3.5" />
                              <span className="hidden sm:inline">
                                {isCompleted ? (lang === 'te' ? 'సాధించాను' : 'Practiced') : (lang === 'te' ? 'గుర్తుంచు' : 'Mark Done')}
                              </span>
                            </button>

                            <button
                              type="button"
                              onClick={() => onSolveQuery(item.q_en)}
                              className="flex-1 py-2 px-3.5 rounded-xl bg-rose-50 hover:bg-[#c01e2e] text-rose-900 hover:text-white text-xs font-bold border border-rose-200 hover:border-[#c01e2e] transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-2xs group"
                            >
                              <span>{lang === 'te' ? 'లెక్కను సాధించండి' : 'Solve with Math Mitra'}</span>
                              <ArrowRight className="w-3.5 h-3.5 text-rose-600 group-hover:text-white group-hover:translate-x-0.5 transition-transform" />
                            </button>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* TAB 2: 15 MUST-PASS QUESTIONS */}
      {activeTab === 'guaranteed' && (
        <div className="space-y-3">
          <div className="p-4 rounded-2xl bg-rose-50/80 border border-rose-200 text-xs text-rose-950 flex items-start gap-2.5">
            <AlertTriangle className="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" />
            <div>
              <p className="font-bold">
                {lang === 'te'
                  ? 'ఈ 15 మోడల్ ప్రశ్నలను సాధిస్తే చాలు, 40 మార్కులతో సులభంగా పాస్ అవ్వచ్చు!'
                  : 'Mastering these 15 recurring question types guarantees 40+ marks in the SSC Board Examination!'}
              </p>
              <p className="text-[11px] text-rose-800 mt-0.5">
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
                className="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs hover:border-rose-300 transition-all flex flex-col justify-between space-y-3"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-rose-50 text-rose-800 border border-rose-200">
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

                  <p className="text-[11px] text-rose-900 font-medium">
                    💡 <span className="font-bold">{lang === 'te' ? 'పరీక్ష చిట్కా: ' : 'SSC Tip: '}</span>
                    {lang === 'te' && item.tip_te ? item.tip_te : item.tip_en}
                  </p>
                </div>

                <button
                  onClick={() => onSolveQuery(item.typical_question)}
                  className="w-full py-2 px-3 rounded-xl bg-rose-50 hover:bg-[#c01e2e] text-rose-900 hover:text-white text-xs font-bold border border-rose-200 hover:border-[#c01e2e] transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-2xs"
                >
                  <span>{lang === 'te' ? 'దీనిని సాధించండి' : 'Solve This Problem'}</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: HIGH-YIELD CHAPTERS */}
      {activeTab === 'high_yield' && (
        <div className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {examData.high_yield_chapters?.map((ch, idx) => (
              <div
                key={idx}
                className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs space-y-3 hover:border-rose-300 transition-all"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="w-7 h-7 rounded-lg bg-rose-100 text-rose-900 font-black text-xs flex items-center justify-center">
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
                  <span className="font-bold text-rose-900">{lang === 'te' ? 'లక్ష్యం: ' : 'Target: '}</span>
                  <span>{ch.target_marks}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
