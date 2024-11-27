from app.handlers.sentiment_handler import analyze_sentiment

def test_analyze_sentiment():
    text = "I love this application! It's fantastic."
    response = analyze_sentiment(text)

    # Assert that the sentiment handler works correctly
    assert "The sentiment is:" in response
    assert "POSITIVE" in response or "NEGATIVE" in response or "NEUTRAL" in response
