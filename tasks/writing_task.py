from crewai import Task


def create_writing_task(writer_agent, research_task):
    return Task(
        description=(
            """
            Convert the research findings into a professional report.

            The report should:
            - Have a clear title
            - Use proper headings
            - Include bullet points where appropriate
            - Be easy to read
            - Maintain a professional tone
            - Preserve all important technical information
            """
        ),

        expected_output=(
            """
            A polished research report in Markdown format,
            suitable for technical documentation.
            """
        ),

        agent=writer_agent,

        context=[research_task]
    )