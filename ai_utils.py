# ai_utils.py
from textblob import TextBlob
 
def analyze_sentiment(text: str) -> str:
    """
    Returns sentiment as Positive, Negative, or Neutral
    """
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"
 
def summarize_text(text: str) -> str:
    """
    Very simple summarization: returns first 2 sentences
    """
    sentences = text.split(".")
    summary = ".".join(sentences[:2]).strip()
    if summary and summary[-1] != ".":
        summary += "."
    return summary
 
