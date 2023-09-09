from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=[POST])
def submit_form() {
    stockId = request.form.get('stockname')
    return f''
}

if __name__ == "__main__":
    app.run(debug=True)


