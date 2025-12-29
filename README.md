# YouTube Transcript Summarizer — Streamlit + Gemini

**Project type:** NLP · Summarization · Web app  
**Role:** Junior Data Analyst / Developer  
**Tech:** Python · Streamlit · youtube-transcript-api · google-generative-ai (Gemini) · python-dotenv

---

## 🚀 Project Overview
A simple Streamlit app that accepts a YouTube link, fetches the video transcript, and uses the Gemini model to create a concise summary and key takeaways. Ideal for quickly extracting knowledge from long videos.

---

## ✨ Features
- Input: YouTube URL or video ID
- Transcript fetching (via `youtube-transcript-api` or fallback)
- Transcript preprocessing + chunking for long videos
- Summarization using Gemini with prompt-engineered outputs
- Streamlit UI with summary preview, download, and copy options

---

## 🧭 Repo structure (suggested)
/app.py

/requirements.txt

/.env.example

/README.md

/utils/transcript_utils.py

/utils/gemini_client.py

/assets/demo.gif

---

# 📌 Usage & UX expectations

Paste YouTube URL → click Summarize

App shows progress: fetching transcript → chunking → summarizing

Final output: 2–3 sentence summary, 5 bullet takeaways

Buttons: Download summary (.txt), Copy to clipboard, Regenerate (shorter/longer)


# ⚠️ Edge cases

No transcript available: show friendly message and possible fixes (enable captions, try another video)

API errors / rate limits: show clear error message and instruct to check API key or retry later

Long transcripts: chunk before calling Gemini and then aggregate chunk summaries



# ✅ Future improvements

Add caching for transcripts + results

Add retry/backoff for Gemini calls

Add speaker diarization or timestamps

Multi-language support and highlights view

