from flask import Flask, render_template, url_for, request
from gtts import gTTS
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    stockId = request.form.get('stockname')
    return f'tickerID: {stockId}'



if __name__ == "__main__":
    app.run(debug=True)

# When it submits, it goes to about page
# On about page, have the graph on the about page
# And then have options for the user to select which we then have to send to the backend and make another API call


