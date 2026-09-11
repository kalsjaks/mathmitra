import React, { useState, useRef, useEffect } from 'react';
import { Camera, Upload, X, Check, RefreshCw, Sparkles, Image as ImageIcon } from 'lucide-react';
import { processOcr } from '../services/api';

export default function CameraOcrModal({ isOpen, onClose, onSolveOcr, lang }) {
  const [cameraActive, setCameraActive] = useState(false);
  const [capturedImage, setCapturedImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [ocrError, setOcrError] = useState('');
  const videoRef = useRef(null);
  const streamRef = useRef(null);

  // Sample photos for instant camera test in classroom
  const sampleProblems = [
    { title: 'Quadratic Equation (x² + 5x + 6 = 0)', query: 'Find the roots of quadratic equation: x^2 + 5x + 6 = 0' },
    { title: 'SSC Ex 1.1 Euclid HCF (900, 270)', query: 'Exercise 1.1: Use Euclid division algorithm to find the HCF of 900 and 270' },
    { title: 'Trig Identity (sin²θ + cos²θ = 1)', query: 'Prove that sin^2 theta + cos^2 theta = 1' },
  ];

  useEffect(() => {
    if (isOpen) {
      startCamera();
    } else {
      stopCamera();
      setCapturedImage(null);
      setOcrError('');
    }
    return () => stopCamera();
  }, [isOpen]);

  const startCamera = async () => {
    setOcrError('');
    try {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: { facingMode: 'environment', width: { ideal: 1280 }, height: { ideal: 720 } }
        });
        streamRef.current = stream;
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
          setCameraActive(true);
        }
      } else {
        setOcrError('Camera access not supported on this device/browser.');
      }
    } catch (err) {
      console.warn('Camera access denied or unavailable:', err);
      setOcrError('Camera access not allowed or unavailable. You can upload a photo or choose a sample below.');
      setCameraActive(false);
    }
  };

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach(track => track.stop());
      streamRef.current = null;
    }
    setCameraActive(false);
  };

  const capturePhoto = () => {
    if (!videoRef.current) return;
    const canvas = document.createElement('canvas');
    canvas.width = videoRef.current.videoWidth || 640;
    canvas.height = videoRef.current.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg');
    setCapturedImage(dataUrl);
    stopCamera();
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      setCapturedImage(reader.result);
      stopCamera();
    };
    reader.readAsDataURL(file);
  };

  const handleSolveExtracted = async (customQuery) => {
    setLoading(true);
    setOcrError('');
    try {
      if (customQuery) {
        onSolveOcr({ query: customQuery, exercise: null, page: null });
        onClose();
        return;
      }
      // Call backend OCR API
      const res = await processOcr(null, capturedImage);
      if (res && res.solution) {
        onSolveOcr(res.solution);
        onClose();
      } else {
        throw new Error('Could not recognize mathematical equation.');
      }
    } catch (err) {
      console.error(err);
      setOcrError('Could not process photo OCR. Please check clarity or pick a sample problem.');
    } finally {
      setLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm animate-fade-in">
      <div className="bg-white dark:bg-slate-900 rounded-3xl max-w-xl w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 relative max-h-[90vh] overflow-y-auto">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Title */}
        <div className="flex items-center gap-3 mb-4">
          <div className="w-10 h-10 rounded-xl bg-teal-500/10 text-teal-600 flex items-center justify-center">
            <Camera className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-slate-900 dark:text-white">
              {lang === 'te' ? 'కెమెరా మ్యాథ్ సాల్వర్ (OCR)' : 'Camera Math Solver (OCR)'}
            </h3>
            <p className="text-xs text-slate-500">
              {lang === 'te' ? 'మీ పాఠ్యపుస్తక లెక్క ఫోటో తీయండి' : 'Point camera at your textbook problem'}
            </p>
          </div>
        </div>

        {/* Camera Viewport / Captured Preview */}
        <div className="relative rounded-2xl overflow-hidden bg-slate-950 aspect-video flex items-center justify-center border-2 border-dashed border-slate-300 dark:border-slate-700 mb-4">
          {capturedImage ? (
            <img src={capturedImage} alt="Captured Math Problem" className="w-full h-full object-contain" />
          ) : cameraActive ? (
            <>
              <video ref={videoRef} autoPlay playsInline className="w-full h-full object-cover" />
              {/* Equation alignment overlay frame */}
              <div className="absolute inset-8 border-2 border-emerald-400/80 rounded-xl pointer-events-none flex flex-col justify-between p-2 shadow-inner">
                <span className="text-[10px] font-bold bg-emerald-500 text-white px-2 py-0.5 rounded self-start">
                  {lang === 'te' ? 'లెక్కను ఈ ఫ్రేమ్‌లో ఉంచండి' : 'Align Math Problem Here'}
                </span>
              </div>
            </>
          ) : (
            <div className="text-center p-6 text-slate-400">
              <Camera className="w-12 h-12 mx-auto mb-2 opacity-40" />
              <p className="text-sm font-medium">{ocrError || 'Camera preview unavailable.'}</p>
            </div>
          )}
        </div>

        {/* Actions Bar */}
        <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
          {capturedImage ? (
            <>
              <button
                onClick={() => {
                  setCapturedImage(null);
                  startCamera();
                }}
                className="flex items-center gap-1.5 px-4 py-2 rounded-xl border border-slate-300 text-slate-700 dark:text-slate-300 text-xs font-bold hover:bg-slate-100 transition-all"
              >
                <RefreshCw className="w-3.5 h-3.5" />
                <span>{lang === 'te' ? 'మళ్ళీ తీయండి' : 'Retake'}</span>
              </button>

              <button
                onClick={() => handleSolveExtracted()}
                disabled={loading}
                className="flex items-center gap-2 px-6 py-2 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 text-white font-bold text-xs shadow-md transition-all ml-auto"
              >
                {loading ? (
                  <span>{lang === 'te' ? 'గుర్తిస్తున్నాం...' : 'Recognizing Math...'}</span>
                ) : (
                  <>
                    <Check className="w-4 h-4" />
                    <span>{lang === 'te' ? 'లెక్కను సాధించండి' : 'Extract & Solve'}</span>
                  </>
                )}
              </button>
            </>
          ) : (
            <>
              {cameraActive && (
                <button
                  onClick={capturePhoto}
                  className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md transition-all"
                >
                  <Camera className="w-4 h-4" />
                  <span>{lang === 'te' ? 'ఫోటో తీయండి' : 'Snap Photo'}</span>
                </button>
              )}

              {/* Upload Image Option */}
              <label className="flex items-center gap-2 px-4 py-2 rounded-xl border border-indigo-200 bg-indigo-50/50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold cursor-pointer hover:bg-indigo-100 transition-all ml-auto">
                <Upload className="w-3.5 h-3.5" />
                <span>{lang === 'te' ? 'గ్యాలరీ నుండి అప్‌లోడ్' : 'Upload Image'}</span>
                <input type="file" accept="image/*" onChange={handleFileUpload} className="hidden" />
              </label>
            </>
          )}
        </div>

        {/* Quick Simulated Photo Samples */}
        <div className="border-t border-slate-100 dark:border-slate-800 pt-3">
          <p className="text-xs font-bold text-slate-500 mb-2 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-amber-500" />
            {lang === 'te' ? 'లేదా పరీక్ష కోసం శాంపిల్ లెక్కను ఎంచుకోండి:' : 'Or test instantly with textbook samples:'}
          </p>
          <div className="space-y-1.5">
            {sampleProblems.map((sample, idx) => (
              <button
                key={idx}
                onClick={() => handleSolveExtracted(sample.query)}
                className="w-full text-left p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-teal-400 hover:bg-teal-50/30 dark:hover:bg-slate-800 text-xs font-medium text-slate-700 dark:text-slate-300 transition-all flex items-center justify-between"
              >
                <span>{sample.title}</span>
                <span className="text-[11px] text-teal-600 font-bold">{lang === 'te' ? 'సాధించు' : 'Solve'} &rarr;</span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
