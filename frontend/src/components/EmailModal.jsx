import React, { useState } from 'react';
import { Mail, X, CheckCircle, Send, Sparkles } from 'lucide-react';
import { sendEmail } from '../services/api';

export default function EmailModal({ isOpen, onClose, solutionData, lang }) {
  const [email, setEmail] = useState('');
  const [studentName, setStudentName] = useState('');
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  if (!isOpen || !solutionData) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email || !email.includes('@')) {
      setErrorMsg(lang === 'te' ? 'సరైన ఈమెయిల్ చిరునామా నమోదు చేయండి' : 'Please enter a valid email address');
      return;
    }

    setLoading(true);
    setErrorMsg('');
    try {
      const res = await sendEmail({
        email: email.trim(),
        query: solutionData.query,
        solutionData,
        studentName: studentName.trim() || 'Student'
      });
      setSuccessMsg(res.message || 'PDF solution sent successfully to your Gmail!');
    } catch (err) {
      setErrorMsg(lang === 'te' ? 'ఈమెయిల్ పంపడంలో సమస్య ఎదురైంది.' : 'Could not send email. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm animate-fade-in">
      <div className="bg-white dark:bg-slate-900 rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 relative">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 rounded-full hover:bg-slate-100 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {successMsg ? (
          <div className="text-center py-6 space-y-4">
            <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto">
              <CheckCircle className="w-8 h-8" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 dark:text-white">
              {lang === 'te' ? 'ఈమెయిల్ పంపబడింది! 🎉' : 'PDF Sent Successfully! 🎉'}
            </h3>
            <p className="text-sm text-slate-600 dark:text-slate-300">
              {successMsg}
            </p>
            <button
              onClick={() => {
                setSuccessMsg('');
                onClose();
              }}
              className="px-6 py-2.5 rounded-xl bg-indigo-600 text-white font-bold text-sm hover:bg-indigo-700 transition-colors cursor-pointer"
            >
              {lang === 'te' ? 'ముగించు' : 'Close'}
            </button>
          </div>
        ) : (
          <div>
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 flex items-center justify-center">
                <Mail className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                  {lang === 'te' ? 'మీ ఈమెయిల్‌కు సొల్యూషన్ PDF పంపండి' : 'Email Solution PDF to Gmail'}
                </h3>
                <p className="text-xs text-slate-500">
                  {lang === 'te' ? 'పూర్తి 3 లెవల్స్ సాధన మీ ఇన్‌బాక్స్‌కు వస్తుంది' : 'Receive all 3 solution tiers directly in your inbox'}
                </p>
              </div>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                  {lang === 'te' ? 'విద్యార్థి పేరు (ఐచ్ఛికం)' : 'Student Name (Optional)'}
                </label>
                <input
                  type="text"
                  value={studentName}
                  onChange={(e) => setStudentName(e.target.value)}
                  placeholder="e.g. Ramesh"
                  className="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                  {lang === 'te' ? 'మీ Gmail ID *' : 'Your Gmail ID *'}
                </label>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="student@gmail.com"
                  className="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              {errorMsg && (
                <p className="text-xs text-rose-500 font-medium">{errorMsg}</p>
              )}

              <button
                type="submit"
                disabled={loading}
                className="w-full flex items-center justify-center gap-2 py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 text-white font-bold text-sm shadow-md transition-all cursor-pointer"
              >
                {loading ? (
                  <span>{lang === 'te' ? 'పంపుతున్నాం...' : 'Sending PDF...'}</span>
                ) : (
                  <>
                    <Send className="w-4 h-4" />
                    <span>{lang === 'te' ? 'ఇప్పుడే PDF పంపు' : 'Send Solution PDF'}</span>
                  </>
                )}
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
}
