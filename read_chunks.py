import json
import os
import re
import time
import traceback

import requests


OLLAMA_URL = "http://localhost:11434/api/embed"
OLLAMA_MODEL = "bge-m3"
MAX_CHUNKS = 10


def log(message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}", flush=True)

def create_embedding(text):
    request_started = time.perf_counter()
    log(f"Sending embedding request to {OLLAMA_URL} using model={OLLAMA_MODEL}; text_length={len(text)}")
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "input": text,
        },
        timeout=60,
    )
    request_elapsed = time.perf_counter() - request_started
    log(f"Embedding HTTP response received in {request_elapsed:.3f}s; status_code={response.status_code}")
    response.raise_for_status()

    parse_started = time.perf_counter()
    payload = response.json()
    parse_elapsed = time.perf_counter() - parse_started
    log(f"Embedding JSON parsed in {parse_elapsed:.3f}s; keys={list(payload.keys())}")

    embeddings = payload.get("embeddings")
    if not embeddings:
        raise KeyError(f"Missing 'embeddings' in Ollama response: {payload}")

    embedding = embeddings[0]
    log(f"Received embedding vector with {len(embedding)} dimensions")
    return embedding

# print(create_embedding("cat sat on the mat"))
def main():
    overall_started = time.perf_counter()

    try:
        log("Listing JSON files in jsons/")
        list_started = time.perf_counter()
        jsons = os.listdir("jsons")
        list_elapsed = time.perf_counter() - list_started
        log(f"os.listdir completed in {list_elapsed:.3f}s; found {len(jsons)} files")

        jsons = [name for name in jsons if re.match(r"^(\d+)", name)]
        jsons.sort(key=lambda name: int(re.match(r"(\d+)", name).group(1)))
        log(f"Sorted JSON files: {jsons}")

        my_dicts = []
        chunk_id = 0

        for json_file in jsons:
            file_path = os.path.join("jsons", json_file)
            log(f"Opening JSON file: {file_path}")
            load_started = time.perf_counter()
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
            load_elapsed = time.perf_counter() - load_started
            log(f"Loaded {json_file} in {load_elapsed:.3f}s; chunks_in_file={len(content)}")

            for chunk_index, chunk in enumerate(content, start=1):
                if chunk_id >= MAX_CHUNKS:
                    log(f"Reached MAX_CHUNKS={MAX_CHUNKS}; stopping early for test run")
                    break

                try:
                    text = chunk.get("text", "")
                    log(
                        f"Processing chunk_id={chunk_id} file={json_file} chunk_index={chunk_index} text_length={len(text)}"
                    )
                    embedding_started = time.perf_counter()
                    embedding = create_embedding(text)
                    embedding_elapsed = time.perf_counter() - embedding_started

                    chunk["chunk_id"] = chunk_id
                    chunk["embedding"] = embedding
                    my_dicts.append(chunk)
                    chunk_id += 1

                    log(
                        f"Chunk processed in {embedding_elapsed:.3f}s; total_chunks={len(my_dicts)}; embedding_preview={embedding[:5]}"
                    )
                except Exception:
                    log(f"Failed while processing chunk_id={chunk_id} in {json_file}")
                    traceback.print_exc()
                    raise

            if chunk_id >= MAX_CHUNKS:
                break

        summary_started = time.perf_counter()
        log(f"Preparing compact summary for {len(my_dicts)} processed chunks")
        summary = [
            {
                "chunk_id": item["chunk_id"],
                "title": item.get("title"),
                "start": item.get("start"),
                "end": item.get("end"),
                "text_preview": item.get("text", "")[:80],
                "embedding_dimensions": len(item.get("embedding", [])),
            }
            for item in my_dicts
        ]
        summary_elapsed = time.perf_counter() - summary_started
        log(f"Summary prepared in {summary_elapsed:.3f}s")
        print(json.dumps(summary, indent=2), flush=True)

    except Exception:
        log("Fatal error in read_chunks.py")
        traceback.print_exc()
        raise
    finally:
        overall_elapsed = time.perf_counter() - overall_started
        log(f"Total runtime: {overall_elapsed:.3f}s")


if __name__ == "__main__":
    main()