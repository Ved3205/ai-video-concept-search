import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        },
        timeout=120
    )

    r.raise_for_status()

    return r.json()["embeddings"]


jsons = sorted(
    os.listdir("jsons"),
    key=lambda x: int(x.split("_")[0])
)

my_dicts = []
chunk_id = 0

for json_file in jsons:

    with open(
        os.path.join("jsons", json_file),
        "r",
        encoding="utf-8"
    ) as f:
        content = json.load(f)

    print(f"Creating embeddings for {json_file}")

    embeddings = create_embedding(
        [chunk["text"] for chunk in content]
    )

    for i, chunk in enumerate(content):

        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]

        my_dicts.append(chunk)

        chunk_id += 1

df = pd.DataFrame.from_records(my_dicts)

print(f"\nLoaded {len(df)} chunks")

while True:

    incoming_query = input("\nAsk a Question (or type exit): ")

    if incoming_query.lower() == "exit":
        break

    question_embedding = create_embedding(
        [incoming_query]
    )[0]

    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [question_embedding]
    ).flatten()

    top_results = 3

    max_index = similarities.argsort()[::-1][:top_results]

    new_df = df.iloc[max_index]

    print("\nTop Matching Chunks:\n")

    for rank, (_, row) in enumerate(new_df.iterrows(), start=1):

        print(f"Rank #{rank}")
        print(f"Similarity : {similarities[row.name]:.4f}")
        print(f"Title      : {row['title']}")
        print(f"Number     : {row['number']}")
        print(f"Start      : {row['start']}")
        print(f"End        : {row['end']}")
        print(f"Text       : {row['text']}")
        print("-" * 100)