import os
import sys
import json
import re
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

EM_PATH = os.path.join("knowledgesource", "10 mathematics em 2023-24.pdf")
TM_PATH = os.path.join("knowledgesource", "X Mathematics TM 2026-27.pdf")

def analyze_pdfs():
    print(f"Checking EM PDF: {os.path.exists(EM_PATH)}")
    print(f"Checking TM PDF: {os.path.exists(TM_PATH)}")
    
    reader_em = pypdf.PdfReader(EM_PATH)
    print(f"EM total pages: {len(reader_em.pages)}")
    
    # Check sample exercises in EM
    exercises_found = []
    for i in range(len(reader_em.pages)):
        text = reader_em.pages[i].extract_text() or ""
        matches = re.findall(r'Exercise\s*[-–]?\s*(\d+\.\d+)', text, re.IGNORECASE)
        for m in matches:
            exercises_found.append((m, i + 1))
    
    print(f"Total exercise instances found in EM: {len(exercises_found)}")
    print("Sample exercises:", exercises_found[:15])

if __name__ == "__main__":
    analyze_pdfs()
