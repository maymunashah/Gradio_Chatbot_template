from transformers import pipeline

def load_qa_model():
    model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return model, None

def answer_question(model, tokenizer, question, context):
    return model(question=question, context=context)['answer']
