# 🐞 AI Bug Report Analyzer (LangGraph + Google Gemini)

An enterprise-grade, multi-agent AI assistant that automatically analyzes raw natural language bug descriptions and transforms them into structured, actionable engineering bug reports using **LangGraph**, **Google Gemini**, **FastAPI**, and a modern **Tailwind CSS Glassmorphism Dashboard**.

---

## 📸 Dashboard Preview

> *Enterprise UI showing live LangGraph node-state tracking and structured root-cause investigation outputs.*

![AI Bug Report Analyzer Enterprise Dashboard](Asset/AI%20Bug%20Report%20Analyzer%20Enterprise%20Dashboard_2.png)

---

## 🚀 Architectural Workflow (LangGraph Pipeline)

The core backend orchestrates state deterministically across sequential specialized AI nodes:

```text
User Input (Raw Description)
        │
        ▼
🔍 Node 1: Bug Analysis & Extraction (Extracts title, affected feature & summary)
        │
        ▼
🚨 Node 2: Severity Classification (Classifies as Critical, High, Medium, or Low)
        │
        ▼
🛠️ Node 3: Root Cause Suggestion (Architectural diagnosis & code investigation points)
        │
        ▼
📄 Node 4: Report Formatting (Generates clean markdown/structured payload)
        │
        ▼
🏁 END – Structured Dashboard Output
```

---

## ✨ Key Features

* **Multi-Agent State Orchestration:** Built with `LangGraph` StateGraphs for robust state transitions.
* **Structured Output Parsing:** Enforces strict Pydantic schemas combined with Google Gemini's generative capabilities.
* **Modern SaaS UI:** Custom Tailwind CSS dark-mode glassmorphism dashboard with real-time node animation.
* **Developer Productivity Tools:** Includes one-click sample loaders, clipboard copying, and direct PDF report printing.

---

## 📂 Project Structure

```text
ai-bug-analyzer/
├── Asset/
│   └── AI Bug Report Analyzer Enterprise Dashboard_2.png
├── venv/
├── .env
├── .gitignore
├── graph.py
├── index.html
├── main.py
├── nodes.py
├── requirements.txt
├── server.py
└── state.py
```

---

## 🛠️ Tech Stack

* **AI Orchestration:** LangGraph, LangChain Google GenAI
* **LLM Engine:** Google Gemini (Gemini Flash)
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla)
* **Environment Management:** Python-Dotenv

---

## ⚙️ Getting Started & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-bug-analyzer-langgraph.git
cd ai-bug-analyzer
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API Key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### 5. Run the Application
Start the FastAPI server via Uvicorn:
```bash
python -m uvicorn server:app --reload
```

Open your browser and navigate to: **`http://127.0.0.1:8000`**

---
