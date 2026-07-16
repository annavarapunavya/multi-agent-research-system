# 🤖 Multi-Agent Research System with CrewAI

A modular **Agentic AI** application built using **CrewAI** and **Google Gemini** that demonstrates **multi-agent collaboration**, **role-based agent design**, and **task orchestration**.

This project showcases how specialized AI agents can collaborate to perform research tasks and generate structured reports. It is designed as a portfolio project to demonstrate practical Agentic AI concepts used in modern AI applications.

---

# 🚀 Features

### ✅ Current Features (Version 1.0)

- Research Agent powered by Gemini
- Modular Agent & Task architecture
- CrewAI workflow orchestration
- Generates structured research reports
- Environment variable management using `.env`
- Clean project structure following software engineering principles

---

# 🛠 Planned Features

- 🔄 Interactive topic input
- ✍️ Writer Agent
- ✅ Fact Checker Agent
- 🌐 Web Search Tool Integration
- 📄 Markdown report generation
- 📑 PDF export
- 🖥 Streamlit Web Interface
- 💾 Research history
- 🔍 Multi-agent collaboration workflow

---

# 📂 Project Structure

```text
multi-agent-research-system/
│
├── agents/
│   └── research_agent.py
│
├── tasks/
│   └── research_task.py
│
├── output/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🧠 System Architecture

```text
                 User
                   │
                   ▼
          Research Topic
                   │
                   ▼
           Research Task
                   │
                   ▼
       Senior AI Research Agent
                   │
                   ▼
            CrewAI Orchestrator
                   │
                   ▼
        Google Gemini 3.5 Flash
                   │
                   ▼
         Structured Research Report
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| CrewAI | Multi-Agent Framework |
| Google Gemini API | Large Language Model |
| LiteLLM | LLM Integration Layer |
| python-dotenv | Environment Variable Management |
| Git & GitHub | Version Control |

---

# 🏗 Software Engineering Concepts Used

- Agentic AI
- Multi-Agent Systems
- Role-Based Agent Design
- Task Orchestration
- Dependency Injection
- Modular Programming
- Single Responsibility Principle (SRP)
- Environment Variable Management
- Version Control using Git

---

# 👨‍💻 Current Workflow

```text
Load Environment Variables
          │
          ▼
Create Gemini LLM
          │
          ▼
Create Research Agent
          │
          ▼
Create Research Task
          │
          ▼
Create Crew
          │
          ▼
Crew Kickoff
          │
          ▼
Generate Research Report
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/annavarapunavya/multi-agent-research-system.git
```

Move into the project

```bash
cd multi-agent-research-system
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 📌 Current Output

The application generates a structured research report for the given topic using the Research Agent.

Example topic:

```
Explainable AI
```

Output includes:

- Introduction
- Key Concepts
- Applications
- Advantages
- Challenges
- Recent Developments
- Conclusion

---

# 📈 Roadmap

- [x] Setup CrewAI Project
- [x] Configure Gemini API
- [x] Create Research Agent
- [x] Create Research Task
- [x] CrewAI Integration
- [x] Generate Research Report
- [x] Interactive Topic Input
- [ ] Writer Agent
- [ ] Fact Checker Agent
- [ ] Web Search Tool
- [ ] Markdown Export
- [ ] PDF Export
- [ ] Streamlit UI

---

# 🎯 Learning Outcomes

This project demonstrates:

- Agentic AI Development
- CrewAI Framework
- LLM Integration
- Multi-Agent Architecture
- AI Workflow Design
- Modular Python Project Structure
- Git & GitHub Workflow
- API Integration
- Prompt Engineering

---

# 👩‍💻 Author

**Navya Annavarapu**

B.Tech Computer Science Engineering

Passionate about Artificial Intelligence, Machine Learning, Data Science, and Agentic AI.

GitHub:
https://github.com/annavarapunavya

---

# ⭐ Future Scope

This project will evolve into a complete **Multi-Agent Research Assistant** capable of:

- Researching any topic
- Searching the web
- Verifying facts
- Writing professional reports
- Exporting reports as PDF
- Providing an interactive web interface
- Demonstrating real-world Agentic AI collaboration