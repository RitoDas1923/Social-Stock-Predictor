# Create a flask app
from flask import Flask, render_template, request
from plot_AAPL import plot
import os

app = Flask(__name__, static_url_path='/static')
# Create a route


@app.route('/')
def index():
    if(os.path.exists('./static/plot.jpg')):
        os.remove('./static/plot.jpg')
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot_route():
    start_date = request.form['start']
    end_date = request.form['end']
    plot('AAPL', start_date, end_date)
    return render_template('plot.html')


if __name__ == '__main__':
    app.run(debug=True)
    