import React, { useState, useEffect } from 'react';
import { BarChart3, Upload, PlusCircle, CheckCircle, TrendingUp, AlertCircle, Sparkles } from 'lucide-react';
import { fetchAnalytics, addTeacherNote, uploadTeacherPdf } from '../services/api';

export default function TeacherDashboard({ chapters = [], lang }) {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('analytics');

  const [noteChapter, setNoteChapter] = useState('Real Numbers');
  const [noteExercise, setNoteExercise] = useState('1.1');
  const [teacherName, setTeacherName] = useState('');
  const [tipText, setTipText] = useState('');
  const [noteSubmitting, setNoteSubmitting] = useState(false);
  const [noteSuccess, setNoteSuccess] = useState('');

  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadSubmitting, setUploadSubmitting] = useState(false);
  const [uploadSuccess, setUploadSuccess] = useState('');

  useEffect(() => {
    loadAnalytics();
  }, []);

  const loadAnalytics = async () => {
    setLoading(true);
    try {
      const data = await fetchAnalytics();
      setAnalytics(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const handleAddNote = async (e) => {
    e.preventDefault();
    if (!tipText.trim()) return;
    setNoteSubmitting(true);
    setNoteSuccess('');
    try {
      await addTeacherNote({
        chapter: noteChapter,
        exercise: noteExercise,
        teacherName: teacherName.trim() || 'Government School Teacher',
        tip: tipText.trim(),
      });
      setNoteSuccess('Teacher tip added successfully! It will guide students when solving this topic.');
      setTipText('');
      loadAnalytics();
    } catch (e) {
      alert('Failed to save teacher note');
    } finally {
      setNoteSubmitting(false);
    }
  };

  const handleUploadPdf = async (e) => {
    e.preventDefault();
    if (!selectedFile) return;
    setUploadSubmitting(true);
    setUploadSuccess('');
    try {
      const res = await uploadTeacherPdf(selectedFile);
      setUploadSuccess(res.message || 'PDF successfully integrated into Math Mitra knowledge base!');
      setSelectedFile(null);
    } catch (e) {
      alert('Failed to upload PDF');
    } finally {
      setUploadSubmitting(false);
    }
  };

  return (
    <div className="w-full max-w-5xl mx-auto mt-4 space-y-6 animate-fade-in">
      {/* Header Banner in Soothing Crimson/Coral Warm Gradient */}
      <div className="bg-gradient-to-r from-[#b91c1c] via-[#991b1b] to-[#7f1d1d] rounded-3xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-2xl">
          <span className="px-3 py-1 rounded-full text-xs font-bold bg-white/20 text-white backdrop-blur-md inline-block mb-3">
            {lang === 'te' ? 'ఉపాధ్యాయ & NGO డాష్‌బోర్డ్' : 'Teacher & NGO Analytics Portal'}
          </span>
          <h2 className="text-2xl sm:text-3xl font-black">
            {lang === 'te' ? 'విద్యార్థుల అభ్యసన విశ్లేషణ' : 'Student Learning & Difficulty Analytics'}
          </h2>
          <p className="text-sm text-red-100 mt-2 opacity-90">
            {lang === 'te'
              ? 'ప్రభుత్వ పాఠశాలల్లో విద్యార్థులు ఏయే లెక్కలలో ఇబ్బంది పడుతున్నారో పరిశీలించండి మరియు పరీక్ష మార్గదర్శకాలను అందించండి.'
              : 'Identify chapters where government school students struggle most, upload extra worksheets, and add custom exam tips.'}
          </p>
        </div>

        {/* Sub-tabs */}
        <div className="flex flex-wrap gap-2 mt-6 pt-4 border-t border-white/20">
          <button
            onClick={() => setActiveTab('analytics')}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'analytics'
                ? 'bg-white text-red-900 shadow-md'
                : 'bg-white/10 hover:bg-white/20 text-white'
            }`}
          >
            <BarChart3 className="w-4 h-4" />
            <span>{lang === 'te' ? 'సమస్యల నివేదిక' : 'Struggle Topics Report'}</span>
          </button>

          <button
            onClick={() => setActiveTab('add-tip')}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'add-tip'
                ? 'bg-white text-red-900 shadow-md'
                : 'bg-white/10 hover:bg-white/20 text-white'
            }`}
          >
            <PlusCircle className="w-4 h-4" />
            <span>{lang === 'te' ? 'టీచర్ చిట్కా చేర్చండి' : 'Add Custom Exam Tips'}</span>
          </button>

          <button
            onClick={() => setActiveTab('upload-pdf')}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'upload-pdf'
                ? 'bg-white text-red-900 shadow-md'
                : 'bg-white/10 hover:bg-white/20 text-white'
            }`}
          >
            <Upload className="w-4 h-4" />
            <span>{lang === 'te' ? 'కొత్త PDF అప్‌లోడ్' : 'Upload Study Materials (PDF)'}</span>
          </button>
        </div>
      </div>

      {/* Tab 1: Analytics & Topic Difficulties */}
      {activeTab === 'analytics' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="glass-card p-5 rounded-2xl border border-slate-200">
              <span className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                {lang === 'te' ? 'మొత్తం పరిష్కరించిన లెక్కలు' : 'Total Problems Solved'}
              </span>
              <p className="text-3xl font-black text-[#c01e2e] mt-2">
                {analytics?.total_queries || 48}
              </p>
              <span className="text-xs text-emerald-600 font-semibold flex items-center gap-1 mt-1">
                <TrendingUp className="w-3 h-3" />
                {lang === 'te' ? 'రోజురోజుకూ పెరుగుతోంది' : '+24% from rural schools'}
              </span>
            </div>

            <div className="glass-card p-5 rounded-2xl border border-slate-200">
              <span className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                {lang === 'te' ? 'భాషల నిష్పత్తి' : 'Language Distribution'}
              </span>
              <div className="flex items-center gap-3 mt-3">
                <div className="flex-1">
                  <div className="flex justify-between text-xs font-bold mb-1 text-slate-700">
                    <span>తెలుగు: {analytics?.queries_by_language?.te || 20}</span>
                    <span>English: {analytics?.queries_by_language?.en || 28}</span>
                  </div>
                  <div className="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden flex">
                    <div className="bg-amber-500 h-full" style={{ width: '42%' }} />
                    <div className="bg-rose-600 h-full" style={{ width: '58%' }} />
                  </div>
                </div>
              </div>
            </div>

            <div className="glass-card p-5 rounded-2xl border border-slate-200">
              <span className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                {lang === 'te' ? 'అత్యధికంగా చూసిన పద్ధతి' : 'Most Viewed Solution Tier'}
              </span>
              <p className="text-2xl font-bold text-slate-800 mt-2 flex items-center gap-2">
                <span>📘 Medium Way</span>
                <span className="text-xs px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">
                  Board Exam
                </span>
              </p>
              <p className="text-xs text-slate-500 mt-1">Students focus heavily on standard exam step marks.</p>
            </div>
          </div>

          <div className="glass-card rounded-2xl p-6 border border-slate-200">
            <h3 className="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
              <AlertCircle className="w-5 h-5 text-rose-500" />
              <span>{lang === 'te' ? 'విద్యార్థులు ఎక్కువ శ్రమపడుతున్న అంశాలు' : 'Topics Where Students Struggle Most'}</span>
            </h3>

            <div className="space-y-3">
              {analytics?.struggled_topics?.map((topic, i) => (
                <div
                  key={i}
                  className="p-4 rounded-xl border border-slate-100 bg-[#fbfbf9] flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-full bg-rose-100 text-rose-700 font-bold flex items-center justify-center text-xs">
                      #{i + 1}
                    </div>
                    <div>
                      <h4 className="font-bold text-sm text-slate-900">
                        {topic.chapter} {topic.chapter_te && `(${topic.chapter_te})`}
                      </h4>
                      <p className="text-xs text-slate-500">
                        {topic.queries} student queries logged • NGO Priority Focus
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <span
                      className={`text-xs px-3 py-1 rounded-full font-bold ${
                        topic.difficulty_rating === 'High'
                          ? 'bg-rose-100 text-rose-700 border border-rose-200'
                          : topic.difficulty_rating === 'Medium'
                          ? 'bg-amber-100 text-amber-800 border border-amber-200'
                          : 'bg-emerald-100 text-emerald-700 border border-emerald-200'
                      }`}
                    >
                      {topic.difficulty_rating} Difficulty
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {analytics?.teacher_notes && analytics.teacher_notes.length > 0 && (
            <div className="glass-card rounded-2xl p-6 border border-slate-200">
              <h3 className="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-amber-500" />
                <span>{lang === 'te' ? 'ఉపాధ్యాయుల బోర్డు పరీక్ష సూచనలు' : 'Teacher Board Exam Tips Applied in App'}</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {analytics.teacher_notes.map((note) => (
                  <div key={note.id} className="p-4 rounded-xl border border-amber-200 bg-amber-50/40 text-xs space-y-1.5">
                    <div className="flex justify-between font-bold text-amber-900">
                      <span>{note.chapter} (Ex {note.exercise})</span>
                      <span className="text-[11px] opacity-80">{note.teacher_name}</span>
                    </div>
                    <p className="text-slate-700 italic">"{note.tip}"</p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Add Custom Teacher Exam Tips */}
      {activeTab === 'add-tip' && (
        <form onSubmit={handleAddNote} className="glass-card p-6 sm:p-8 rounded-3xl border border-slate-200 space-y-4 max-w-2xl mx-auto">
          <h3 className="text-xl font-bold text-slate-900">
            {lang === 'te' ? 'విద్యార్థుల కోసం కొత్త పరీక్ష చిట్కాను జోడించండి' : 'Add Verified Teacher Tip for Students'}
          </h3>
          <p className="text-xs text-slate-500">
            {lang === 'te'
              ? 'ఈ చిట్కా విద్యార్థులు ఆ అభ్యాసాన్ని పరిష్కరించేటప్పుడు సూచనల బాక్స్‌లో కనిపిస్తుంది.'
              : 'This tip will appear directly when students solve questions from this chapter/exercise.'}
          </p>

          {noteSuccess && (
            <div className="p-3 bg-emerald-50 text-emerald-800 rounded-xl text-xs font-semibold flex items-center gap-2 border border-emerald-200">
              <CheckCircle className="w-4 h-4" />
              <span>{noteSuccess}</span>
            </div>
          )}

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">Chapter</label>
              <select
                value={noteChapter}
                onChange={(e) => setNoteChapter(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-slate-300 bg-slate-50 text-xs font-medium"
              >
                {chapters.map((ch) => (
                  <option key={ch.id} value={ch.name_en}>
                    {ch.id}. {ch.name_en} ({ch.name_te})
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">Exercise (e.g. 1.1)</label>
              <input
                type="text"
                value={noteExercise}
                onChange={(e) => setNoteExercise(e.target.value)}
                placeholder="1.1"
                className="w-full p-2.5 rounded-xl border border-slate-300 bg-slate-50 text-xs font-medium"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">Teacher Name & School</label>
            <input
              type="text"
              value={teacherName}
              onChange={(e) => setTeacherName(e.target.value)}
              placeholder="e.g. Srikanth Sir, ZPHS Warangal"
              className="w-full p-2.5 rounded-xl border border-slate-300 bg-slate-50 text-xs font-medium"
            />
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">Exam Tip / Caution / Formula Advice *</label>
            <textarea
              rows={4}
              required
              value={tipText}
              onChange={(e) => setTipText(e.target.value)}
              placeholder="e.g. In Euclid division lemma, remind students that remainder r must satisfy 0 <= r < b..."
              className="w-full p-3 rounded-xl border border-slate-300 bg-slate-50 text-xs font-medium resize-none"
            />
          </div>

          <button
            type="submit"
            disabled={noteSubmitting}
            className="w-full py-3 rounded-xl bg-[#c01e2e] hover:bg-[#a51927] text-white font-bold text-xs shadow-md transition-all cursor-pointer"
          >
            {noteSubmitting ? 'Saving Tip...' : 'Publish Teacher Tip to App'}
          </button>
        </form>
      )}

      {/* Tab 3: Upload Supplementary PDF Materials */}
      {activeTab === 'upload-pdf' && (
        <form onSubmit={handleUploadPdf} className="glass-card p-6 sm:p-8 rounded-3xl border border-slate-200 space-y-4 max-w-2xl mx-auto">
          <h3 className="text-xl font-bold text-slate-900">
            {lang === 'te' ? 'కొత్త పాఠ్యపుస్తకం లేదా నోట్స్ PDF అప్‌లోడ్ చేయండి' : 'Upload Extra Textbook Chapters / Notes'}
          </h3>
          <p className="text-xs text-slate-500">
            {lang === 'te'
              ? 'ఈ PDF లోని గణిత లెక్కలు మరియు సమాధానాలు మ్యాథ్ మిత్ర RAG ఇంజిన్‌లోకి చేర్చబడతాయి.'
              : 'Content from this PDF will be integrated into the Math Mitra local RAG retriever for student search.'}
          </p>

          {uploadSuccess && (
            <div className="p-3 bg-emerald-50 text-emerald-800 rounded-xl text-xs font-semibold flex items-center gap-2 border border-emerald-200">
              <CheckCircle className="w-4 h-4" />
              <span>{uploadSuccess}</span>
            </div>
          )}

          <div className="border-2 border-dashed border-slate-300 rounded-2xl p-8 text-center bg-slate-50">
            <Upload className="w-10 h-10 text-rose-600 mx-auto mb-3" />
            <p className="text-sm font-bold text-slate-800 mb-1">Select or drop your SSC Math PDF here</p>
            <p className="text-xs text-slate-500 mb-4">Accepts .pdf files up to 50MB</p>
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setSelectedFile(e.target.files[0])}
              className="block mx-auto text-xs text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-red-50 file:text-red-700 hover:file:bg-red-100"
            />
          </div>

          <button
            type="submit"
            disabled={uploadSubmitting || !selectedFile}
            className="w-full py-3 rounded-xl bg-[#c01e2e] hover:bg-[#a51927] text-white font-bold text-xs shadow-md disabled:opacity-50 transition-all cursor-pointer"
          >
            {uploadSubmitting ? 'Processing & Indexing PDF...' : 'Ingest into Knowledge Source'}
          </button>
        </form>
      )}
    </div>
  );
}
