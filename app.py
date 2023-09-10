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


@app.route('/')
def index():
    return render_template('index.html')


"""@app.route('/submit', methods=['POST'])
def submit_form():
    stockId = request.form.get('stockname')"""

#route to fetch time series analysis graph
@app.route('/submit', methods=['POST'])
def fetch_data():

    end_date = datetime.strptime('2018-03-27', '%Y-%m-%d')
    start_date = end_date - timedelta(days=91)
    stockId = request.form.get('stockname')
<<<<<<< HEAD
    return f'tickerID: {stockId}'
=======
    url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{stockId.upper()}.csv?collapse=none&start_date={start_date}&end_date={end_date}&api_key=tMexE-dhnFFSApsTQVgz"
    response = requests.get(url)

    if response.status_code == 200:
        font_sizing = 15
        label_sizing = 30
>>>>>>> 61203b2e9e0509411230df91bcb3999451f8dc1a

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
        plt.title(f'{stockId.upper()} Chart', fontproperties=custom_font, fontsize=label_sizing)
        plt.grid(True)
        plt.legend([(stockId.upper())], prop=custom_font, fontsize=font_sizing)
        plt.tight_layout()
        plt.xticks(fontproperties=custom_font, fontsize=font_sizing)
        plt.yticks(fontproperties=custom_font, fontsize=font_sizing)
        

        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        # Display the chart
        return Response(img_buffer.read(), content_type='image/png')
    else:
        return 'API request failed with status code:', response.status_code

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)

# When it submits, it goes to about page
# On about page, have the graph on the about page
# And then have options for the user to select which we then have to send to the backend and make another API call



custom_font_path = 'OpenDyslexic3-Regular.ttf'
custom_font = FontProperties(fname=custom_font_path)

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




"""tickerName = stockId

    end_date = datetime.strptime('2018-03-27', '%Y-%m-%d')
    start_date = end_date - timedelta(days=91)
    url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{tickerName}.csv?collapse=none&start_date={start_date}&end_date={end_date}&api_key=tMexE-dhnFFSApsTQVgz"

    response = requests.get(url)

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
        
        # Display the chart
        plt.show()
    else:
        print("API request failed with status code:", response.status_code)
"""

    ####################################### CHARTING ###################################





