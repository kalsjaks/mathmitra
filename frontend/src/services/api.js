const API_BASE = '/api';

export async function fetchChapters() {
  try {
    const res = await fetch(`${API_BASE}/chapters`);
    if (!res.ok) throw new Error('Failed to fetch chapters');
    const data = await res.json();
    localStorage.setItem('math_mitra_chapters_cache', JSON.stringify(data));
    return data;
  } catch (err) {
    const cached = localStorage.getItem('math_mitra_chapters_cache');
    if (cached) return JSON.parse(cached);
    throw err;
  }
}

export async function solveProblem({ query, exercise, page, language = 'auto', action_type = 'solve' }) {
  try {
    const res = await fetch(`${API_BASE}/solve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, exercise, page: page ? parseInt(page) : null, language, action_type }),
    });
    if (!res.ok) throw new Error('Could not solve problem');
    const data = await res.json();
    
    // Save to local solved history for offline browsing
    const history = JSON.parse(localStorage.getItem('math_mitra_history') || '[]');
    history.unshift({ query: query || `Exercise ${exercise}`, result: data, timestamp: Date.now() });
    localStorage.setItem('math_mitra_history', JSON.stringify(history.slice(0, 30)));
    
    return data;
  } catch (err) {
    console.warn('Network error, attempting offline cache lookup:', err);
    const history = JSON.parse(localStorage.getItem('math_mitra_history') || '[]');
    const match = history.find(h => h.query.toLowerCase().includes((query || '').toLowerCase()));
    if (match) {
      return { ...match.result, offlineCached: true };
    }
    throw err;
  }
}

export async function processOcr(file, base64) {
  const formData = new FormData();
  if (file) {
    formData.append('file', file);
  }
  if (base64) {
    formData.append('image_base64', base64);
  }
  const res = await fetch(`${API_BASE}/ocr`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error('OCR process failed');
  return await res.json();
}

export async function sendEmail({ email, query, solutionData, studentName }) {
  const res = await fetch(`${API_BASE}/email`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email,
      query,
      solution_data: solutionData,
      student_name: studentName,
    }),
  });
  if (!res.ok) throw new Error('Failed to send email');
  return await res.json();
}

export async function fetchAnalytics() {
  const res = await fetch(`${API_BASE}/analytics`);
  if (!res.ok) throw new Error('Failed to load analytics');
  return await res.json();
}

export async function addTeacherNote({ chapter, exercise, teacherName, tip }) {
  const res = await fetch(`${API_BASE}/teacher/note`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chapter,
      exercise,
      teacher_name: teacherName,
      tip,
    }),
  });
  if (!res.ok) throw new Error('Failed to add teacher note');
  return await res.json();
}

export async function uploadTeacherPdf(file) {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${API_BASE}/teacher/upload`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error('Failed to upload PDF');
  return await res.json();
}

export async function fetchQuestionPreview(exercise, question = 1) {
  try {
    const res = await fetch(`${API_BASE}/exercise-question?exercise=${encodeURIComponent(exercise)}&question=${question}`);
    if (!res.ok) return null;
    return await res.json();
  } catch (err) {
    console.warn('Error fetching question preview:', err);
    return null;
  }
}

export async function fetchFormulas() {
  try {
    const res = await fetch(`${API_BASE}/formulas`);
    if (!res.ok) throw new Error('Failed to fetch formulas');
    return await res.json();
  } catch (err) {
    console.error('Error fetching formulas:', err);
    throw err;
  }
}

export async function fetchExamPrep() {
  try {
    const res = await fetch(`${API_BASE}/exam-prep`);
    if (!res.ok) throw new Error('Failed to fetch exam prep');
    return await res.json();
  } catch (err) {
    console.error('Error fetching exam prep:', err);
    throw err;
  }
}

export async function fetchPastPapers() {
  try {
    const res = await fetch(`${API_BASE}/past-papers`);
    if (!res.ok) throw new Error('Failed to fetch past papers');
    return await res.json();
  } catch (err) {
    console.error('Error fetching past papers:', err);
    throw err;
  }
}
