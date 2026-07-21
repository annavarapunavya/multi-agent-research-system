
# ============================================================
# AI Multi-Agent Research System - Streamlit UI
# ============================================================

import streamlit as st
from app import run_research
import time
from datetime import datetime
from utils.pdf_generator import create_pdf
import os
from datetime import datetime

st.set_page_config(
    page_title="AI Multi-Agent Research System",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:#F5F7FB;
}

.hero{
background:linear-gradient(135deg,#4F46E5,#7C3AED);
padding:35px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:25px;
box-shadow:0 10px 25px rgba(79,70,229,.25);
}

.hero h1{
font-size:48px;
margin-bottom:10px;
}

.hero p{
font-size:18px;
opacity:.95;
}

.feature-box{
background:white;
padding:25px;
border-radius:18px;
text-align:center;
box-shadow:0 8px 18px rgba(0,0,0,.08);
transition:.3s;
}

.feature-box:hover{
transform:translateY(-6px);
}

.stButton>button{
width:100%;
height:58px;
border:none;
border-radius:14px;
font-size:20px;
font-weight:bold;
background:linear-gradient(90deg,#4F46E5,#7C3AED);
color:white;
}

.stTextInput input{
height:52px;
border-radius:12px;
font-size:18px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🤖 AI Research")
    st.caption("Multi-Agent Report Generator")
    st.markdown("---")
    st.markdown("""
### 🔄 Workflow

🔍 Research Agent

✍️ Writer Agent

✔️ Fact Checker

---

### 🚀 Tech Stack

- CrewAI
- Gemini
- Streamlit
- Python

---

### ✨ Features

- AI Research
- Report Generation
- Fact Verification
- Markdown Export
""")

st.markdown("""
<div class="hero">
<h1>🤖 AI Multi-Agent Research System</h1>
<p>
Generate professional AI-powered research reports using collaborative
Research, Writer and Fact Checker agents.
</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("<div class='feature-box'><h3>🔍 Research</h3>Collects reliable information.</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='feature-box'><h3>✍️ Writer</h3>Creates structured reports.</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='feature-box'><h3>✔️ Fact Checker</h3>Validates the final content.</div>", unsafe_allow_html=True)

st.write("")

left,right = st.columns([4,1])

with left:
    topic = st.text_input(
        "Research Topic",
        placeholder="Example: Explainable AI, Agentic AI, Quantum Computing..."
    )

with right:
    st.write("")
    st.write("")
    generate = st.button("🚀 Generate")

if generate:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    start = time.time()

    with st.status("🤖 AI Agents are generating your research report...", expanded=True) as status:

        st.write("🔍 Research Agent is gathering information...")

        result, output_path = run_research(topic)

        st.write("✍️ Writer Agent has created the report.")
        st.write("✔️ Fact Checker has verified the report.")

        status.update(
            label="✅ Research Report Generated Successfully!",
            state="complete"
        )

    execution = round(time.time() - start, 2)

    st.markdown("---")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("📌 Topic", topic)
    m2.metric("🤖 Agents", "3")
    m3.metric("⏱ Time", f"{execution}s")
    m4.metric("✅ Status", "Completed")

    st.markdown("---")

    with st.expander("📄 View Generated Report", expanded=True):
        st.markdown(result)

    with open(output_path, "r", encoding="utf-8") as f:
        report = f.read()

    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = topic.replace(" ", "_")
    pdf_path = os.path.join(
        "reports",
        f"{safe_topic}_{timestamp}.pdf"
    )
    create_pdf(report, pdf_path)
    st.download_button(
        "⬇️ Download Markdown Report",
        data=report,
        file_name="research_report.md",
        mime="text/markdown"
    )

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            "📄 Download PDF Report",
            data=pdf_file.read(),
            file_name="research_report.pdf",
            mime="application/pdf"
        )

st.markdown("---")
st.caption("© 2026 AI Multi-Agent Research System | Built with CrewAI • Gemini • Streamlit")