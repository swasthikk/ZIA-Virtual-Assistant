# Zia AI Assistant 🤖

**Zia** is a voice-controlled AI assistant built in Python. It can perform tasks like opening websites, playing music, fetching news, and answering queries using OpenAI GPT-3.5-turbo.

---

## 🚀 Features

- **Wake word detection** – Activate Zia by saying `zia`.
- **Web browsing** – Open sites like Google, YouTube, Facebook, LinkedIn.
- **Music playback** – Play songs from YouTube.
- **News headlines** – Fetch top news using NewsAPI.
- **AI responses** – Get answers to general questions via OpenAI GPT.
- **Text-to-Speech** – Uses gTTS + pygame for spoken responses.
- **Ambient noise adjustment** – Recognizes speech in noisy environments.

---

## 🛠️ Requirements

- Python 3.10+ (tested on Python 3.13)
- Packages:

```bash
pip install speechrecognition pyttsx3 gtts pygame requests openai pyaudio
