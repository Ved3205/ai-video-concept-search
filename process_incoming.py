import numpy as np
import requests
import joblib
from sklearn.metrics.pairwise import cosine_similarity
# from read_chunks import create_embedding

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

df = joblib.load("embeddings.joblib")

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