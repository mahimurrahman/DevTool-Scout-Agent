
# 🔎 DevTool Scout Agent

**AI-powered GitHub developer tool finder**

DevTool Scout is an AI agent that discovers useful open-source developer tools by searching GitHub repositories and analyzing them using a large language model.

The system combines **GitHub API search + LLM reasoning** to recommend the most relevant developer tools for a given query.

---

## 🌐 Live Demo

Try the running application here:

**https://huggingface.co/spaces/mahim217/DevTool-Scout**

---

## ✨ Features

* 🔍 Search GitHub repositories for developer tools
* 🤖 AI agent analyzes repositories using an LLM
* ⭐ Returns top tools sorted by relevance
* 🔗 Clickable GitHub links for each tool
* 📊 Structured table output for easy comparison
* ⚡ Fast deployment using Hugging Face Spaces

---

## 🧠 How It Works

The system follows a simple AI agent pipeline:

User Query
↓
GitHub Search Tool (API)
↓
Repository Data Collection
↓
LLM Analysis (Groq API)
↓
Structured Recommendations
↓
Displayed in Gradio UI

The AI agent searches GitHub, collects repository metadata (stars, description, URL), and uses an LLM to recommend the best tools.

---

## 🏗️ Project Structure

```
DevTool-Scout-Agent
│
├── app.py                # Entry point for the application
├── requirements.txt      # Project dependencies
├── README.md
│
├── agent
│   └── agent.py          # Core agent logic
│
├── models
│   └── groq_model.py     # LLM interaction (Groq API)
│
├── tools
│   └── github_search.py  # GitHub API search tool
│
└── ui
    └── app.py            # Gradio user interface
```

---

## ⚙️ Installation (Local Run)

Clone the repository:

```
git clone https://github.com/mahimurrahman/DevTool-Scout-Agent.git
cd DevTool-Scout-Agent
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file:

```
GITHUB_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```
python app.py
```

---

## 🔑 Required APIs

The project uses two APIs:

### GitHub API

Used to search public repositories.

Create token:
https://github.com/settings/tokens

Scope required:

```
public_repo
```

---

### Groq API

Used for LLM reasoning and analysis.

Get API key:

https://console.groq.com/

---

## 💡 Example Queries

You can search for:

```
python ai agents
react ui libraries
devops automation tools
game ai frameworks
```

---

## 🚀 Deployment

The project is deployed using **Hugging Face Spaces** with Gradio.

Deployment steps:

1. Push project to GitHub
2. Create a Hugging Face Space
3. Add environment secrets
4. Deploy using `app.py`

---

## 🛠️ Tech Stack

* Python
* Gradio
* GitHub REST API
* Groq LLM API
* Hugging Face Spaces

---

## ⭐ Future Improvements

* Smarter GitHub query generation
* Repository ranking system
* Multi-tool agent architecture
* Better UI result visualization
* Automatic README analysis


