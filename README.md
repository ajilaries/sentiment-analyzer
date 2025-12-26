<<<<<<< HEAD
# Sentiment Analyzer

A simple web application built with Flask that analyzes the sentiment of user-inputted text using TextBlob. It classifies text as Positive 😊, Negative 😠, or Neutral 😐.

## Features

- Real-time sentiment analysis
- Clean, responsive web interface
- Easy to deploy and run

## UI Overview

The interface consists of:

- A centered container with a title "Sentiment Analyzer"
- An input field for entering text
- An "Analyze" button
- Results section displaying the original text and sentiment (shown after submission)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sentiment-analyzer
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`

## Usage

- Enter any text in the input field
- Click "Analyze" to get the sentiment result
- Results are displayed below the form

## Technologies Used

- Flask (Python web framework)
- TextBlob (NLP library for sentiment analysis)
- HTML/CSS (Frontend)

## Deployment

To deploy this app live on Render:

1. Sign up for a Render account at https://render.com
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure the service:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy the service
6. Your app will be live at the provided URL

## License

MIT License
=======
# sentiment-analyzer
Real-time sentiment analysis web app using Python, Flask, and NLP to classify text as positive, negative, or neutral.
>>>>>>> origin/main
