import gradio as gr
from app.handlers.sentiment_handler import analyze_sentiment_with_response
from app.utils.preprocessing import clean_text

def chat_with_sentiment(user_input):
    """
    Preprocesses input, analyzes sentiment, and generates a response.
    """
    cleaned_input = clean_text(user_input)
    sentiment_result = analyze_sentiment_with_response(cleaned_input)
    return f"Sentiment: {sentiment_result['sentiment']} (Confidence: {sentiment_result['confidence']})\nResponse: {sentiment_result['response']}"

def create_interface():
    """
    Creates the Gradio interface with a chat feature.
    """
    # Sentiment chat demo
    chatbot = gr.Interface(
        fn=chat_with_sentiment,
        inputs="text",
        outputs="text",
        title="Chatbot with Sentiment Analysis",
        description="Chat with the bot and get responses based on sentiment.",
    )

    return gr.TabbedInterface(
        interface_list=[chatbot],
        tab_names=["Chatbot with Sentiment"]
    )

if __name__ == "__main__":
    interface = create_interface()
    interface.launch()
