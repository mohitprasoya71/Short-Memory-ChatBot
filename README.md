# 🤖 Short Memory Chatbot

A conversational AI chatbot built with **Streamlit** and **LangChain** that maintains short-term memory across messages.

## 🚀 Live Demo

👉 [**Try it here → short-memory-chatbot.onrender.com**](https://short-memory-chatbot.onrender.com)

## 🛠️ Tech Stack

- **Frontend** — Streamlit
- **Backend** — Python, LangChain,LangGraph
- **AI Model** — Google Gemini API
- **Deployment** — Render

## 📁 Project Structure

```
Short-Memory-Chatbot/
├── backend.py              # Chatbot logic & LangChain setup
├── streamlit_frontend.py   # Streamlit UI
├── .env.example            # Environment variable template
├── requirements.txt        # Python dependencies
└── README.md
```

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/Short-Memory-Chatbot.git
cd Short-Memory-Chatbot

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your GOOGLE_API_KEY in .env

# 5. Run the app
streamlit run streamlit_frontend.py
```

## 🔑 Environment Variables

Create a `.env` file based on `.env.example`:

```
GOOGLE_API_KEY=your_api_key_here
```

## 📄 License

MIT License
