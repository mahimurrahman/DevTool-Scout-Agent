import gradio as gr
from agent.agent import run_agent


def search(query):
    return run_agent(query)


description = """
# 🔎 DevTool Scout

### AI-powered GitHub Developer Tool Finder

Created by **Mahimur Rahman Khan**

DevTool Scout helps developers discover useful open-source tools from GitHub.  
It searches repositories and analyzes them using an AI model to recommend the most relevant developer tools.


---

### 💡 Example Searches

- python ai agents  
- react ui libraries  
- devops automation tools  
- game ai frameworks  
"""


# Custom CSS to fix table layout and star column
custom_css = """
#results table {
    width: 100%;
    border-collapse: collapse;
}

#results th, #results td {
    padding: 12px;
    border-bottom: 1px solid #444;
}

#results th {
    font-size: 16px;
}

#results td {
    font-size: 15px;
}

#results th:nth-child(1),
#results td:nth-child(1) {
    width: 220px;
}

#results th:nth-child(2),
#results td:nth-child(2) {
    width: 120px;
    text-align: center;
    white-space: nowrap;
}

#results th:nth-child(3),
#results td:nth-child(3) {
    width: 60%;
}

#results th:nth-child(4),
#results td:nth-child(4) {
    width: 200px;
}

#results a {
    color: #4ea1ff;
    text-decoration: none;
    font-weight: 500;
}

#results a:hover {
    text-decoration: underline;
}
"""


with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as app:

    gr.Markdown(description)

    with gr.Row():

        query = gr.Textbox(
            label="Search Developer Tools",
            placeholder="Example: python ai agents",
            lines=1,
            scale=4
        )

    with gr.Row():

        clear_btn = gr.Button("Clear")
        submit_btn = gr.Button("Search", variant="primary")

    gr.Markdown("## ⭐ Recommended Developer Tools")

    output = gr.Markdown(
        value="Search for developer tools to see results.",
        elem_id="results"
    )

    submit_btn.click(
        fn=search,
        inputs=query,
        outputs=output
    )

    clear_btn.click(
        fn=lambda: ("", "Search for developer tools to see results."),
        outputs=[query, output]
    )


app.launch()