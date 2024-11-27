from app.utils.preprocessing import clean_text

def test_clean_text():
    text = "   This   is   a   test   sentence.   "
    cleaned = clean_text(text)

    # Assert cleaning functionality
    assert cleaned == "This is a test sentence."
