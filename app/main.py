import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gradio as gr
from app.handlers.sentiment_handler import analyze_sentiment_with_response
from app.utils.preprocessing import clean_text
import random

def chat_with_sentiment(message, history):
    """
    Preprocesses input, analyzes sentiment, and generates a response.
    """
    # Clean the message
    cleaned_input = clean_text(message)
    print(f"cleaned input: {clean_text}")
    # Perform sentiment analysis
    sentiment_result = analyze_sentiment_with_response(cleaned_input)
    print(f"sentiment result: {sentiment_result}")

    # Build the response based on sentiment
    sentiment_response = f"Sentiment: {sentiment_result['sentiment']} (Confidence: {sentiment_result['confidence']})\nResponse: {sentiment_result['response']}"
    print(sentiment_response)
    # Append the new message and response to history
    history.append((message, "thankuou"))

    # Return the response and updated history
    return sentiment_result['response']

def random_response(message, history):
    return random.choice(["Yes", "No"])

# demo = gr.ChatInterface(random_response, type="messages")
def vote(data: gr.LikeData):
    if data.liked:
        print("You upvoted this response: " + data.value["value"])
    else:
        print("You downvoted this response: " + data.value["value"])



with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        # Clean the message
        cleaned_input = clean_text(message)
        print(f"cleaned input: {clean_text}")
        # Perform sentiment analysis
        sentiment_result = analyze_sentiment_with_response(cleaned_input)
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": sentiment_result['response']})
        # time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(debug=True)
