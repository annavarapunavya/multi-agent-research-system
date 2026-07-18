from crewai import Agent


def create_writer_agent(llm):
    return Agent(
        role="Technical Content Writer",

        goal=(
            "Transform research findings into clear, engaging, and "
            "well-structured reports."
        ),

        backstory=(
            "You are an experienced technical writer who specializes "
            "in converting complex research into professional, "
            "easy-to-understand documentation. "
            "Your reports are logical, concise, and readable."
        ),
        max_execution_time=300,

        llm=llm,
        verbose=True
    )