# Emotion Detection Application

## Project Description

The Emotion Detection Application is a Python-based web application that uses the IBM Watson NLP Emotion Prediction service to analyze the emotions expressed in a given text. Users can enter text through a web interface, and the application predicts the intensity of the following emotions:

- Anger
- Disgust
- Fear
- Joy
- Sadness

The application identifies the dominant emotion and displays the results in a user-friendly format. It is developed using Flask for the web interface and includes proper error handling, unit testing, and static code analysis.

---

## Features

- Detects emotions from user-provided text
- Predicts five emotions:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Identifies the dominant emotion
- Flask-based web interface
- Handles invalid or blank input
- Includes unit tests
- Follows Python coding standards using Pylint

---

## Project Structure

```
EmotionDetectionProject/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── static/
│
├── server.py
├── test_emotion_detection.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3
- Flask
- IBM Watson NLP Emotion Prediction API
- Requests
- unittest
- Pylint
- HTML
- CSS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/emotion-detection-app.git
```

Navigate to the project folder:

```bash
cd emotion-detection-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python server.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Running Unit Tests

```bash
python -m unittest test_emotion_detection.py
```

---

## Running Static Code Analysis

```bash
pylint server.py
```

---

## Expected Output

Example input:

```
I am very happy today.
```

Example output:

```
The given text has the following emotions:
anger: 0.01,
disgust: 0.00,
fear: 0.02,
joy: 0.96,
sadness: 0.01.

The dominant emotion is joy.
```

---

## Author

**Shreyas Santi**

Computer Science and Engineering (AI & ML)

---

## License

This project is developed for educational purposes as part of the IBM Skills Network Emotion Detection assignment.
