import React, { useState, useEffect } from 'react';
import { FileText, Download, ExternalLink, Calendar, Award, CheckCircle, Sparkles } from 'lucide-react';
import { fetchPastPapers } from '../services/api';

export default function PastPapersView({ lang = 'en' }) {
  const [papersData, setPapersData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPapers();
  }, []);

  const loadPapers = async () => {
    setLoading(true);
    try {
      const data = await fetchPastPapers();
      if (data && data.papers) {
        setPapersData(data.papers);
      }
    } catch (e) {
      console.error('Failed to load past papers', e);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="text-center py-16 text-slate-500">
        <div className="inline-block w-8 h-8 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mb-3"></div>
        <p className="text-xs font-bold">{lang === 'te' ? 'పాత ప్రశ్నాపత్రాలు లోడ్ అవుతున్నాయి...' : 'Loading Past Board Exam Papers...'}</p>
      </div>
    );
  }

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Top Banner */}
      <div className="bg-gradient-to-r from-indigo-700 via-blue-800 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-2xl space-y-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/20 text-indigo-100 backdrop-blur-md">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>{lang === 'te' ? 'SSC బోర్డు పరీక్ష పత్రాలు (AP & TS)' : 'Previous SSC Board Papers (AP & TS)'}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            {lang === 'te' ? 'గత సంవత్సరాల ప్రశ్నాపత్రాలు & మోడల్ పేపర్లు' : 'Official Previous Question Papers & Blueprints'}
          </h2>
          <p className="text-xs sm:text-sm text-indigo-100/90 leading-relaxed font-medium">
            {lang === 'te'
              ? 'తెలంగాణ మరియు ఆంధ్రప్రదేశ్ 10వ తరగతి గత 5 సంవత్సరాల అసలైన ప్రశ్నాపత్రాలు, సమాధానాలు మరియు మార్కింగ్ స్కీమ్‌లు.'
              : 'Download and practice official AP and Telangana SSC board examination question papers with chapter weightage.'}
          </p>
        </div>
      </div>

      {/* List of Papers */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        {papersData.map((paper, idx) => {
          const links = paper.download_links && paper.download_links.length > 0
            ? paper.download_links
            : (paper.download_url ? [{ label: 'View Question Paper', url: paper.download_url, type: 'Portal' }] : []);

          const title = paper.title || `${paper.state} SSC Mathematics ${paper.year}`;

          return (
            <div
              key={idx}
              className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between space-y-4"
            >
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-800 border border-indigo-200">
                    {paper.state || 'AP & TS SSC'} • {paper.year}
                  </span>
                  <span className="text-xs font-bold text-slate-500 flex items-center gap-1">
                    <Calendar className="w-3.5 h-3.5 text-indigo-600" />
                    {paper.month || paper.exam_type || 'Annual Examination'}
                  </span>
                </div>

                <h3 className="text-sm sm:text-base font-bold text-slate-800 leading-snug">
                  {title}
                </h3>

                <p className="text-xs text-slate-600 leading-relaxed">
                  {paper.description || 'Full 80-mark SSC Board paper with Part A & Part B.'}
                </p>

                {paper.mediums && (
                  <div className="flex flex-wrap gap-1.5 pt-1">
                    {paper.mediums.map((med, mIdx) => (
                      <span key={mIdx} className="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-slate-100 text-slate-700">
                        {med}
                      </span>
                    ))}
                  </div>
                )}

                {paper.key_topics && (
                  <div className="pt-2 border-t border-slate-100 text-[11px] text-slate-500">
                    <span className="font-semibold text-slate-700">
                      {lang === 'te' ? 'ముఖ్య అంశాలు: ' : 'Key Focus Areas: '}
                    </span>
                    <span>{paper.key_topics}</span>
                  </div>
                )}
              </div>

              {/* Download / Resource Links */}
              <div className="space-y-2 pt-3 border-t border-slate-100">
                <div className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                  {lang === 'te' ? 'అధికారిక పేపర్లు & సొల్యూషన్స్' : 'Official Papers & Solutions'}
                </div>
                <div className="flex flex-col gap-2">
                  {links.map((lnk, lIdx) => (
                    <a
                      key={lIdx}
                      href={lnk.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-full py-2.5 px-3.5 rounded-xl bg-indigo-50 hover:bg-indigo-600 text-indigo-700 hover:text-white text-xs font-bold border border-indigo-200 hover:border-indigo-600 transition-all flex items-center justify-between group cursor-pointer shadow-2xs"
                    >
                      <div className="flex items-center gap-2">
                        <FileText className="w-3.5 h-3.5 text-indigo-500 group-hover:text-white" />
                        <span className="text-left font-medium">{lnk.label}</span>
                      </div>
                      <ExternalLink className="w-3.5 h-3.5 text-indigo-400 group-hover:text-white shrink-0 ml-1" />
                    </a>
                  ))}
                  {links.length === 0 && (
                    <a
                      href="https://bse.telangana.gov.in/"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-full py-2 px-3 rounded-xl bg-indigo-50 hover:bg-indigo-600 text-indigo-700 hover:text-white text-xs font-bold border border-indigo-200 hover:border-indigo-600 transition-all flex items-center justify-between"
                    >
                      <span>{lang === 'te' ? 'బోర్డు అధికారిక పోర్టల్' : 'Visit BSE Official Portal'}</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </a>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
