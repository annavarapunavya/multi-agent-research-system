from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report_text, output_path):
    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):
        story.append(Paragraph(line.replace(" ", "&nbsp;"), styles["BodyText"]))

    doc.build(story)