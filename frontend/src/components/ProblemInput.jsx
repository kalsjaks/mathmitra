import React, { useState, useEffect, useRef } from 'react';
import { Search, Mic, MicOff, Camera, BookOpen, Sparkles, CheckCircle2, ArrowRight, FileQuestion } from 'lucide-react';
import { fetchQuestionPreview } from '../services/api';

export default function ProblemInput({
  onSolve,
  onOpenOcr,
  chapters = [],
  loading,
  lang
}) {
  const [activeTab, setActiveTab] = useState('textbook'); // Default to textbook selector
  const [query, setQuery] = useState('');
  const [selectedChapterId, setSelectedChapterId] = useState('1');
  const [selectedExercise, setSelectedExercise] = useState('1.1');
  const [selectedProblemNum, setSelectedProblemNum] = useState('1');
  const [selectedSubQuestion, setSelectedSubQuestion] = useState(null);
  const [questionPreview, setQuestionPreview] = useState(null);
  const [previewLoading, setPreviewLoading] = useState(false);
  const [customProblemText, setCustomProblemText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [speechError, setSpeechError] = useState('');
  const recognitionRef = useRef(null);

  const currentChapter = chapters.find(c => String(c.id) === String(selectedChapterId)) || chapters[0];

  useEffect(() => {
    if (currentChapter && currentChapter.exercises?.length > 0) {
      setSelectedExercise(currentChapter.exercises[0]);
    }
  }, [selectedChapterId, chapters]);

  // Load question preview whenever exercise or problem number changes
  useEffect(() => {
    if (selectedExercise && selectedProblemNum) {
      loadPreview(selectedExercise, selectedProblemNum);
    }
  }, [selectedExercise, selectedProblemNum]);

  const loadPreview = async (ex, qNum) => {
    setPreviewLoading(true);
    setSelectedSubQuestion(null);
    try {
      const data = await fetchQuestionPreview(ex, parseInt(qNum) || 1);
      setQuestionPreview(data);
    } catch (e) {
      console.warn('Failed to load question preview', e);
      setQuestionPreview(null);
    } finally {
      setPreviewLoading(false);
    }
  };

  // Quick problem number options
  const problemNumbers = ['1', '2', '3', '4', '5', '6', '7', '8'];

  // Examples for Type or Speak
  const examples = lang === 'te' ? [
    { label: 'యూక్లిడ్ గ.సా.భా (1.2 & 0.12)', q: 'Can you find the HCF of 1.2 and 0.12 by using Euclid division algorithm? Justify your answer.' },
    { label: 'యూక్లిడ్ గ.సా.భా (900 & 270)', q: 'యూక్లిడ్ విశేషవిధి ద్వారా 900 మరియు 270 ల గ.సా.భా కనుగొనుము', ex: '1.1' },
    { label: 'శూన్యాలు: 2 & -1/3 (వర్గ బహుపది)', q: 'Find the quadratic polynomial whose zeroes are 2 and -1/3', ex: '3.3' },
    { label: 'వర్గ సమీకరణం (x² + 5x + 6 = 0)', q: 'వర్గ సమీకరణం x^2 + 5x + 6 = 0 యొక్క మూలాలను కనుగొనండి', ex: '5.2' },
    { label: 'త్రికోణమితి (sin²θ + cos²θ = 1)', q: 'త్రికోణమితి సర్వసమీకరణం sin^2 theta + cos^2 theta = 1 నిరూపించండి', ex: '11.4' },
    { label: 'అంకశ్రేఢి 10వ పదం (AP)', q: 'అంకశ్రేఢి 2, 7, 12, ... లో 10వ పదాన్ని కనుగొనండి', ex: '6.2' },
  ] : [
    { label: 'Euclid HCF of 1.2 & 0.12 (Decimals)', q: 'Can you find the HCF of 1.2 and 0.12 by using Euclid division algorithm? Justify your answer.' },
    { label: 'Euclid HCF of 900 & 270', q: 'Find the HCF of 900 and 270 using Euclid division algorithm', ex: '1.1' },
    { label: 'Zeroes: 2 & -1/3 (Quadratic Poly)', q: 'Find the quadratic polynomial whose zeroes are 2 and -1/3', ex: '3.3' },
    { label: 'Quadratic Equation (x² + 5x + 6)', q: 'Find the roots of quadratic equation x^2 + 5x + 6 = 0', ex: '5.2' },
    { label: 'Trig Identity (sin²θ + cos²θ = 1)', q: 'Prove that sin^2 theta + cos^2 theta = 1', ex: '11.4' },
    { label: '10th term of AP 2, 7, 12...', q: 'Find the 10th term of the AP: 2, 7, 12, ...', ex: '6.2' },
  ];

  // Speech-to-text setup
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = lang === 'te' ? 'te-IN' : 'en-IN';

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        setQuery(transcript);
        setIsListening(false);
      };

      recognition.onerror = (err) => {
        console.warn('Speech recognition error:', err);
        setSpeechError(lang === 'te' ? 'వాయిస్ లోపం. దయచేసి స్పష్టంగా మాట్లాడండి లేదా టైప్ చేయండి.' : 'Voice error. Please speak clearly or type below.');
        setIsListening(false);
      };

      recognition.onend = () => setIsListening(false);
      recognitionRef.current = recognition;
    }
  }, [lang]);

  const toggleListening = () => {
    setSpeechError('');
    if (!recognitionRef.current) {
      alert(lang === 'te' ? 'ఈ బ్రౌజర్‌లో వాయిస్ ఇన్పుట్ సదుపాయం లేదు. దయచేసి టైప్ చేయండి.' : 'Speech recognition is not supported in this browser. Please type.');
      return;
    }

    if (isListening) {
      recognitionRef.current.stop();
      setIsListening(false);
    } else {
      try {
        recognitionRef.current.lang = lang === 'te' ? 'te-IN' : 'en-IN';
        recognitionRef.current.start();
        setIsListening(true);
      } catch (e) {
        console.error(e);
        setIsListening(false);
      }
    }
  };

  // Handler for Textbook section submission
  const handleTextbookSolve = () => {
    const chName = lang === 'te' ? currentChapter?.name_te : currentChapter?.name_en;
    let targetQuery = '';

    if (customProblemText.trim()) {
      targetQuery = customProblemText.trim();
    } else if (selectedSubQuestion) {
      targetQuery = `Exercise ${selectedExercise}, Question ${selectedProblemNum} ${selectedSubQuestion.part}: ${selectedSubQuestion.text}`;
    } else if (questionPreview && questionPreview.question_text) {
      targetQuery = `Exercise ${selectedExercise}, Question ${selectedProblemNum}: ${questionPreview.question_text}`;
    } else {
      targetQuery = `${chName} - Exercise ${selectedExercise}, Question ${selectedProblemNum}`;
    }

    onSolve({
      query: targetQuery,
      exercise: selectedExercise,
      page: null,
      action_type: 'solve',
    });
  };

  // Handler for Type or Speak submission
  const handleTypedSolve = () => {
    if (!query.trim()) return;
    onSolve({
      query: query.trim(),
      exercise: null,
      page: null,
      action_type: 'solve',
    });
  };

  return (
    <div className="w-full max-w-4xl mx-auto space-y-4">
      {/* Tab Switcher: 1. Select from Textbook | 2. Type or Speak Problem */}
      <div className="flex items-center justify-between border-b border-slate-200 pb-3">
        <div className="flex items-center gap-2">
          {/* Tab 1: Textbook Selection */}
          <button
            onClick={() => setActiveTab('textbook')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer ${
              activeTab === 'textbook'
                ? 'bg-[#c01e2e] text-white shadow-sm'
                : 'text-slate-600 hover:bg-slate-100'
            }`}
          >
            <BookOpen className="w-4 h-4 text-amber-300" />
            <span>{lang === 'te' ? '1. పాఠ్యపుస్తకం నుండి ఎంచుకోండి' : '1. Select from Textbook'}</span>
          </button>

          {/* Tab 2: Type or Speak */}
          <button
            onClick={() => setActiveTab('text')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer ${
              activeTab === 'text'
                ? 'bg-[#c01e2e] text-white shadow-sm'
                : 'text-slate-600 hover:bg-slate-100'
            }`}
          >
            <Search className="w-4 h-4 text-amber-300" />
            <span>{lang === 'te' ? '2. టైప్ చేయండి / మాట్లాడండి' : '2. Type or Speak Problem'}</span>
          </button>
        </div>

        {/* Camera Snapshot Button */}
        <button
          onClick={onOpenOcr}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-[#c01e2e] hover:bg-[#a81926] text-white text-xs font-bold shadow-xs transition-all cursor-pointer"
          title="Snap Photo of Problem"
        >
          <Camera className="w-4 h-4" />
          <span className="hidden sm:inline">{lang === 'te' ? 'ఫోటో తీయండి' : 'Snap Photo'}</span>
        </button>
      </div>

      {/* ======================================================== */}
      {/* FEATURE 1: Select Topic / Chapter / Section / Problem   */}
      {/* ======================================================== */}
      {activeTab === 'textbook' && (
        <div className="space-y-4 bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 shadow-2xs">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {/* Step 1: Select Chapter */}
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                {lang === 'te' ? '1. అధ్యాయం / టాపిక్ (Chapter)' : '1. Select Topic / Chapter'}
              </label>
              <select
                value={selectedChapterId}
                onChange={(e) => setSelectedChapterId(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-slate-300 bg-[#fbfbf9] text-xs sm:text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-amber-500"
              >
                {chapters.map((ch) => (
                  <option key={ch.id} value={ch.id}>
                    {ch.id}. {lang === 'te' ? `${ch.name_te} (${ch.name_en})` : `${ch.name_en} (${ch.name_te})`}
                  </option>
                ))}
              </select>
            </div>

            {/* Step 2: Select Exercise */}
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                {lang === 'te' ? '2. అభ్యాసం (Exercise / Section)' : '2. Select Exercise / Section'}
              </label>
              <select
                value={selectedExercise}
                onChange={(e) => setSelectedExercise(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-slate-300 bg-[#fbfbf9] text-xs sm:text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-amber-500"
              >
                {currentChapter?.exercises?.map((ex) => (
                  <option key={ex} value={ex}>
                    Exercise {ex} {lang === 'te' ? `(అభ్యాసం ${ex})` : ''}
                  </option>
                )) || <option value="1.1">Exercise 1.1</option>}
              </select>
            </div>

            {/* Step 3: Select Problem Number */}
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1.5">
                {lang === 'te' ? '3. లెక్క సంఖ్య (Problem Number)' : '3. Problem Number'}
              </label>
              <select
                value={selectedProblemNum}
                onChange={(e) => setSelectedProblemNum(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-slate-300 bg-[#fbfbf9] text-xs sm:text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-amber-500"
              >
                {problemNumbers.map((num) => (
                  <option key={num} value={num}>
                    {lang === 'te' ? `ప్రశ్న ${num} (Question ${num})` : `Question ${num}`}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* LIVE TEXTBOOK QUESTION PREVIEW (As requested by user!) */}
          <div className="p-4 rounded-2xl bg-amber-50/70 border border-amber-200/80 space-y-2.5 transition-all">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-amber-950 flex items-center gap-1.5">
                <FileQuestion className="w-4 h-4 text-amber-700" />
                <span>
                  {lang === 'te'
                    ? `ఎంచుకున్న పాఠ్యపుస్తక ప్రశ్న (అభ్యాసం ${selectedExercise}, ప్రశ్న ${selectedProblemNum}):`
                    : `Textbook Question Preview (Exercise ${selectedExercise}, Q${selectedProblemNum}):`}
                </span>
              </span>
              {previewLoading && (
                <span className="text-[11px] font-semibold text-amber-700 animate-pulse">
                  {lang === 'te' ? 'ప్రశ్న లోడ్ అవుతోంది...' : 'Loading question...'}
                </span>
              )}
            </div>

            {questionPreview && questionPreview.question_text ? (
              <div className="space-y-2">
                <p className="text-xs sm:text-sm font-semibold text-slate-800 leading-relaxed bg-white p-3 rounded-xl border border-amber-200/60 shadow-2xs">
                  {questionPreview.question_text}
                </p>

                {/* Sub-questions clickable chips if available */}
                {questionPreview.sub_questions && questionPreview.sub_questions.length > 0 && (
                  <div className="space-y-1.5 pt-1">
                    <span className="text-[11px] font-bold text-amber-900 block">
                      {lang === 'te' ? 'సబ్-ప్రశ్నను ఎంచుకోండి (ఐచ్ఛికం):' : 'Select Sub-Question Part to solve:'}
                    </span>
                    <div className="flex flex-wrap gap-2">
                      {questionPreview.sub_questions.map((sub, idx) => {
                        const isSelected = selectedSubQuestion?.part === sub.part;
                        return (
                          <button
                            key={idx}
                            type="button"
                            onClick={() => setSelectedSubQuestion(isSelected ? null : sub)}
                            className={`text-xs px-3 py-1.5 rounded-xl border font-medium transition-all cursor-pointer ${
                              isSelected
                                ? 'bg-amber-600 text-white border-amber-600 shadow-2xs'
                                : 'bg-white text-slate-700 border-amber-200 hover:border-amber-400'
                            }`}
                          >
                            <span className="font-bold mr-1">{sub.part}</span>
                            <span>{sub.text}</span>
                          </button>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <p className="text-xs text-amber-800/80 italic">
                {lang === 'te'
                  ? `అభ్యాసం ${selectedExercise}, ప్రశ్న ${selectedProblemNum} సాధించడానికి సిద్ధంగా ఉంది.`
                  : `Ready to solve Exercise ${selectedExercise}, Question ${selectedProblemNum}.`}
              </p>
            )}
          </div>

          {/* Optional specific problem question custom override */}
          <div>
            <label className="block text-xs font-bold text-slate-600 mb-1">
              {lang === 'te' ? 'అంకెలు లేదా కస్టమ్ లెక్క మార్చాలనుకుంటే ఇక్కడ టైప్ చేయండి (ఐచ్ఛికం):' : 'Custom Numbers / Specific Variation (Optional):'}
            </label>
            <input
              type="text"
              value={customProblemText}
              onChange={(e) => setCustomProblemText(e.target.value)}
              placeholder={
                lang === 'te'
                  ? 'ఉదా: 900 మరియు 270 ల గ.సా.భా, లేదా 1.2 మరియు 0.12...'
                  : 'e.g. Find HCF of 900 and 270, or 1.2 and 0.12...'
              }
              className="w-full p-2.5 rounded-xl border border-slate-300 bg-[#fbfbf9] text-xs sm:text-sm font-medium text-slate-800 focus:ring-2 focus:ring-amber-500"
            />
          </div>

          {/* ONLY ONE SINGLE ACTION BUTTON (Removed duplicate 'Explain How to Solve') */}
          <div className="flex items-center justify-end pt-2 border-t border-slate-100">
            <button
              type="button"
              disabled={loading}
              onClick={handleTextbookSolve}
              className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-3 rounded-2xl bg-[#c01e2e] hover:bg-[#a51927] text-white font-black text-sm sm:text-base shadow-md hover:shadow-lg transition-all cursor-pointer"
            >
              {loading ? (
                <span>{lang === 'te' ? 'సాధిస్తున్నాం...' : 'Solving...'}</span>
              ) : (
                <>
                  <CheckCircle2 className="w-5 h-5" />
                  <span>{lang === 'te' ? 'ఈ లెక్కను సాధించండి' : 'Solve Problem'}</span>
                  <ArrowRight className="w-4 h-4 ml-1 stroke-[3]" />
                </>
              )}
            </button>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* FEATURE 2: Type or Speak Any Problem                     */}
      {/* ======================================================== */}
      {activeTab === 'text' && (
        <div className="space-y-4 bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 shadow-2xs">
          <div className="relative rounded-2xl border-2 border-slate-200 focus-within:border-amber-500 bg-[#fbfbf9] p-3 transition-all">
            <textarea
              rows={3}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={
                lang === 'te'
                  ? 'మీ లెక్కను ఇక్కడ టైప్ చేయండి లేదా మైక్ నొక్కి మాట్లాడండి (ఉదా: 900 మరియు 270 ల గ.సా.భా, లేదా 1.2 and 0.12, x^2 + 5x + 6 = 0)...'
                  : 'Type any math problem or tap the mic to speak (e.g. Find HCF of 1.2 and 0.12, roots of x^2 + 5x + 6, sin 30)...'
              }
              className="w-full p-1 text-sm sm:text-base focus:outline-none bg-transparent text-slate-800 placeholder:text-slate-400 resize-none"
            />

            <div className="flex items-center justify-between pt-2 border-t border-slate-200">
              {/* Voice Mic Button */}
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={toggleListening}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold transition-all cursor-pointer ${
                    isListening
                      ? 'bg-rose-500 text-white animate-pulse shadow-sm'
                      : 'bg-amber-100 hover:bg-amber-200 text-amber-900 border border-amber-300'
                  }`}
                  title="Speak in English or Telugu"
                >
                  {isListening ? <MicOff className="w-3.5 h-3.5" /> : <Mic className="w-3.5 h-3.5" />}
                  <span>
                    {isListening
                      ? lang === 'te' ? 'వింటున్నాం...' : 'Listening...'
                      : lang === 'te' ? 'వాయిస్ మైక్ (మాట్లాడండి)' : 'Voice Mic (Speak)'}
                  </span>
                </button>

                {speechError && (
                  <span className="text-xs text-rose-600 font-medium">{speechError}</span>
                )}
              </div>

              {/* Character hint */}
              <span className="text-[11px] text-slate-400">English & తెలుగు</span>
            </div>
          </div>

          {/* Quick Examples */}
          <div className="flex flex-wrap items-center gap-2 pt-1">
            <span className="text-xs font-semibold text-slate-500 flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              {lang === 'te' ? 'ఉదాహరణ లెక్కలు:' : 'Try Examples:'}
            </span>
            {examples.map((item, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => {
                  setQuery(item.q);
                  onSolve({ query: item.q, exercise: item.ex, page: null, action_type: 'solve' });
                }}
                className="text-xs font-medium px-3 py-1.5 rounded-xl bg-slate-50 text-slate-700 border border-slate-200 hover:border-amber-400 hover:text-amber-900 hover:bg-amber-50/50 transition-all cursor-pointer"
              >
                {item.label}
              </button>
            ))}
          </div>

          {/* ONLY ONE SINGLE ACTION BUTTON (Removed duplicate 'Explain How to Solve') */}
          <div className="flex items-center justify-end pt-2 border-t border-slate-100">
            <button
              type="button"
              disabled={loading || !query.trim()}
              onClick={handleTypedSolve}
              className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-3 rounded-2xl bg-[#c01e2e] hover:bg-[#a51927] text-white font-black text-sm sm:text-base shadow-md hover:shadow-lg transition-all cursor-pointer disabled:opacity-50"
            >
              {loading ? (
                <span>{lang === 'te' ? 'సాధిస్తున్నాం...' : 'Solving...'}</span>
              ) : (
                <>
                  <CheckCircle2 className="w-5 h-5" />
                  <span>{lang === 'te' ? 'ఈ లెక్కను సాధించండి' : 'Solve Problem'}</span>
                  <ArrowRight className="w-4 h-4 ml-1 stroke-[3]" />
                </>
              )}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
