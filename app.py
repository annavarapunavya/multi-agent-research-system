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
    api_key=gemini_api_key,
    temperature=0.2,
)

research_agent = create_research_agent(llm)

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

crew = Crew(
    agents=[research_agent],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Generate filename
file_name = topic.replace(" ", "_") + "_Report.md"

# Create full file path
output_path = os.path.join("output", file_name)

# Save report
with open(output_path, "w", encoding="utf-8") as file:
    file.write(str(result))

print("\n" + "=" * 60)
print("✅ Research Completed")
print("=" * 60)
print(f"📄 Report saved successfully: {output_path}")
print("\nPreview (first 500 characters):\n")
print(str(result)[:500] + "...")