# ==============================
# app.py
# CEO Persona Analyzer + Pitch Optimizer
# Developed by Salma Bibi
# ==============================

# Import required modules
import streamlit as st
from utils import (
    extract_keywords,
    analyze_sentiment,
    match_persona_keywords,
    rewrite_pitch_to_match_tone
)

# Page configuration
st.set_page_config(page_title="CEO Persona Analyzer", layout="centered")

# Title and introduction
st.title("CEO Persona Analyzer + Pitch Optimizer")

st.write(
    """
    Analyze a CEO's communication style using NLP, then match and improve your resume or pitch
    to better align with their persona. Built using KeyBERT, TextBlob, and Streamlit.
    """
)

# Input section — CEO bio or public statement
ceo_text = st.text_area(
    label="CEO Bio / Statement",
    placeholder="Paste the CEO’s LinkedIn post or public message here...",
    height=200
)

# Input section — user's resume or pitch text
user_text = st.text_area(
    label="Resume / Pitch Summary",
    placeholder="Paste your resume summary or elevator pitch here...",
    height=200
)

# Button — Analyze CEO persona
if st.button("Analyze CEO Persona"):
    if ceo_text:
        keywords = extract_keywords(ceo_text)
        tone, polarity = analyze_sentiment(ceo_text)

        st.subheader("CEO Style Summary")
        st.text(f"Top Keywords: {', '.join(keywords)}")
        st.text(f"Tone: {tone}")
        st.text(f"Sentiment Polarity: {polarity}")
    else:
        st.warning("Please paste the CEO bio first to analyze.")

# Button — Match resume keywords with CEO persona
if st.button("Match Resume to CEO Style"):
    if ceo_text and user_text:
        matched, score = match_persona_keywords(ceo_text, user_text)

        st.subheader("Resume Match Results")
        st.text(f"Matching Keywords: {', '.join(matched)}")
        st.text(f"Match Score: {score}%")
    else:
        st.warning("Please paste both CEO bio and your resume or pitch.")

# Button — Rewrite pitch to match CEO tone
if st.button("Rewrite Pitch Based on CEO Tone"):
    if ceo_text and user_text:
        tone, _ = analyze_sentiment(ceo_text)
        rewritten = rewrite_pitch_to_match_tone(user_text, tone)

        st.subheader("Tone-Adjusted Pitch")
        st.text_area("Modified Pitch", value=rewritten, height=200)
    else:
        st.warning("Please provide both CEO text and your pitch for rewriting.")

# Footer
st.markdown("---")
st.caption("Developed by Salma Bibi | NLP, Streamlit, and ML Applications")