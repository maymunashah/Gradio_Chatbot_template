from transformers import pipeline

def analyze_sentiment_text(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return f"{result['label']} (confidence: {result['score']:.2f})"
