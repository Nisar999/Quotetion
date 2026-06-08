"""
Quotetion — Streamlit Frontend
================================
A beautiful, dark-themed motivational quote generator.
Connects to the FastAPI backend for motivation data.

Run locally:
    streamlit run app.py
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Configuration
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Page Configuration
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.set_page_config(
    page_title="Quotetion — Get Motivated",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Custom CSS — Glassmorphism + Dark Theme
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(
    """
<style>
    /* ── Import Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global Styles ── */
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%);
        font-family: 'Inter', sans-serif;
    }

    /* ── Hide Streamlit Defaults ── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ── Animated Background Orbs ── */
    .bg-orbs {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .bg-orbs::before, .bg-orbs::after {
        content: '';
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.15;
        animation: float 15s ease-in-out infinite;
    }

    .bg-orbs::before {
        width: 400px;
        height: 400px;
        background: #a855f7;
        top: -100px;
        right: -100px;
    }

    .bg-orbs::after {
        width: 350px;
        height: 350px;
        background: #6366f1;
        bottom: -100px;
        left: -100px;
        animation-delay: -7s;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        33% { transform: translateY(-30px) rotate(5deg); }
        66% { transform: translateY(20px) rotate(-3deg); }
    }

    /* ── Hero Section ── */
    .hero {
        text-align: center;
        padding: 2rem 0 1rem 0;
        position: relative;
        z-index: 1;
    }

    .hero h1 {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a855f7, #6366f1, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }

    .hero p {
        color: #94a3b8;
        font-size: 1.15rem;
        font-weight: 300;
        letter-spacing: 0.02em;
    }

    /* ── Glass Card ── */
    .glass-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        position: relative;
        z-index: 1;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border-color: rgba(168, 85, 247, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.1);
    }

    /* ── Category Badge ── */
    .category-badge {
        display: inline-block;
        background: linear-gradient(135deg, #a855f7, #6366f1);
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
    }

    /* ── Result Cards ── */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        position: relative;
        z-index: 1;
        transition: all 0.3s ease;
    }

    .result-card:hover {
        background: rgba(255, 255, 255, 0.05);
        transform: translateX(4px);
    }

    .result-card .card-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .result-card .card-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #a855f7;
        margin-bottom: 0.5rem;
    }

    .result-card .card-content {
        font-size: 1.05rem;
        color: #e2e8f0;
        line-height: 1.6;
        font-weight: 400;
    }

    .result-card.motivation {
        border-left: 3px solid #a855f7;
    }

    .result-card.quote {
        border-left: 3px solid #6366f1;
    }

    .result-card.action {
        border-left: 3px solid #ec4899;
    }

    /* ── Divider ── */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(168, 85, 247, 0.3), transparent);
        margin: 2rem 0;
        border: none;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #475569;
        font-size: 0.85rem;
        position: relative;
        z-index: 1;
    }

    .footer a {
        color: #a855f7;
        text-decoration: none;
    }

    /* ── Button Styling ── */
    .stButton > button {
        background: linear-gradient(135deg, #a855f7, #6366f1) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        letter-spacing: 0.02em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ── Text Input ── */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-size: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        padding: 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 0 2px rgba(168, 85, 247, 0.2) !important;
    }

    .stTextArea label {
        color: #94a3b8 !important;
        font-weight: 500 !important;
    }

    /* ── Error/Warning Styling ── */
    .stAlert {
        border-radius: 12px !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-color: #a855f7 !important;
    }
</style>

<!-- Background Orbs -->
<div class="bg-orbs"></div>
""",
    unsafe_allow_html=True,
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Hero Section
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(
    """
<div class="hero">
    <h1>🌟 Quotetion</h1>
    <p>Tell us your challenge. We'll fuel your fire.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# API Communication Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def call_generate(situation: str) -> dict | None:
    """Call the /generate endpoint with the user's situation."""
    try:
        response = requests.post(
            f"{BACKEND_URL}/generate",
            json={"situation": situation},
            timeout=15,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error(
            "🔌 **Cannot connect to the backend.** "
            "Make sure the FastAPI server is running."
        )
        return None
    except requests.exceptions.Timeout:
        st.error("⏱️ **Request timed out.** Please try again.")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ **API Error:** {e}")
        return None


def call_surprise() -> dict | None:
    """Call the /surprise endpoint for random motivation."""
    try:
        response = requests.get(
            f"{BACKEND_URL}/surprise",
            timeout=15,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error(
            "🔌 **Cannot connect to the backend.** "
            "Make sure the FastAPI server is running."
        )
        return None
    except requests.exceptions.Timeout:
        st.error("⏱️ **Request timed out.** Please try again.")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ **API Error:** {e}")
        return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Display Results
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def display_results(data: dict):
    """Render the motivation results in beautiful glassmorphism cards."""
    # Category Badge
    st.markdown(
        f'<div style="text-align: center;">'
        f'<span class="category-badge">🏷️ {data["category"]}</span>'
        f"</div>",
        unsafe_allow_html=True,
    )

    # Motivation Card
    st.markdown(
        f"""
    <div class="result-card motivation">
        <div class="card-icon">💪</div>
        <div class="card-label">Motivation</div>
        <div class="card-content">{data["motivation"]}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quote Card
    st.markdown(
        f"""
    <div class="result-card quote">
        <div class="card-icon">💬</div>
        <div class="card-label">Inspirational Quote</div>
        <div class="card-content">"{data["quote"]}"</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Action Step Card
    st.markdown(
        f"""
    <div class="result-card action">
        <div class="card-icon">🎯</div>
        <div class="card-label">Action Step</div>
        <div class="card-content">{data["action_step"]}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main Input Section
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown(
    '<div class="glass-card">', unsafe_allow_html=True
)

situation = st.text_area(
    "💭 What's on your mind?",
    placeholder="e.g., I am preparing for placements and feeling nervous...",
    height=100,
    max_chars=500,
    key="situation_input",
)

# Action Buttons
col1, col2 = st.columns(2)

with col1:
    generate_clicked = st.button(
        "✨ Get Motivated",
        use_container_width=True,
        key="btn_generate",
    )

with col2:
    surprise_clicked = st.button(
        "🎲 Surprise Me",
        use_container_width=True,
        key="btn_surprise",
    )

st.markdown("</div>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Handle Button Clicks
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if generate_clicked:
    if not situation or len(situation.strip()) < 2:
        st.warning("✏️ Please describe your situation (at least 2 characters).")
    else:
        with st.spinner("🌟 Generating your motivation..."):
            result = call_generate(situation.strip())
        if result:
            st.markdown(
                '<div class="custom-divider"></div>', unsafe_allow_html=True
            )
            display_results(result)

if surprise_clicked:
    with st.spinner("🎲 Rolling the dice..."):
        result = call_surprise()
    if result:
        st.markdown(
            '<div class="custom-divider"></div>', unsafe_allow_html=True
        )
        display_results(result)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Footer
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="footer">
    <p>Built with ❤️ using <strong>Streamlit</strong> + <strong>FastAPI</strong></p>
    <p>A teaching project for Deployment, CI/CD & DevOps</p>
</div>
""",
    unsafe_allow_html=True,
)
