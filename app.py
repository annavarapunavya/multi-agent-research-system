from dotenv import load_dotenv
import os

from crewai import Crew, Task, LLM

from agents.research_agent import create_research_agent

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key = gemini_api_key,
    temperature = 0.2
)