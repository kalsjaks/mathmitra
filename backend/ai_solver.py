# -*- coding: utf-8 -*-
"""
AI Solver Module for Math Mitra (10th SSC AP & TS)
Integrates Google Gemini Flash API using standard library (urllib.request)
to solve any arbitrary or unlisted mathematics problem with SSC board pedagogical rubric.
Gracefully falls back to local deterministic solver if API key is not configured.
"""

import os
import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any

def get_gemini_api_key() -> Optional[str]:
    """Retrieve Gemini API key from environment or local .env file."""
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if key and key.strip():
        return key.strip()

    # Search common .env locations
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        os.path.join(base_dir, ".env"),
        os.path.join(os.path.dirname(__file__), ".env")
    ]
    for env_path in candidates:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("#") or not line:
                            continue
                        if line.startswith("GEMINI_API_KEY="):
                            val = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if val:
                                return val
                        elif line.startswith("GOOGLE_API_KEY="):
                            val = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if val:
                                return val
            except Exception:
                pass
    return None

def solve_with_gemini(query: str, lang: str = "auto", custom_api_key: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Calls Google Gemini REST API to solve an unlisted or general math problem.
    Returns structured Math Mitra response or None if API key unavailable / call fails.
    """
    api_key = custom_api_key or get_gemini_api_key()
    if not api_key:
        return None

    # Determine desired language
    is_te = lang == "te" or any('\u0c00' <= char <= '\u0c7f' for char in query)
    target_lang_instruction = (
        "Explain primarily in clear, student-friendly Telugu (తెలుగు) with standard English mathematical terms and formulas in KaTeX."
        if is_te else
        "Explain in clear, student-friendly English with standard KaTeX formulas ($...$ for inline, $$...$$ for block)."
    )

    system_instruction = f"""You are Math Mitra (గణిత మిత్ర), an expert SSC 10th Class Board Mathematics Master Teacher & State Evaluator for Telangana (TS) and Andhra Pradesh (AP) SCERT curriculum.

A student or teacher has pasted a mathematics problem:
"{query}"

Your task is to provide an exemplary, high-scoring, step-by-step textbook solution that teaches and explains the concept clearly to 10th class students.

Guidelines:
1. {target_lang_instruction}
2. Format your entire solution in clean Markdown with KaTeX math syntax:
   - Inline math: $formula$
   - Display equations: $$formula$$
3. Strictly structure your explanation into these exact sections:
   ### 🧮 Question
   **[Full question statement]**

   ---

   ### ✏️ Solution & Step-by-Step Method

   **Step 1: Given Information & Identifying Formula**
   • Write clearly what is given in the question with symbols and units.
   • State the exact SSC 10th Class formula or theorem applicable (e.g. Euclid's Division Lemma, Quadratic Formula, Distance Formula, etc.).

   **Step 2: Systematic Step-by-Step Calculation**
   • Substitute the values into the formula.
   • Show every single intermediate arithmetic step clearly so students never get confused.

   **Step 3: Verification & Key Mathematical Concepts**
   • Explain the reasoning, verify why the solution is correct, or explain alternate method if applicable.

   ---

   ### ✅ Final Answer:
   [Boxed or bold final answer with units]

   ---

   ### 💡 SSC 10th Board Exam Tip & Marks Rubric:
   • Mention how marks are awarded in SSC Board exams (Formula: 1 Mark, Steps: 2 Marks, Final Answer: 1 Mark).
   • Common mistake to avoid during exams.

Do not output JSON or conversational prelude. Output only the markdown solution.
"""

    models_to_try = [
        "gemini-2.5-flash",
        "gemini-1.5-flash",
        "gemini-2.0-flash",
        "gemini-pro"
    ]

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [{"text": system_instruction}]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 2500
            }
        }
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                if response.status == 200:
                    res_body = json.loads(response.read().decode("utf-8"))
                    candidates = res_body.get("candidates", [])
                    if candidates and "content" in candidates[0]:
                        parts = candidates[0]["content"].get("parts", [])
                        if parts and "text" in parts[0]:
                            generated_text = parts[0]["text"]
                            
                            # Deduce chapter from query / text
                            chapter_id = 1
                            chapter_en = "SSC Mathematics"
                            chapter_te = "గణిత శాస్త్రం"
                            q_l = (query + " " + generated_text).lower()
                            if any(k in q_l for k in ["euclid", "real number", "hcf", "lcm", "irrational", "logarithm", "వాస్తవ"]):
                                chapter_id, chapter_en, chapter_te = 1, "Real Numbers", "వాస్తవ సంఖ్యలు"
                            elif any(k in q_l for k in ["set", "subset", "union", "intersection", "సమితి"]):
                                chapter_id, chapter_en, chapter_te = 2, "Sets", "సమితులు"
                            elif any(k in q_l for k in ["polynomial", "zeroes", "బహుపది"]):
                                chapter_id, chapter_en, chapter_te = 3, "Polynomials", "బహుపదులు"
                            elif any(k in q_l for k in ["linear", "two variable", "రెండు చరరాశులు"]):
                                chapter_id, chapter_en, chapter_te = 4, "Pair of Linear Equations", "రెండు చరరాశులలో రేఖీయ సమీకరణాలు"
                            elif any(k in q_l for k in ["quadratic", "roots", "discriminant", "వర్గ సమీకరణ"]):
                                chapter_id, chapter_en, chapter_te = 5, "Quadratic Equations", "వర్గ సమీకరణాలు"
                            elif any(k in q_l for k in ["progression", "arithmetic progression", "ap", "gp", "శ్రేఢి"]):
                                chapter_id, chapter_en, chapter_te = 6, "Progressions", "శ్రేఢులు"
                            elif any(k in q_l for k in ["coordinate", "distance", "midpoint", "collinear", "నిరూపక"]):
                                chapter_id, chapter_en, chapter_te = 7, "Coordinate Geometry", "నిరూపక రేఖాగణితం"
                            elif any(k in q_l for k in ["triangle", "thales", "similar", "సరూప"]):
                                chapter_id, chapter_en, chapter_te = 8, "Similar Triangles", "సరూప త్రిభుజాలు"
                            elif any(k in q_l for k in ["tangent", "secant", "circle", "స్పర్శరేఖ"]):
                                chapter_id, chapter_en, chapter_te = 9, "Tangents and Secants to a Circle", "స్పర్శరేఖలు మరియు ఛేదనరేఖలు"
                            elif any(k in q_l for k in ["mensuration", "cylinder", "cone", "sphere", "hemisphere", "volume", "surface area", "క్షేత్రమితి"]):
                                chapter_id, chapter_en, chapter_te = 10, "Mensuration", "క్షేత్రమితి"
                            elif any(k in q_l for k in ["trigonometry", "sin", "cos", "tan", "sec", "cosec", "cot", "త్రికోణమితి"]):
                                chapter_id, chapter_en, chapter_te = 11, "Trigonometry", "త్రికోణమితి"
                            elif any(k in q_l for k in ["height", "distance", "elevation", "depression", "tower", "టవర్", "ఎత్తు"]):
                                chapter_id, chapter_en, chapter_te = 12, "Applications of Trigonometry", "త్రికోణమితి అనువర్తనాలు"
                            elif any(k in q_l for k in ["probability", "dice", "coin", "card", "సంభావ్యత"]):
                                chapter_id, chapter_en, chapter_te = 13, "Probability", "సంభావ్యత"
                            elif any(k in q_l for k in ["statistics", "mean", "median", "mode", "సాంఖ్యకశాస్త్రం"]):
                                chapter_id, chapter_en, chapter_te = 14, "Statistics", "సాంఖ్యకశాస్త్రం"

                            return {
                                "query": query,
                                "language": "te" if is_te else "en",
                                "chapter_id": chapter_id,
                                "chapter_en": chapter_en,
                                "chapter_te": chapter_te,
                                "page_reference": "Board Problem Practice",
                                "exercise_reference": "Custom / Unlisted SSC Problem (AI Solved)",
                                "formulas": ["SSC 10th Board Standard Formula"],
                                "explanation": {
                                    "en": generated_text,
                                    "te": generated_text
                                }
                            }
        except Exception:
            continue

    return None
