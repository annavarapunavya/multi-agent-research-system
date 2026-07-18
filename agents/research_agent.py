from crewai import Agent
#from tools.search_tool import search_tool

def create_research_agent(llm):
    return Agent(
        role = "Senior AI Researcher",
        goal = "Research topics throughly and provide accurate information.",
        backstory = ( "You are a senior research analyst with extensive experience in "
    "analyzing technical papers, industry reports, and trusted online sources. "
    "You are known for gathering accurate information, cross-checking facts, "
    "identifying key insights, and presenting findings in a clear, structured, "
    "and unbiased manner."),
    llm = llm,
    max_execution_time = 300,
    #tools=[search_tool],
    verbose = True
    )