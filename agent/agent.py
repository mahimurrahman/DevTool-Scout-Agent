from tools.github_search import search_repositories
from models.groq_model import ask_llm

def run_agent(query):

    repos = search_repositories(query)

    repo_text = ""

    for r in repos:
        repo_text += f"""
Repository: {r['name']}
Stars: {r['stars']}
Description: {r['description']}
URL: {r['url']}
"""

    prompt = f"""
You are DevTool Scout.

IMPORTANT RULES:

1. Use ONLY the repositories listed below.
2. Do NOT invent tools.
3. Do NOT recommend tools that are not in the list.
4. If the list is empty, say "No relevant repositories found."

User Query:
{query}

GitHub Results:

{repo_text}

Return results in this Markdown table format:

| Tool | Stars | Description | GitHub |
|------|------|-------------|--------|

Use the exact repository names and URLs from the list above.
"""

    answer = ask_llm(prompt)

    return answer

