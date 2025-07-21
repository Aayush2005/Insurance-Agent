# 🛡️ Insurance Voice Agent (Hackathon Edition)

![Last Commit](https://img.shields.io/github/last-commit/Aayush2005/Insurance-Agent?style=flat-square)
![Tech Stack](https://img.shields.io/badge/Mistral%207B-Ollama-blueviolet?style=flat-square)
![License](https://img.shields.io/github/license/Aayush2005/Insurance-Agent?style=flat-square)

A fully local, privacy-first **voice-based AI assistant** for handling insurance queries.  
Powered by ✨ Retrieval-Augmented Generation (RAG), real-time voice, and a warm human-like tone.

---

## 🚀 Features

- 🎙️ **Voice Interaction** (STT + TTS)
- 💬 **Intent Classification** (Mistral 7B via Ollama)
- 📚 **RAG-based Contextual Answers**
- 🧠 **Personalization** via user policy data
- 🔍 Real-world performance: Low latency, high accuracy

---

## 🛠️ Tech Stack

| Component           | Tech                             |
|--------------------|----------------------------------|
| **LLM**            | [Mistral 7B](https://mistral.ai) via [Ollama](https://ollama.com) |
| **STT**            | [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)       |
| **TTS**            | [TTS Coqui](https://github.com/coqui-ai/TTS) / [pyttsx3](https://github.com/nateshmbhat/pyttsx3) |                      |
| **RAG**            | FAISS + Sentence Transformers (`all-MiniLM-L6-v2`)               |
| **User DB**        | [TinyDB](https://tinydb.readthedocs.io/en/latest/) (no SQL!)     |

---

## 🧩 Project Structure

```
backend/
├── main.py                      
├── intent_classifier.py         # Intent classification using Mistral
├── response_generator.py        # Context-based reply generation
├── rag_pipeline.py              # FAISS retrieval based on intent
├── user_data_handler.py         # User info extraction from policy numbers
├── prompts/
│   ├── intent_classifier_prompt.txt
│   ├── response_with_context.txt
│   └── response_without_context.txt
├── vector_db/
│   ├── build_index.py
│   ├── faiss_index/
│   └── metadata.pkl
docs/
└── data/                        # Intent-tagged .txt files for indexing
```

---

## 🗣️ Demo Flow

```
Voice Input 🎙️ → STT (Whisper) → Intent Classification 🧠 →
Retrieve Static + User Context 📚 → Mistral 7B → TTS 🎧 → Response
```

---

## 💡 Example Query

> "**I want to surrender my policy P123456**"

→ Extracts policy number → Classifies intent (`surrender_policy`)  
→ RAG retrieves context → Mistral crafts empathetic reply  
→ TTS reads out the answer

---

## 📦 How to Run

**Make sure you are in backend directory**

1. 🔁 Pull Ollama + Mistral:
   ```bash
   ollama pull mistral
   ```

2. 📚 Index knowledge base:
   ```bash
   python vector_db/build_index.py
   ```

3. 🚀 Start the backend:
   ```bash
   python main.py
   ```


---

## 🧠 Hackathon Judging Criteria Mapped

| Criteria             | How We Achieved It                        |
|----------------------|-------------------------------------------|
| **⚡ Latency**         | Lightweight STT + Tiny RAG + Ollama local |
| **✅ Accuracy**        | RAG + user personalization                |
| **🫶 Empathy**         | Structured LLM prompt w/ emotional tone   |
| **💥 Interruption**     | STT handles mid-sentence or fragment      |

---

## 👨‍💻 Authors & Contributors

| Name     | Role                 |
|----------|----------------------|
| Aayush Kumar Singh | Backend & AI Logic 🧠 |
| Shreyanshu Raj | STT + TTS 🎙️ |
| Harshvardhan | STT + TTS |

---

## 🧾 License

MIT © Aayush Kumar Singh

---

## 🌟 Final Thought

> A voice agent isn’t just about answers —  
> it’s about clarity, care, and speed.  
> Yours delivers all three. 🧠⚡🫶
