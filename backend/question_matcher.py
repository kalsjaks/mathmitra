# -*- coding: utf-8 -*-
"""
Question Matcher Module for Math Mitra (10th SSC AP & TS)
Performs intelligent fuzzy, keyword, and semantic matching of pasted student queries
against the official 10th Class SCERT Mathematics textbook exercises and questions.
Allows users to copy-paste ANY question directly from their book or exam paper
without needing to select the exercise dropdown.
"""

import re
import json
import os
from typing import Optional, Tuple, Dict, Any

INDEX_PATH = os.path.join(os.path.dirname(__file__), "data", "textbook_index.json")
TM_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "telugu_textbook_questions.json")

# Precompiled stop words to ignore during matching
STOP_WORDS = {
    "use", "using", "algorithm", "to", "show", "that", "any", "is", "of", "the", "form",
    "where", "some", "integer", "find", "determine", "evaluate", "prove", "check", "whether",
    "write", "following", "given", "for", "each", "and", "or", "in", "by", "from", "with",
    "క్రింది", "ఆధారంగా", "కనుగొనండి", "చూపండి", "అని", "ఒక", "యొక్క", "మరియు", "లేదా", "రూపంలో"
}

def clean_tokens(text: str) -> set:
    """Extract significant alphaneumeric math tokens from query."""
    if not text:
        return set()
    # Normalize powers, spacing, and numbers with variables (e.g. 6 q -> 6q)
    text = re.sub(r'(\d+)\s+([a-zA-Z])', r'\1\2', text)
    tokens = set(re.findall(r'[a-zA-Z0-9\u0c00-\u0c7f]+', text.lower()))
    return tokens - STOP_WORDS

def match_textbook_question(query: str) -> Optional[Tuple[str, int, str]]:
    """
    Matches an arbitrary pasted question string to an SSC textbook (exercise, question_num, language).
    Returns (exercise_str, question_num, lang) or None.
    """
    if not query or len(query.strip()) < 8:
        return None

    clean_q = query.strip()
    norm_q = clean_q.lower()
    # Normalize "6 q" -> "6q", "3 p" -> "3p", "9 m" -> "9m"
    norm_q = re.sub(r'(\d+)\s+([a-zA-Z])', r'\1\2', norm_q)

    # 1. DIRECT CURATED PATTERN RULES (Instant high-confidence matches)
    # Exercise 1.1 Q2: 6q + 1, 6q + 3, 6q + 5
    if ("6q" in norm_q or "6 q" in query) and ("odd" in norm_q or "బేసి" in query or "division algorithm" in norm_q or "భాగహార విశేషవిధి" in query or "6q + 1" in norm_q or "6q+1" in norm_q):
        return ("1.1", 2, "te" if "బేసి" in query else "en")

    # Exercise 1.1 Q3: square of positive integer is 3p or 3p + 1
    if ("3p" in norm_q or "3 p" in query) and ("square" in norm_q or "వర్గం" in query or "positive integer" in norm_q or "పూర్ణ సంఖ్య" in query):
        return ("1.1", 3, "te" if "వర్గం" in query else "en")

    # Exercise 1.1 Q4: cube of positive integer is 9m, 9m + 1, 9m + 8
    if ("9m" in norm_q or "9 m" in query) and ("cube" in norm_q or "ఘనం" in query or "positive integer" in norm_q or "పూర్ణ సంఖ్య" in query):
        return ("1.1", 4, "te" if "ఘనం" in query else "en")

    # Exercise 1.1 Q5: n, n + 2 or n + 4 is divisible by 3
    if ("n + 2" in norm_q or "n+2" in norm_q) and ("3" in norm_q or "divisible" in norm_q or "భాగింపబడుతుంది" in query):
        return ("1.1", 5, "te" if "భాగింపబడుతుంది" in query else "en")

    # Exercise 1.1 Q1: Euclid HCF of (900 & 270) or (196 & 38220) or (1651 & 2032)
    if ("900" in norm_q and "270" in norm_q) or ("196" in norm_q and "38220" in norm_q) or ("1651" in norm_q and "2032" in norm_q):
        return ("1.1", 1, "te" if "గ.సా.భా" in query else "en")

    # Exercise 1.2 Q1: prime factors 140, 156, 3825, 5005, 7429
    if any(num in norm_q for num in ["140", "156", "3825", "5005", "7429"]) and ("prime" in norm_q or "కారణాంక" in query or "factor" in norm_q):
        return ("1.2", 1, "te" if "కారణాంక" in query else "en")

    # Exercise 1.2 Q3: 6^n can end with digit 0
    if ("6^n" in norm_q or "6 ^ n" in norm_q or "6n" in norm_q) and ("0" in norm_q or "zero" in norm_q or "సున్నా" in query):
        return ("1.2", 3, "te" if "సున్నా" in query else "en")

    # Exercise 1.3 Q1: Prove that √5 is irrational
    if ("√5" in query or "sqrt(5)" in norm_q or "root 5" in norm_q or "√2" in query or "√3" in query) and ("irrational" in norm_q or "కరణీయ" in query):
        if "3" in query and "+" in query:
            return ("1.3", 2, "te" if "కరణీయ" in query else "en")
        return ("1.3", 1, "te" if "కరణీయ" in query else "en")

    # Exercise 1.4: Terminating decimal expansion
    if ("terminating" in norm_q or "అంతమయ్యే" in query) and any(frac in norm_q for frac in ["13/3125", "11/12", "64/455", "15/1600", "3125", "1600"]):
        return ("1.4", 1, "te" if "అంతమయ్యే" in query else "en")

    # Exercise 1.5: Logarithms log2 512, log5 1/625, 2 log 3 + 3 log 5 - 5 log 2
    if "log" in norm_q or "సంవర్గమాన" in query:
        if any(w in norm_q for w in ["512", "625", "243", "0.001", "log2", "log5", "log10", "single logarithm"]):
            return ("1.5", 1, "te" if "సంవర్గమాన" in query else "en")

    # Exercise 3.3 Q1: zeroes of x^2 - 2x - 8 or 4s^2 - 4s + 1
    if ("x^2 - 2x - 8" in norm_q or "4s^2 - 4s + 1" in norm_q or "6x^2 - 3 - 7x" in norm_q) and ("zero" in norm_q or "శూన్య" in query):
        return ("3.3", 1, "te" if "శూన్య" in query else "en")

    # Exercise 5.2 Q1: roots of x^2 - 3x - 10 = 0
    if ("x^2 - 3x - 10" in norm_q or "2x^2 + x - 6" in norm_q) and ("roots" in norm_q or "మూలాలు" in query or "factorisation" in norm_q):
        return ("5.2", 1, "te" if "మూలాలు" in query else "en")

    # Exercise 6.2: 10th term of AP: 2, 7, 12 or 30th term of AP: 10, 7, 4
    if ("2, 7, 12" in norm_q or "10, 7, 4" in norm_q or "ap: 2, 7" in norm_q) and ("term" in norm_q or "పదం" in query):
        return ("6.2", 2, "te" if "పదం" in query else "en")

    # Exercise 7.1: distance between (2, 3) and (4, 1)
    if "(2, 3)" in query and "(4, 1)" in query:
        return ("7.1", 1, "te" if "దూరం" in query else "en")

    # Exercise 8.1: Thales theorem / Basic Proportionality Theorem
    if "thales" in norm_q or "basic proportionality" in norm_q or "తేల్స్" in query or "సరూప" in query:
        return ("8.1", 1, "te" if "తేల్స్" in query else "en")

    # Exercise 9.1: Tangents from external point
    if ("tangent" in norm_q or "స్పర్శరేఖ" in query) and ("circle" in norm_q or "వృత్త" in query or "external" in norm_q):
        return ("9.1", 1, "te" if "స్పర్శరేఖ" in query else "en")

    # Exercise 11.4: sin^2 theta + cos^2 theta = 1 or (sin A + cosec A)^2
    if ("sin^2" in norm_q or "cos^2" in norm_q or "tan^2" in norm_q or "cosec" in norm_q) and ("prove" in norm_q or "నిరూపించండి" in query or "identity" in norm_q):
        return ("11.4", 1, "te" if "నిరూపించండి" in query else "en")

    # 2. TOKEN-BASED JACCARD MATCHING AGAINST ALL CURATED QUESTIONS
    q_tokens = clean_tokens(query)
    if not q_tokens:
        return None

    # Try matching against study_material curated
    try:
        from backend.study_material import get_curated_exercise_question
        for ex_id in ["1.1", "1.2", "1.3", "1.4", "1.5", "2.1", "2.2", "3.1", "3.2", "3.3", "5.1", "5.2", "6.1", "6.2", "7.1", "11.1", "14.1"]:
            for q_idx in range(1, 6):
                cand = get_curated_exercise_question(ex_id, q_idx)
                if not cand or "Solve the textbook problem" in cand:
                    continue
                c_tokens = clean_tokens(cand)
                if not c_tokens:
                    continue
                intersection = q_tokens.intersection(c_tokens)
                overlap = len(intersection) / max(len(c_tokens), 1)
                if overlap >= 0.50 and len(intersection) >= 3:
                    return (ex_id, q_idx, "en")
    except Exception:
        pass

    # Try matching against Telugu textbook JSON
    if os.path.exists(TM_DATA_PATH):
        try:
            with open(TM_DATA_PATH, "r", encoding="utf-8") as f:
                tm_data = json.load(f)
            for ex_id, ex_info in tm_data.get("exercises", {}).items():
                for q_num_str, q_obj in ex_info.get("questions", {}).items():
                    tm_text = q_obj.get("text", "")
                    c_tokens = clean_tokens(tm_text)
                    if not c_tokens:
                        continue
                    intersection = q_tokens.intersection(c_tokens)
                    overlap = len(intersection) / max(len(c_tokens), 1)
                    if overlap >= 0.45 and len(intersection) >= 2:
                        return (ex_id, int(q_num_str), "te")
        except Exception:
            pass

    return None
