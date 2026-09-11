import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import HomeScreen from './components/HomeScreen';
import ProblemInput from './components/ProblemInput';
import SolutionViewer from './components/SolutionViewer';
import FormulasView from './components/FormulasView';
import ExamPrepView from './components/ExamPrepView';
import PastPapersView from './components/PastPapersView';
import TeacherDashboard from './components/TeacherDashboard';
import CameraOcrModal from './components/CameraOcrModal';
import EmailModal from './components/EmailModal';
import { fetchChapters, solveProblem } from './services/api';
import { History, CheckCircle2, Heart, ArrowLeft, BookOpen, Target } from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('app'); // Default directly to app workspace so students never get stuck!
  const [currentTab, setCurrentTab] = useState('solver'); // 'solver' | 'formulas' | 'examprep' | 'pastpapers' | 'teacher'
  const [lang, setLang] = useState('en'); // 'en' | 'te'
  const [fontSize, setFontSize] = useState(16);
  const [chapters, setChapters] = useState([]);
  const [solutionData, setSolutionData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isOcrOpen, setIsOcrOpen] = useState(false);
  const [isEmailModalOpen, setIsEmailModalOpen] = useState(false);
  const [recentHistory, setRecentHistory] = useState([]);

  useEffect(() => {
    loadInitialData();
  }, []);

  const loadInitialData = async () => {
    try {
      const data = await fetchChapters();
      if (data && data.chapters) {
        setChapters(data.chapters);
      }
    } catch (err) {
      console.warn('Could not load online chapters:', err);
    }

    const saved = localStorage.getItem('math_mitra_history');
    if (saved) {
      setRecentHistory(JSON.parse(saved).slice(0, 5));
    }
  };

  const handleStart = () => {
    setCurrentView('app');
    setCurrentTab('solver');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleNavigateTab = (tabId) => {
    setCurrentView('app');
    setCurrentTab(tabId);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleGoHome = () => {
    setCurrentView('home');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSolve = async ({ query, exercise, page, language = 'auto', action_type = 'solve' }) => {
    setLoading(true);
    try {
      const res = await solveProblem({
        query,
        exercise,
        page,
        language: lang === 'te' ? 'te' : language,
        action_type
      });
      setSolutionData(res);
      if (res.language && !lang) {
        setLang(res.language);
      }

      const saved = localStorage.getItem('math_mitra_history');
      if (saved) {
        setRecentHistory(JSON.parse(saved).slice(0, 5));
      }

      setTimeout(() => {
        const el = document.getElementById('solution-section');
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } catch (err) {
      alert(lang === 'te' ? 'లెక్క సాధించడంలో సమస్య ఎదురైంది. దయచేసి మళ్ళీ ప్రయత్నించండి.' : 'Error solving problem. Please check your query or network connection.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="min-h-screen flex flex-col bg-[#fbfbf9] text-slate-800 transition-colors"
      style={{ fontSize: `${fontSize}px` }}
    >
      {/* 1. SIMPLE HOME / LANDING PAGE */}
      {currentView === 'home' && (
        <HomeScreen
          onStart={handleStart}
          onNavigateTab={handleNavigateTab}
          lang={lang}
          setLang={setLang}
        />
      )}

      {/* 2. MAIN APPLICATION WORKSPACE & CORE MODULES */}
      {currentView === 'app' && (
        <>
          {/* Header with Navigation Tabs (Solver, Formulas, Exam Prep 40+, Past Papers, Teacher Portal) */}
          <Header
            lang={lang}
            setLang={setLang}
            fontSize={fontSize}
            setFontSize={setFontSize}
            onGoHome={handleGoHome}
            showHomeButton={true}
            currentTab={currentTab}
            setCurrentTab={setCurrentTab}
          />

          <main className="flex-1 max-w-5xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6 animate-fade-in">
            {/* Top Back to Home link */}
            <div className="flex items-center justify-between">
              <button
                onClick={handleGoHome}
                className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900 transition-colors cursor-pointer"
              >
                <ArrowLeft className="w-4 h-4" />
                <span>{lang === 'te' ? 'హోమ్ పేజీకి వెళ్ళు' : 'Welcome Home Screen'}</span>
              </button>

              <span className="text-xs font-semibold px-3 py-1 rounded-full bg-amber-50 text-amber-900 border border-amber-200">
                {lang === 'te' ? '10వ తరగతి SSC గణితం (AP & TS)' : '10th Class SSC Mathematics (AP & TS)'}
              </span>
            </div>

            {/* TAB 1: SOLVER WORKSPACE */}
            {currentTab === 'solver' && (
              <div className="space-y-6">
                <ProblemInput
                  onSolve={handleSolve}
                  onOpenOcr={() => setIsOcrOpen(true)}
                  chapters={chapters}
                  loading={loading}
                  lang={lang}
                />

                {/* Solution Display Area */}
                <div id="solution-section">
                  {solutionData && (
                    <SolutionViewer
                      solutionData={solutionData}
                      onOpenEmailModal={() => setIsEmailModalOpen(true)}
                      lang={lang}
                    />
                  )}
                </div>

                {/* Offline Recent Solved History */}
                {recentHistory.length > 0 && !solutionData && (
                  <div className="border-t border-slate-200 pt-6 mt-6">
                    <h4 className="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-1.5 mb-3">
                      <History className="w-4 h-4 text-amber-600" />
                      <span>{lang === 'te' ? 'ఇటీవల చూసిన లెక్కలు:' : 'Recently Checked Problems:'}</span>
                    </h4>
                    <div className="flex flex-wrap gap-2">
                      {recentHistory.map((item, idx) => (
                        <button
                          key={idx}
                          onClick={() => {
                            setSolutionData(item.result);
                            setTimeout(() => {
                              const el = document.getElementById('solution-section');
                              if (el) el.scrollIntoView({ behavior: 'smooth' });
                            }, 100);
                          }}
                          className="text-xs px-3.5 py-2 rounded-xl bg-white border border-slate-200 hover:border-amber-400 text-slate-700 font-medium transition-all text-left flex items-center gap-2 cursor-pointer shadow-2xs"
                        >
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                          <span className="truncate max-w-xs">{item.query}</span>
                        </button>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* TAB 2: FORMULAS TO BYHEART (ALL 14 CHAPTERS) */}
            {currentTab === 'formulas' && (
              <FormulasView lang={lang} />
            )}

            {/* TAB 3: HOW TO PASS SSC (40+ MARKS GUARANTEE) */}
            {currentTab === 'examprep' && (
              <ExamPrepView
                lang={lang}
                onSolveQuery={(q) => {
                  setCurrentTab('solver');
                  handleSolve({ query: q });
                }}
              />
            )}

            {/* TAB 4: PAST BOARD PAPERS */}
            {currentTab === 'pastpapers' && (
              <PastPapersView lang={lang} />
            )}

            {/* TAB 5: TEACHER DASHBOARD */}
            {currentTab === 'teacher' && (
              <TeacherDashboard
                chapters={chapters}
                lang={lang}
              />
            )}
          </main>
        </>
      )}

      {/* Camera OCR Modal */}
      <CameraOcrModal
        isOpen={isOcrOpen}
        onClose={() => setIsOcrOpen(false)}
        onSolveOcr={(solvedData) => {
          if (solvedData.solutions || solvedData.explanation) {
            setSolutionData(solvedData);
          } else {
            handleSolve({ query: solvedData.query });
          }
        }}
        lang={lang}
      />

      {/* Email PDF Modal */}
      <EmailModal
        isOpen={isEmailModalOpen}
        onClose={() => setIsEmailModalOpen(false)}
        solutionData={solutionData}
        lang={lang}
      />

      {/* Clean, Simple Footer */}
      <footer className="border-t border-[#edece8] bg-[#f7f6f2] py-5 mt-auto">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <span className="font-bold text-slate-700">SSC Math Mitra • గణిత మిత్ర</span>
            <span>&bull;</span>
            <span>Telangana & AP 10th Class</span>
          </div>
          <div className="flex items-center gap-1">
            <span>Simple Step-by-Step Math Learning</span>
            <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500 inline ml-1" />
          </div>
        </div>
      </footer>
    </div>
  );
}
