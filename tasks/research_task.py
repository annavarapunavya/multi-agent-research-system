from crewai import Task


def create_research_task(agent, topic):
    return Task(
        description=(
            f"""
            Conduct comprehensive research on the topic: "{topic}".

            Your report should include:
            1. Introduction
            2. Key Concepts
            3. Applications
            4. Advantages
            5. Challenges
            6. Recent Developments
            7. Conclusion

            Use accurate and well-organized information.
            """
        ),
        expected_output="""
        A professional research report in Markdown format
        with headings, bullet points, and clear explanations.
        """,
        agent=agent,
    )