# Speech to Text
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import whisper
import json
model = whisper.load_model("medium")
result = model.transcribe(audio="audios\\8_Functions_in_Java_Practice_Questions_.mp3",language="hi",task="translate",word_timestamps=False)
# print(result["segments"])
# chunks = []
# for segment in result["segments"]:
#     chunks.append({
#         "id": segment["id"],
#         "start": segment["start"],
#         "end": segment["end"],
#         "text": segment["text"]
#     })

chunks = []
for segment in result["segments"]:
    chunks.append({
        "number": "8",
        "title": "8_Functions_in_Java_Practice_Questions_",
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })
chunks_with_metadata = {
    "chunks": chunks,
    "text": result["text"]
}

# print(chunks)
with open("8_Functions_in_Java_Practice_Questions_.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)