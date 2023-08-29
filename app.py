from flask import Flask, render_template, redirect, url_for, request
from scrape import CoinMarket

coinmarket = CoinMarket()

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html', top_25 = coinmarket.load_top_25())

@app.route('/assets')
def assets():
        
    return render_template('assets.html', top_100=coinmarket.load_top_100())

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/feedback')
def contact():
    
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)


