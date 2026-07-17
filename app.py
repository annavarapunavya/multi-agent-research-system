from dotenv import load_dotenv
import os

from crewai import Crew, Task, LLM
from agents.research_agent import create_research_agent
from agents.writer_agent import create_writer_agent

from tasks.research_task import create_research_task
from tasks.writing_task import create_writing_task
from utils.file_handler import save_report

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=gemini_api_key,
    temperature=0.2,
)

research_agent = create_research_agent(llm)
writer_agent = create_writer_agent(llm)

print("=" * 60)
print("🤖 Multi-Agent Research System")
print("=" * 60)

topic = input("\nEnter a research topic: ").strip()

if not topic:
    raise ValueError("Research topic cannot be empty.")

research_task = create_research_task(
    research_agent,
    topic
)

writing_task = create_writing_task(
    writer_agent,
    research_task
)

crew = Crew(
    agents=[
        research_agent,
        writer_agent
    ],

    tasks=[
        research_task,
        writing_task
    ],

    verbose=True
)

result = crew.kickoff()

output_path = save_report(topic, result)

print("\n" + "=" * 60)
print("✅ Research Completed")
print("=" * 60)
print(f"📄 Report saved successfully: {output_path}")
print("\nPreview (first 500 characters):\n")
print(str(result)[:500] + "...")