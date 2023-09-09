from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    stockId = request.form.get('stockname')
<<<<<<< HEAD

    return f'tickerID: {stockId}'

=======
    return f''
}
>>>>>>> cc6004ea94026ff7af90af5991dd229616481e8b

if __name__ == "__main__":
    app.run(debug=True)


