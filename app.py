from flask import Flask , render_template , request     
from textblob import TextBlob
app = Flask ( __name__ )

@app.route ( '/' , methods = [ ' GET ' , ' POST ' ] )
def index ():   
    sentiment-""
    text= ""

    if request.method == ' POST ' :
        text=request.form["message"]
        analysis = TextBlob ( text )

        if analysis.sentiment.polarity > 0 :
            sentiment = " Positive "
        elif analysis.sentiment.polarity < 0 :
            sentiment = " Negative "
        else :
            sentiment = " Neutral "     
    return render_template ( ' index.html ' , sentiment = sentiment , text = text )

if __name__ == ' __main__ ' :
    app.run ( debug = True )