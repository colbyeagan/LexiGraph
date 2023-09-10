import base64
import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, url_for, request, Response
from matplotlib.font_manager import FontProperties
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO, BytesIO
from datetime import datetime, timedelta

app = Flask(__name__)

custom_font_path = 'OpenDyslexic3-Regular.ttf'
custom_font = FontProperties(fname=custom_font_path)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def create_plot_standard(tickerSymbol, df):
    # Create a time series line chart
    font_sizing = 15
    label_sizing = 30
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    plt.plot(df.index, df['Open'], linestyle='-', color='b', label='Price')
    plt.xlabel('Date', labelpad=20, fontproperties=custom_font, fontsize=label_sizing)
    plt.ylabel('Value', labelpad=20, fontproperties=custom_font, fontsize=label_sizing)
    plt.title(f'{tickerSymbol.upper()} Chart', fontproperties=custom_font, fontsize=label_sizing)
    plt.grid(True)
    plt.legend([(tickerSymbol.upper())], prop=custom_font, fontsize=font_sizing)
    plt.tight_layout()
    plt.xticks(fontproperties=custom_font, fontsize=font_sizing)
    plt.yticks(fontproperties=custom_font, fontsize=font_sizing)
        
    return plt

def create_plot(tickerSymbol):
    end_date = datetime.strptime('2018-03-27', '%Y-%m-%d')
    start_date = end_date - timedelta(days=91)
    url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{tickerSymbol.upper()}.csv?collapse=none&start_date={start_date}&end_date={end_date}&api_key=tMexE-dhnFFSApsTQVgz"
    response = requests.get(url)

    if response.status_code == 200:
        # Use Pandas to read the CSV data from the response and create a DataFrame
        df = pd.read_csv(StringIO(response.text))
        # Convert the 'Date' column to a datetime data type
        df['Date'] = pd.to_datetime(df['Date'])
        # Set the 'Date' column as the index
        df.set_index('Date', inplace=True)
        
        # Creates the plt
        plt = create_plot_standard(tickerSymbol, df)

        # Put chart in img
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)

        image_data_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')

        # Display the chart
        return render_template('about.html', image_data=image_data_base64)
    else:
        return 'API request failed with status code:', response.status_code

#route to fetch time series analysis graph
@app.route('/submit', methods=['POST'])
def fetch_data():
    stockId = request.form.get('stockname')
    return create_plot(stockId)


if __name__ == "__main__":
    app.run(debug=True)
