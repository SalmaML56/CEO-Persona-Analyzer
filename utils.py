# ==============================
# utils.py
# NLP Core Functions
# ==============================

from keybert import KeyBERT
from textblob import TextBlob

# Initialize keyword extractor
kw_model = KeyBERT()

def extract_keywords(text, num_keywords=5):
    """
    Extract keyphrases from input text using KeyBERT.
    Returns top keywords that define communication style.
    """
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=num_keywords
    )
    return [kw[0] for kw in keywords]

def analyze_sentiment(text):
    """
    Analyze text sentiment using TextBlob.
    Returns tone classification and polarity score.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    tone = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return tone, polarity

def match_persona_keywords(ceo_text, user_pitch):
    """
    Compare CEO text and resume pitch keywords.
    Returns list of overlapping traits and a match score (%).
    """
    ceo_keywords = set(extract_keywords(ceo_text))
    pitch_keywords = set(extract_keywords(user_pitch))

    overlap = ceo_keywords.intersection(pitch_keywords)
    score = round((len(overlap) / len(ceo_keywords)) * 100, 2) if ceo_keywords else 0

    return list(overlap), score

def rewrite_pitch_to_match_tone(user_text, tone):
    """
    Adjust user's pitch based on CEO's tone.
    Placeholder logic using TextBlob; can be extended with transformers.
    """
    blob = TextBlob(user_text)

    if tone == "Positive":
        rewritten = blob.correct()
        result = f"Optimistic Version:\n{rewritten}"
    elif tone == "Negative":
        result = f"Direct Version:\n{user_text.lower()}"
    else:
        result = f"Neutral Style:\n{user_text}"

    return result