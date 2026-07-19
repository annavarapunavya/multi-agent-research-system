from dotenv import load_dotenv
import os

from crewai import Crew, Task, LLM
from agents.research_agent import create_research_agent
from agents.writer_agent import create_writer_agent
from agents.fact_checker_agent import create_fact_checker_agent

from tasks.research_task import create_research_task
from tasks.writing_task import create_writing_task
from tasks.fact_check_task import create_fact_check_task
from utils.file_handler import save_report

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=gemini_api_key,
    temperature=0.2,
)

research_agent = create_research_agent(llm)
writer_agent = create_writer_agent(llm)
fact_checker_agent = create_fact_checker_agent(llm)

def run_research(topic):
    if not topic:
        raise ValueError("Research topic cannot be empty.")

    # Create tasks
    research_task = create_research_task(
        research_agent,
        topic
    )

    writing_task = create_writing_task(
        writer_agent,
        research_task
    )

    fact_check_task = create_fact_check_task(
        fact_checker_agent,
        writing_task
    )

    # Create Crew
    crew = Crew(
        agents=[
            research_agent,
            writer_agent,
            fact_checker_agent
        ],
        tasks=[
            research_task,
            writing_task,
            fact_check_task
        ],
        verbose=True
    )

    # Execute Crew
    result = crew.kickoff()

    report = result.raw
    # Save report
    output_path = save_report(topic, report)

    return report, output_path

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 Multi-Agent Research System")
    print("=" * 60)

    topic = input("\nEnter a research topic: ").strip()

    result, output_path = run_research(topic)

    print("\n" + "=" * 60)
    print("✅ Research Completed")
    print("=" * 60)
    print(f"📄 Report saved successfully: {output_path}")

    print("\nPreview (first 500 characters):\n")
    print(str(result)[:500] + "...")