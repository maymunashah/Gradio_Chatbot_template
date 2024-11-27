from app.handlers.document_handler import handle_document

def test_handle_document():
    # Create a dummy text file
    file_path = "tests/dummy_doc.txt"
    with open(file_path, "w") as f:
        f.write("This is a test document containing example text.")

    # Test handler
    with open(file_path, "r") as f:
        response = handle_document(f)

    # Assert expected behavior
    assert "Q: What is the main idea" in response
    assert "A: " in response
