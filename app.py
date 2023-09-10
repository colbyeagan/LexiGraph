from flask import Flask, render_template, url_for, request
import io
import base64
from gtts import gTTS
import os
from matplotlib.font_manager import FontProperties
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from datetime import datetime, timedelta
from flask import render_template_string

def create_plot(ticker):
    custom_font_path = 'OpenDyslexic3-Regular.ttf'
    custom_font = FontProperties(fname=custom_font_path)

    def text_to_speech(text):
        # Initialize gTTS with the text to convert
        speech = gTTS(text)

        # Save the audio file to a temporary file
        speech_file = 'speech.mp3'
        speech.save(speech_file)

        # Play the audio file
        os.system('afplay ' + speech_file)


    dyslexia_friendly_settings = {
        'font.family': 'Arial',
        'font.size': 14,
        'font.style': 'normal',  
        'axes.labelsize': 12,    
        'axes.titlesize': 16,    
        'axes.titleweight': 'bold',
        'axes.titlepad': 20,     
        'axes.labelweight': 'bold',
        'xtick.labelsize': 12,   
        'ytick.labelsize': 12,   
        'legend.fontsize': 12,   
        'lines.linewidth': 2,    
        'lines.markersize': 8,   
        'legend.title_fontsize': 12,
        'axes.labelcolor': 'black',  
        'text.color': 'black',  
        'axes.edgecolor': 'black',  
        'axes.facecolor': 'white',  
        'axes.grid': True,      
        'axes.grid.axis': 'both',  
        'grid.color': 'gray',   
        'grid.linestyle': '--',  
        'grid.linewidth': 0.5   
    }

    def get_date_range(time_range):
        end_date = datetime.strptime('2018-03-27', '%Y-%m-%d')
        start_date = end_date - timedelta(days=91)
        time_range_ret = "Three months"
        
        return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), time_range_ret


    tickerName = ticker
    tickerName = tickerName.upper()
    # Make the API call and get the response
    #url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{tickerName}.csv"
    start_date, end_date, time_range = get_date_range(time_range)
    #url = "https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.csv?start_date=2023-07-10&end_date=2023-09-05"
    url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{tickerName}.csv?collapse=none&start_date={start_date}&end_date={end_date}&api_key=tMexE-dhnFFSApsTQVgz"
    print(url)

    response = requests.get(url)

    # Get user input for time range


    # Check if the request was successful
    if response.status_code == 200:
        font_sizing = 15
        label_sizing = 30

        # Use Pandas to read the CSV data from the response and create a DataFrame
        df = pd.read_csv(StringIO(response.text))
        
        # Convert the 'Date' column to a datetime data type
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Set the 'Date' column as the index
        df.set_index('Date', inplace=True)
        
        # Create a time series line chart
        plt.rcParams.update(dyslexia_friendly_settings)
        plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
        plt.plot(df.index, df['Open'], linestyle='-', color='b', label='Price')
        plt.xlabel('Date', labelpad=20, fontproperties=custom_font, fontsize=label_sizing)
        plt.ylabel('Value', labelpad=20, fontproperties=custom_font, fontsize=label_sizing)
        plt.title(f'{tickerName} Chart', fontproperties=custom_font, fontsize=label_sizing)
        plt.grid(True)
        plt.legend([(tickerName)], prop=custom_font, fontsize=font_sizing)
        plt.tight_layout()
        plt.xticks(fontproperties=custom_font, fontsize=font_sizing)
        plt.yticks(fontproperties=custom_font, fontsize=font_sizing)
    else:
        print("API request failed with status code:", response.status_code)


def plot_to_img(ticker):
    # Create plot
    create_plot(ticker)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Convert BytesIO object to base64 string
    img_b64 = base64.b64encode(img.getvalue()).decode()

    return img_b64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    stockId = request.form.get('stockname')

    # Convert plot to image
    img_b64 = plot_to_img(stockId)

    # Render HTML with base64 image
    html = f'<img src="data:image/png;base64,{img_b64}" class="blog-image">'
    return render_template_string(html)
    #return f'tickerID: {stockId}'


if __name__ == "__main__":
    app.run(debug=True)