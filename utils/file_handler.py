import os


def save_report(topic, content):
    """
    Save the generated report as a Markdown file.

    Args:
        topic (str): Research topic.
        content (str): Generated report.
    """

    os.makedirs("output", exist_ok=True)

    file_name = topic.replace(" ", "_") + "_Report.md"

    output_path = os.path.join("output", file_name)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(str(content))

    return output_path