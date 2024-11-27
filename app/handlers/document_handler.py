from app.utils.question_model import load_qa_model, answer_question

def handle_document(doc_file):
    try:
        # Load the document content
        with open(doc_file.name, "r") as file:
            content = file.read()
        
        # Initialize the QA model
        model, tokenizer = load_qa_model()
        
        # Placeholder question
        question = "What is the main idea of this document?"
        answer = answer_question(model, tokenizer, question, content)
        
        return f"Q: {question}\nA: {answer}"
    except Exception as e:
        return f"Error processing document: {str(e)}"
