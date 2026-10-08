# 🎙️ MeetQuery: AI-Powered Meeting Knowledge Retrieval

<p align="center">
  <img src="docs/AI-Meeting Platform.png" alt="AI Meeting Intelligence Platform Architecture" width="100%">
</p>

<p align="center">
  <strong>A Generative AI and Retrieval-Augmented Generation (RAG) system for searching and understanding meeting video content.</strong>
</p>

---

## 📌 Project Title

**MeetQuery: AI-Powered Meeting Knowledge Retrieval**

---

## 👥 Team Members

| Name                | Enrollment Number    |
| ------------------- | -------------------- |
| Vednarayan Hiralkar | BT23F05F028          |
| Aryan Shastri       | BT23F05F028          |


---

# 1. Problem Statement

Meeting recordings contain valuable information such as technical discussions, explanations, decisions, and important points. However, finding a particular piece of information in a long recording requires manually watching or searching through the entire video.

For example, if a user wants to know:

> "Where was Java inheritance discussed?"

they would normally have to watch the recording or manually search through its transcript.

The project addresses this problem by converting meeting videos into searchable textual knowledge and allowing users to ask questions using natural language.

---

# 2. Objectives

The main objectives of this project are:

* Process meeting/video recordings automatically.
* Extract audio from video files.
* Convert speech into text using a Speech-to-Text model.
* Store the generated transcripts in a structured format.
* Divide transcripts into smaller searchable chunks.
* Generate semantic embeddings for transcript content.
* Perform semantic retrieval based on user queries.
* Use Retrieval-Augmented Generation (RAG) to generate answers from retrieved content.
* Demonstrate the practical use of Generative AI for video/meeting knowledge retrieval.
* Explore the complete workflow of a small Generative AI application.

---

# 3. Proposed Solution

The proposed system converts video recordings into a searchable knowledge base.

Instead of directly searching the video itself, the system first converts spoken content into text.

The overall process is:

```text
Video Files
     ↓
Audio Extraction
     ↓
Speech-to-Text
     ↓
Transcript
     ↓
Transcript Chunking
     ↓
Text Embeddings
     ↓
Semantic Retrieval
     ↓
Relevant Context
     ↓
RAG
     ↓
Generated Answer
```

The system was tested using a collection of **10 video recordings**.

The videos were processed individually and their transcript information was used for semantic search and question answering.

---

# 4. Technologies Used

| Technology               | Purpose                                |
| ------------------------ | -------------------------------------- |
| Python                   | Main programming language              |
| FFmpeg                   | Audio extraction from video            |
| Faster-Whisper / Whisper | Speech-to-Text transcription           |
| BGE-M3                   | Text embedding generation              |
| Ollama                   | Local Large Language Model execution   |
| JSON                     | Transcript and structured data storage |
| RAG                      | Retrieval-Augmented Generation         |
| Semantic Search          | Finding relevant transcript content    |

---

# 5. System Workflow

## Step 1 — Video Collection

A dataset of **10 video recordings** was collected for testing the system.

These videos serve as the source knowledge for the application.

```text
Video 1
Video 2
Video 3
...
Video 10
```

---

## Step 2 — Audio Extraction

The audio stream is extracted from each video using **FFmpeg**.

```text
Video
  ↓
FFmpeg
  ↓
Audio
```

This allows the speech recognition model to process the spoken content independently from the video.

---

## Step 3 — Speech-to-Text

The extracted audio is processed using **Whisper / Faster-Whisper**.

The model converts the spoken content into text while retaining timing information.

Example:

```json
{
  "start": 125.4,
  "end": 131.8,
  "text": "Today we will discuss object oriented programming."
}
```

The resulting transcript provides the textual representation of the video.

---

## Step 4 — Transcript Generation

The transcription output is stored in structured JSON format.

The transcript contains information such as:

* Text
* Start time
* End time
* Segment information

This structured representation allows the transcript to be processed programmatically.

---

## Step 5 — Transcript Chunking

Long transcripts are divided into smaller chunks.

For example:

```text
Complete Transcript
        ↓
 ┌───────────────┐
 │    Chunk 1    │
 ├───────────────┤
 │    Chunk 2    │
 ├───────────────┤
 │    Chunk 3    │
 ├───────────────┤
 │      ...      │
 └───────────────┘
```

Chunking makes it possible to retrieve only the portions of the transcript that are relevant to a particular question.

---

# 6. Embedding Generation

Each transcript chunk is converted into a numerical vector representation using **BGE-M3**.

The purpose of embeddings is to represent the semantic meaning of text numerically.

For example:

```text
"What is inheritance in Java?"
```

and

```text
"Java allows a class to inherit properties and methods from another class."
```

may have similar semantic representations even though the exact words are different.

This allows the system to perform **semantic search rather than simple keyword matching**.

---

# 7. Semantic Retrieval

When the user enters a question, the question is converted into an embedding using the same embedding model.

The system then compares the query representation with the available transcript chunks and retrieves the most relevant content.

```text
User Question
      ↓
Query Embedding
      ↓
Semantic Similarity
      ↓
Relevant Transcript Chunks
```

This allows the system to identify relevant information even when the question does not contain the exact words spoken in the video.

---

# 8. Retrieval-Augmented Generation (RAG)

The retrieved transcript content is used as context for the Large Language Model.

The RAG process is:

```text
                 User Question
                       ↓
                Query Embedding
                       ↓
               Semantic Retrieval
                       ↓
             Relevant Transcript
                    Chunks
                       ↓
              Context Construction
                       ↓
              Large Language Model
                       ↓
                Generated Answer
```

Instead of asking the LLM to answer only from its pretrained knowledge, relevant information from the processed videos is provided as context.

This allows the generated response to be grounded in the available video content.

---

# 9. Generative AI Component

The project uses Generative AI primarily during the **RAG question-answering stage**.

The LLM receives:

1. The user's question.
2. Relevant transcript content retrieved from the processed videos.

It then generates a natural-language response.

Therefore, the project demonstrates the practical use of:

* Large Language Models
* Prompt Engineering
* Text Embeddings
* Semantic Search
* Retrieval-Augmented Generation

---

# 10. Project Architecture

```text
                         ┌──────────────────┐
                         │   Video Dataset  │
                         │   10 Videos      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      FFmpeg      │
                         │  Audio Extraction│
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Whisper /        │
                         │ Faster-Whisper   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Transcript    │
                         │      JSON        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Chunking      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     BGE-M3       │
                         │    Embeddings    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Semantic Search  │
                         └────────┬─────────┘
                                  │
                                  │
                       ┌──────────▼──────────┐
                       │    User Question   │
                       └──────────┬──────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Relevant Context │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │       RAG        │
                         │                  │
                         │  Local LLM       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Generated Answer │
                         └──────────────────┘
```

---

# 11. Implementation

The implementation is organized into multiple stages.

### Video Processing

Video files are processed to extract their audio streams.

### Transcription

Audio is passed through the Whisper-based Speech-to-Text model to generate transcript segments.

### Transcript Processing

The generated transcript is converted into structured JSON data.

### Chunk Generation

Transcript content is divided into smaller chunks for retrieval.

### Embedding Generation

BGE-M3 generates vector representations of the transcript chunks.

### Retrieval

A user's natural-language query is converted into an embedding and compared against the available transcript representations.

The most relevant content is selected as context.

### RAG Question Answering

The retrieved content is provided to the local LLM through a RAG prompt.

The LLM generates a response based on the retrieved transcript information.

---

# 12. Experimental Dataset

For the current implementation, **10 video recordings were collected and processed**.

The videos were used to create the searchable knowledge base.

The processing workflow was applied to the videos as follows:

```text
10 Videos
    ↓
Audio Extraction
    ↓
Transcription
    ↓
JSON Transcripts
    ↓
Chunk Generation
    ↓
Embeddings
    ↓
Searchable Knowledge
```

The dataset is used only for demonstrating and testing the system.

---

# 13. Results / Output

The implemented system successfully demonstrates the following workflow:

* Video files can be processed.
* Audio can be extracted from videos.
* Speech can be converted into text.
* Transcripts can be stored as structured JSON.
* Transcript content can be divided into chunks.
* Embeddings can be generated from transcript chunks.
* User queries can be matched with semantically relevant transcript content.
* Retrieved transcript content can be supplied to an LLM.
* The LLM can generate answers based on the retrieved context.

### Example

**User Query**

```text
Where was inheritance discussed?
```

### Retrieval

```text
User Query
     ↓
Embedding
     ↓
Semantic Search
     ↓
Relevant Transcript Chunk
```

### Generation

```text
Relevant Transcript
        +
User Question
        ↓
       LLM
        ↓
Generated Answer
```

The system therefore allows users to interact with information contained in the video dataset using natural language.

---

# 14. Screenshots

Project screenshots are available in:

```text
Screenshots/
```

The screenshots can demonstrate:

* Video processing
* Generated transcript
* JSON transcript structure
* Chunk generation
* Embedding/search process
* User query
* Retrieved context
* Generated RAG response

---

# 15. Project Structure

The project submission follows the prescribed structure:

```text
AI-Meeting-Intelligence/
│
├── README.md
│
├── PPT/
│   └── Project-Presentation.pptx
│
├── Source-Code/
│   └── [Project Source Code]
│
├── Screenshots/
│   └── [Project Screenshots]
│
└── Demo/
    └── [Demo Files / Links]
```

The source code contains the implementation of the video processing, transcription, chunking, embedding, retrieval, prompting, and RAG components.

---

# 16. Working Demonstration

The project has been tested using a collection of 10 video recordings.

The working demonstration shows the complete pipeline:

```text
Video
  ↓
Audio
  ↓
Transcript
  ↓
Chunks
  ↓
Embeddings
  ↓
Semantic Retrieval
  ↓
Relevant Context
  ↓
RAG
  ↓
Answer
```

The demonstration can be performed locally using the provided source code and required models/dependencies.

### Demo Link

**Demo / Deployment:** Not deployed. Local demonstration is used for the current implementation.

---

# 17. Limitations

The current implementation focuses on demonstrating the core Generative AI and RAG workflow.

Current limitations include:

* The system is evaluated on a limited collection of 10 videos.
* The current implementation focuses primarily on transcript-based retrieval.
* Speaker diarization is not currently part of the implemented pipeline.
* Retrieval quality depends on transcript quality and chunking.
* The system does not currently provide a full production web interface.
* Large-scale distributed processing is outside the current project scope.
* The system is designed primarily as a practical prototype rather than a production deployment.

---

# 18. Future Scope

The project can be extended with:

* Speaker diarization
* Speaker-aware retrieval
* Improved chunking strategies
* Better retrieval and reranking
* Timestamp-based answer citations
* Source transcript display
* Meeting summarization
* Automatic action-item extraction
* Decision extraction
* Topic detection
* Search across multiple meetings
* Web-based interface
* Meeting history
* User authentication
* Cloud deployment

These features represent possible future improvements and are not claimed as part of the current implementation.

---

# 19. References

The project uses and builds upon the following technologies and research areas:

### Models and Tools

* **Whisper / Faster-Whisper** — Speech-to-text transcription
* **BGE-M3** — Text embedding model
* **Ollama** — Local execution of Large Language Models
* **FFmpeg** — Audio/video processing

### Concepts

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Text Embeddings
* Large Language Models
* Prompt Engineering
* Speech-to-Text

### Research / Documentation

Relevant research papers and official documentation used during implementation should be listed here with their respective links and citations.

---

# 20. Learning Outcomes

This project provided practical experience in:

* Generative AI application development
* Retrieval-Augmented Generation
* Large Language Models
* Prompt Engineering
* Text Embeddings
* Semantic Search
* Speech-to-Text
* Transcript Processing
* Vector representations
* AI pipeline design
* Local AI model deployment
* Python-based AI development

---

# 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Conclusion

The **AI Meeting Intelligence Platform** demonstrates a practical application of Generative AI by transforming video recordings into searchable textual knowledge.

By combining **Speech-to-Text, transcript processing, semantic embeddings, semantic retrieval, and Retrieval-Augmented Generation**, the system allows users to ask natural-language questions about information contained within a collection of meeting/video recordings.

The project focuses on a small, functional and demonstrable Generative AI solution suitable for practical academic learning and experimentation.
