import json

transcript_path = r"C:\Users\Sreenivas\.gemini\antigravity-ide\brain\96409fa4-beae-47af-b5cc-cd3936e1d2c4\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            print("USER_INPUT:", data.get("content"))
