from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    text = ""

    if request.method == "POST":
        text = request.form["message"]
        result = sentiment_pipeline(text)[0]
        label = result['label']

        if label == 'LABEL_2':
            sentiment = "Positive 😊"
        elif label == 'LABEL_0':
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

    return render_template("index.html", sentiment=sentiment, text=text)

if __name__ == "__main__":
    app.run(debug=True)
