from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment_with_response(user_input):
    """
    Analyzes sentiment and returns a response based on the sentiment.
    """
    # Perform sentiment analysis
    result = sentiment_pipeline(user_input)[0]
    sentiment = result["label"]
    score = result["score"]

    # Generate a response based on the sentiment
    if sentiment == "POSITIVE":
        response = "I'm glad to hear that! 😊"
    elif sentiment == "NEGATIVE":
        response = "I'm sorry to hear that. I'm here to help. 🙁"
    else:
        response = "Thanks for sharing! Let me know how I can assist. 😐"

    return {
        "sentiment": sentiment,
        "confidence": round(score, 2),
        "response": response
    }
