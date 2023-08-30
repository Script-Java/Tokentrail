from flask import Flask, render_template, redirect, url_for, request
from scrape import CoinMarket
from urllib.parse import unquote

coinmarket = CoinMarket()

app = Flask(__name__)
app.config['secret_key'] = 'wbqeugofbdasl3jk@b4308597jwhbdfksjdb092125sdf'

@app.route('/')
def index():
    
    return render_template('index.html', top_25 = coinmarket.load_top_25())

@app.route('/assets')
def assets():
        
    return render_template('assets.html', top_100=coinmarket.load_top_100())

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        search_input = request.form.get('search_input')
        output_data = coinmarket.search_crypto(str(search_input))
        return render_template('search.html', output=output_data)
    except KeyError:
        return render_template('error.html')
    
@app.route('/search/<token_symbol>', methods=['GET', 'POST'])
def search_symbol(token_symbol):
    try:
        input_str = str(token_symbol)
        output = unquote(input_str).lower()
        search_input = output.replace(' ', '-')
        print(search_input)
        output_data = coinmarket.search_crypto(search_input)
        if output_data is None:
            raise Exception(f'No data was found for {search_input}')
        return render_template('search.html', output=output_data)
    
    except KeyError:
        return render_template('error.html')
    
@app.route('/thankyou')
def feedback_submit():
    return render_template('thankyou.html')

@app.route('/feedback')
def contact():
    
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)


