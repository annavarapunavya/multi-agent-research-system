from dotenv import load_dotenv
import os

from crewai import Crew, Task, LLM
from agents.research_agent import create_research_agent
from tasks.research_task import create_research_task

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key = gemini_api_key,
    temperature = 0.2
)

research_agent = create_research_agent(llm)
topic = input("\nEnter a research topic: ")
research_task = create_research_task(
    research_agent,
    topic
)

crew = Crew(
    agents=[research_agent],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()

print("\n" + "=" * 60)
print("RESEARCH REPORT")
print("=" * 60)
print(result)