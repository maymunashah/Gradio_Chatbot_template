# **Gradio Chatbot Template**

## **Overview**

This project is a **template** for building chatbot applications using [Gradio](https://gradio.app/). It provides a starting point for developers to integrate multiple machine learning functionalities, including:

1. **Document Upload for Q&A**: Users can upload a document, and the system answers context-based questions.  
2. **Sentiment Analysis**: Analyze the sentiment (positive, negative, or neutral) of a given text.  
3. **Video Analysis (Placeholder)**: Framework for adding video-based features like facial sentiment analysis.  

The modular design and modern folder structure make this template highly extensible and easy to maintain, serving as a foundation for more complex Gradio-based chatbot applications.

---

## **Features**

- **Context-Based Q&A**: Uses a pre-trained question-answering model to answer questions based on uploaded documents.  
- **Sentiment Analysis**: Employs a sentiment analysis pipeline to determine the emotional tone of a given text.  
- **Video Analysis (Placeholder)**: Placeholder for future video-based features, such as emotion recognition.  
- **Tabbed Interface**: Organized UI using Gradio's tabbed design for seamless navigation.  

---

## **Folder Structure**

```plaintext
chatbot_project/
│
├── app/
│   ├── __init__.py            # Package initialization
│   ├── main.py                # Main Gradio app
│   ├── handlers/              # Business logic for handlers
│   │   ├── __init__.py
│   │   ├── document_handler.py # Q&A functionality
│   │   ├── sentiment_handler.py # Sentiment analysis
│   │   ├── video_handler.py    # Video processing
│   │
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── preprocessing.py    # Text preprocessing
│       ├── sentiment_model.py  # Sentiment analysis helper
│       └── question_model.py   # Q&A model helper
│
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── test_document_handler.py # Tests for Q&A
│   ├── test_sentiment_handler.py # Tests for sentiment analysis
│   ├── test_video_handler.py    # Tests for video processing
│   └── test_preprocessing.py    # Tests for preprocessing utils
│
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
└── .gitignore                 # Files to ignore in version control

```
---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/chatbot_project.git
cd chatbot_project
```


### **2. Install Dependencies**
Ensure Python 3.8 or later is installed. Then run:

(make sure to create a venv and activate it by .\chatbot\scripts\activate or source chatbot/bin/activate and add the path of repo to pythonpaths)

```bash
pip install -r requirements.txt
```
### **3. Run the Application**
```bash
python app/main.py
```
This will launch the Gradio interface in your browser.

### **4. Run Tests**
To validate the application’s functionality, use:

```bash
pytest tests/
```


# Note: You are free to use this as a base for your chatbot project for any academic purposes.