from app.handlers.video_handler import process_video

def test_process_video():
    # Test with a dummy video path
    dummy_video_path = "tests/dummy_video.mp4"
    
    # Write dummy content to simulate video file
    with open(dummy_video_path, "w") as f:
        f.write("Dummy video content.")

    # Call the handler
    response = process_video(dummy_video_path)

    # Assert placeholder logic
    assert response == "Video processing is under development."
