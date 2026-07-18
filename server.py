"""
Flask web server application for emotion detection.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Route that receives 'textToAnalyze' as a query parameter,
    analyzes its emotion, and returns the formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Formatting the string as requested by typical requirements
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Route that renders the main application page.
    For this assignment, we might just return a simple greeting or the index.html.
    """
    return "Emotion Detection Application is running. Send a GET to /emotionDetector."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
