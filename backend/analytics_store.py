import os
import json
import time

if os.environ.get("VERCEL"):
    ANALYTICS_FILE = "/tmp/analytics.json"
else:
    ANALYTICS_FILE = os.path.join(os.path.dirname(__file__), "data", "analytics.json")

def init_analytics():
    if not os.path.exists(ANALYTICS_FILE):
        default_data = {
            "total_queries": 48,
            "queries_by_language": {
                "en": 28,
                "te": 20
            },
            "struggled_topics": [
                {"chapter": "Quadratic Equations", "chapter_te": "వర్గ సమీకరణాలు", "queries": 18, "difficulty_rating": "High"},
                {"chapter": "Real Numbers", "chapter_te": "వాస్తవ సంఖ్యలు", "queries": 14, "difficulty_rating": "Medium"},
                {"chapter": "Trigonometry", "chapter_te": "త్రికోణమితి", "queries": 12, "difficulty_rating": "High"},
                {"chapter": "Similar Triangles", "chapter_te": "సరూప త్రిభుజాలు", "queries": 9, "difficulty_rating": "High"},
                {"chapter": "Coordinate Geometry", "chapter_te": "నిరూపక రేఖాగణితం", "queries": 8, "difficulty_rating": "Medium"},
                {"chapter": "Progressions", "chapter_te": "శ్రేఢులు", "queries": 7, "difficulty_rating": "Low"}
            ],
            "solution_views": {
                "easy": 35,
                "medium": 42,
                "advanced": 19
            },
            "recent_queries": [
                {"query": "Exercise 1.1 Question 1 HCF of 900 and 270", "timestamp": time.time() - 3600, "lang": "en"},
                {"query": "యూక్లిడ్ భాగహార న్యాయం ద్వారా గ.సా.భా", "timestamp": time.time() - 1800, "lang": "te"},
                {"query": "Find roots of x^2 + 5x + 6 = 0", "timestamp": time.time() - 900, "lang": "en"}
            ],
            "teacher_notes": [
                {
                    "id": "tn-1",
                    "chapter": "Real Numbers",
                    "exercise": "1.1",
                    "teacher_name": "Smt. Sarada (Zilla Parishad High School)",
                    "tip": "Remind students that remainder r must always be strictly less than divisor b (0 <= r < b). Often students forget this in 2-mark questions!"
                },
                {
                    "id": "tn-2",
                    "chapter": "Quadratic Equations",
                    "exercise": "5.2",
                    "teacher_name": "Sri. K. Ramesh (Govt Boys High School)",
                    "tip": "When calculating discriminant b^2 - 4ac, pay special attention to minus signs when c is negative (e.g., -4 * 1 * -6 = +24)."
                }
            ]
        }
        os.makedirs(os.path.dirname(ANALYTICS_FILE), exist_ok=True)
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)

init_analytics()

def get_analytics():
    init_analytics()
    try:
        with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def log_query(query: str, chapter_name: str, lang: str):
    try:
        data = get_analytics()
        data["total_queries"] = data.get("total_queries", 0) + 1
        
        # Language counts
        qlang = data.setdefault("queries_by_language", {"en": 0, "te": 0})
        qlang[lang] = qlang.get(lang, 0) + 1
        
        # Recent queries
        recent = data.setdefault("recent_queries", [])
        recent.insert(0, {"query": query, "timestamp": time.time(), "lang": lang})
        data["recent_queries"] = recent[:20]
        
        # Update topic counter
        topics = data.setdefault("struggled_topics", [])
        found = False
        for t in topics:
            if t["chapter"].lower() == chapter_name.lower():
                t["queries"] += 1
                found = True
                break
        if not found:
            topics.append({"chapter": chapter_name, "queries": 1, "difficulty_rating": "Medium"})
            
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error logging analytics: {e}")

def add_teacher_note(chapter: str, exercise: str, teacher_name: str, tip: str):
    try:
        data = get_analytics()
        notes = data.setdefault("teacher_notes", [])
        new_note = {
            "id": f"tn-{len(notes)+1}",
            "chapter": chapter,
            "exercise": exercise,
            "teacher_name": teacher_name,
            "tip": tip
        }
        notes.insert(0, new_note)
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return new_note
    except Exception as e:
        print(f"Error adding teacher note: {e}")
        return None
