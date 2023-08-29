import requests

class CoinMarket:
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '267ecf2c-5c1f-42a8-88bd-e75445541024'
        }
        
        

    def load_top_25(self):
        crypto_list = []
        parameters = {
                    'start':'1',
                    'limit':'25',
                    'convert':'USD'
                }
        
        try:
            req = requests.get(self.url, params=parameters, headers=self.headers)
            res = req.json()
            data = res['data']
            for coin in data:
                name = coin['name']
                symbol = coin['symbol']
                price = coin['quote']['USD']['price']
                volume_24h = coin['quote']['USD']['volume_24h']
                volume_change_24hr = coin['quote']['USD']['volume_change_24h']
                percent_change_1h = coin['quote']['USD']['percent_change_1h']
                percent_change_24h = coin['quote']['USD']['percent_change_24h']
                market_cap = coin['quote']['USD']['market_cap']

                crypto_data = {
                    'name': name,
                    'symbol': symbol,
                    'price': round(price, 2),
                    'vol_24h': round(volume_24h, 2),
                    'vol_24h_change': round(volume_change_24hr, 2),
                    'percent_change_1h': round(percent_change_1h, 2),
                    'percent_change_24h': round(percent_change_24h, 2),
                    'market_cap': round(market_cap, 2)
                }

                crypto_list.append(crypto_data)
                
            return crypto_list
        
        except Exception as e:
            return e
    
    
    def load_top_100(self):
        crypto_list = []
        parameters = {
                    'start':'1',
                    'limit':'100',
                    'convert':'USD'
        }

        try:
            req = requests.get(self.url, params=parameters, headers=self.headers)
            res = req.json()
            data = res['data']
            for coin in data:
                name = coin['name']
                symbol = coin['symbol']
                price = coin['quote']['USD']['price']
                volume_24h = coin['quote']['USD']['volume_24h']
                volume_change_24hr = coin['quote']['USD']['volume_change_24h']
                percent_change_1h = coin['quote']['USD']['percent_change_1h']
                percent_change_24h = coin['quote']['USD']['percent_change_24h']
                market_cap = coin['quote']['USD']['market_cap']  
                crypto_data = {
                    'name': name,
                    'symbol': symbol,
                    'price': round(price, 2),
                    'vol_24h': round(volume_24h, 2),
                    'vol_24h_change': round(volume_change_24hr, 2),
                    'percent_change_1h': round(percent_change_1h, 2),
                    'percent_change_24h': round(percent_change_24h, 2),
                    'market_cap': round(market_cap, 2)
                }

                crypto_list.append(crypto_data) 
            return crypto_list   
        except Exception as e:
            return e


