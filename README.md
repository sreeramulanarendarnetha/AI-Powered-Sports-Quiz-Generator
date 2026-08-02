# 🏆 AI-Powered Sports Quiz Generator

An intelligent **Retrieval-Augmented Generation (RAG)** application that generates sports quizzes using both a **local vector database (ChromaDB)** and **live web search (DuckDuckGo)**. The application uses an LLM (OpenAI or Google Gemini) to create factually grounded multiple-choice quizzes through an interactive **Streamlit** interface.

---

## 📌 Features

* 🎯 Generate quizzes for multiple sports
* 📚 Retrieve historical sports facts from ChromaDB
* 🌐 Fetch recent sports news using DuckDuckGo Search
* 🤖 Generate AI-powered quizzes using OpenAI or Gemini
* ✅ Display answers and explanations
* 💾 Persistent local vector database
* 🖥️ Interactive Streamlit web application

---

## 🏗️ Project Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
          Quiz Generation Agent
          ┌────────┴────────┐
          ▼                 ▼
     ChromaDB          DuckDuckGo Search
 (Historical Facts)    (Latest Sports News)
          └────────┬────────┘
                   ▼
            Context Combination
                   ▼
          OpenAI / Gemini LLM
                   ▼
      Multiple Choice Quiz Output
```

---

## 📁 Project Structure

```
sports-quiz-agent/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── data/
│   └── sports_facts.json
│
├── chroma_db/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── search.py
│   └── generator.py
│
└── app.py
```

---

## ⚙️ Technologies Used

* Python 3.9 – 3.11
* Streamlit
* ChromaDB
* DuckDuckGo Search
* OpenAI API (or Google Gemini)
* Sentence Transformers
* Python Dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sports-quiz-agent.git

cd sports-quiz-agent
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

For OpenAI:

```env
OPENAI_API_KEY=your_openai_api_key
```

Or for Gemini:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your API keys to GitHub.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📚 How It Works

### Step 1 – User Input

The user selects:

* Sport
* Difficulty Level

---

### Step 2 – Historical Retrieval

The application searches ChromaDB for relevant historical sports facts.

Example:

```
Football history
World Cup records
Historic achievements
```

---

### Step 3 – Live Web Search

DuckDuckGo retrieves recent:

* Tournament results
* Championship winners
* Match updates
* Sports news

---

### Step 4 – Context Merging

Historical information and live news are merged into a single context block.

---

### Step 5 – AI Quiz Generation

The LLM generates:

* 3–5 Multiple Choice Questions
* Four answer options
* Correct answer
* Explanation

using only the retrieved context.

---

## 📂 Knowledge Base

Historical facts are stored inside:

```
data/sports_facts.json
```

Example:

```json
{
  "sport": "Football",
  "fact": "The FIFA World Cup was first held in 1930."
}
```

---

## 🧠 Retrieval-Augmented Generation (RAG)

This project follows the RAG workflow:

```
User Query
     │
     ▼
Retrieve Historical Facts (ChromaDB)
     │
     ▼
Retrieve Live News (DuckDuckGo)
     │
     ▼
Combine Context
     │
     ▼
LLM
     │
     ▼
Grounded Quiz
```

---

## 🖥️ User Interface

The Streamlit dashboard allows users to:

* Select a sport
* Choose difficulty
* Generate quizzes
* View explanations
* Inspect retrieved context

---

## 📦 Dependencies

```
streamlit>=1.30.0
chromadb>=0.4.22
duckduckgo-search>=4.4.1
openai>=1.10.0
python-dotenv>=1.0.1
sentence-transformers>=2.3.0
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

* User authentication
* Score tracking
* Timed quizzes
* Leaderboard
* More sports categories
* Image-based questions
* Voice interaction
* Export quizzes as PDF
* OpenAI JSON Mode
* LangChain or LlamaIndex integration

---

## 🛠️ Troubleshooting

### ChromaDB SQLite Error

```bash
pip install pysqlite3-binary
```

Then add:

```python
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
```

at the top of `database.py`.

---

### API Key Not Found

Ensure your `.env` file exists and contains:

```env
OPENAI_API_KEY=your_api_key
```

---

### Empty Search Results

Check your internet connection or retry the DuckDuckGo search.

---
, Streamlit, ChromaDB, DuckDuckGo Search, and OpenAI/Gemini.
"# AI-Powered-Sports-Quiz-Generator" 
