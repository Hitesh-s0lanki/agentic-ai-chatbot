# Agent AI Use-cases Example

A Streamlit-powered application showcasing multiple agentic AI use cases using LangGraph, Tavily, OpenAI, Groq, and LangChain.

**GitHub Repository:** [agentic-ai-chatbot](https://github.com/Hitesh-s0lanki/agentic-ai-chatbot)

**Live Demo:** [hitesh-s0lanki-agentic-ai-chatbot-app](https://hitesh-s0lanki-agentic-ai-chatbot-app-1sl3to.streamlit.app/)

---

## 🚀 Features

- **Streamlit UI:** Fast, interactive interface for exploring AI use cases.
- **LLM Integrations:** OpenAI (gpt-4o), Groq via langchain-groq.
- **Tool Calls:** News & web search using Tavily.
- **Agent Framework:** Built with LangGraph and LangChain for stateful, tool-enabled agents.
- **Organized File Structure:** Modular components and clear directory layout for easy extension.

## 💡 Use Cases

1. **Basic Chatbot** – Stateful conversational interface.
2. **Chatbot with Tool** – Calls external tools to fetch and display recent news.
3. **AI News** – Curated AI news explorer.
4. **Weekly AI News Summary** – Automated weekly recap of AI developments.

## 🛠 Tech Stack

- Python 3.9+
- Streamlit
- OpenAI Python SDK
- Groq LLM SDK (via langchain-groq)
- LangChain & LangGraph
- Tavily API for web/news retrieval

## 📦 Installation

```bash
git clone https://github.com/Hitesh-s0lanki/agentic-ai-chatbot.git
cd agentic-ai-chatbot
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
groq_api_key=your_groq_api_key
```

## ▶️ Usage

```bash
streamlit run app.py
```

- Select your LLM provider and model.
- Choose a use case from the sidebar.
- Enter your API keys.
- Interact with the agent in the main panel.

## 📂 Project Structure

```
agentic-ai-chatbot/
├── app.py              # main file
├── components/ui       # UI components and layouts
├── components/nodes    # Individual node use-case implementations
├── components/graph    # Graph builder Function
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a pull request.

---

**Enjoy exploring Agent AI!**
