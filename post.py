import requests

from bs4 import BeautifulSoup



def general_inf():
    
    url_1 = 'https://bitstat.top/fear_greed.php'

    response_1 = requests.get(url=url_1)

    bs_1 = BeautifulSoup(response_1.text, 'lxml')

    inf = bs_1.find_all('a', 'dark')

    inf = inf[:4]

    domination = inf[0].text
    capitalization = inf[1].text
    volume = inf[2].text
    fear = inf[3].text

    #return f'Капитализация рынка: {capitalization}\nИндекс доминирования BTC: {domination}\nИндекс страха и жадности: {fear}\nОбъем за 24 часа: {volume}'

    url_btc = 'https://cryptorank.io/ru/price/bitcoin'

    response_2 = requests.get(url=url_btc)

    data = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()

    btc = data['price'][:8]


    url_usd = 'https://www.banki.ru/products/currency/usd/'

    response_3 = requests.get(url_usd)
    

    bs_3 = BeautifulSoup(response_3.text, 'lxml')
    
    rubusd = bs_3.find('div', 'Text__sc-j452t5-0 bCCQWi').text # курс рубля к доллару

    url_eur = 'https://www.banki.ru/products/currency/eur/'

    response_4 = requests.get(url_eur)
    

    bs_4 = BeautifulSoup(response_4.text, 'lxml')

    rubeur = bs_4.find('div', 'Text__sc-j452t5-0 bCCQWi').text #курс рубля к евро

    url_spx = 'https://take-profit.org/stocks-market-rates/sp500/'

    response_5 = requests.get(url=url_spx)
    

    bs_5 = BeautifulSoup(response_5.text, 'lxml')

    spx = bs_5.find('div', 'quotation-value').text[:6] #котировка spx
    
    url_gold = 'https://take-profit.org/commodities-market-rates/gold/'

    response_6 = requests.get(url_gold)

    bs_6 = BeautifulSoup(response_6.text, 'lxml')

    gold = bs_6.find('div', 'quotation-value').text #курс золота


    url_oil = 'https://take-profit.org/commodities-market-rates/oil/'

    response_7 = requests.get(url_oil)

    bs_7 = BeautifulSoup(response_7.text, 'lxml')

    oil = bs_7.find('div', 'quotation-value').text
    

    return f'Капитализация рынка: {capitalization}\nИндекс доминирования BTC: {domination}\nИндекс страха и жадности: {fear}\nОбъем за 24 часа: {volume}\n\nКурсы:\nBitcoin - {btc}$\nS&P 500 - {spx}$\nUSD/RUB - {rubusd}\nEUR/USD - {rubeur}\nЗолото - {gold}$\nOil Brent - {oil}$'


def cap(n):

    url = 'https://www.coingecko.com/ru'

    response = requests.get(url=url)
 
    bs = BeautifulSoup(response.text, 'lxml')

    capit = bs.find_all('span', 'tw-text-blue-500')
    dom = bs.find_all('a', 'tw-text-blue-500')
    
    if n == 'c':
        return capit[0].text
    if n == 'v':
        return capit[1].text
    if n == 'd':
        return dom[2].text




def search_binance(para):
     try:
        data = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={para.upper()}").json()
        return data['price']
     except:

            response = requests.get('https://api.mexc.com/api/v3/ticker/24hr')
            price_list = response.json()
            out = ''
            for i in price_list:
                symbol = i['symbol']
                price = i['lastPrice']
                if symbol == para.upper():
                    out = price
            if out != '':
                return out
            else:
                try:
                    price_list = requests.get(f'https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol={para.lower()}').json()
                    return price_list['data'][0]['close']
                except:
                    try:
                        response = requests.get(f'https://api.bitget.com/api/spot/v1/market/ticker?symbol={para.upper()}_SPBL').json()
                        price = response['data']['close']
                        return price
                    except:
                        return 'Что-то пошло не так...'



def first_inf(code):
    url_1 = 'https://bitstat.top/fear_greed.php'

    response_1 = requests.get(url=url_1)

    bs_1 = BeautifulSoup(response_1.text, 'lxml')

    inf = bs_1.find_all('a', 'dark')

    inf = inf[:4]

    domination = inf[0].text
    capitalization = inf[1].text
    volume = inf[2].text
    fear = inf[3].text

    url_2 = 'https://cryptorank.io/'

    response_2 = requests.get(url=url_2)

    bs_2 = BeautifulSoup(response_2.text, 'lxml')

    proc = bs_2.find_all('span', 'sc-130f0f3b-0 sc-3b6c6a9d-0 dDBEoV')

    if code == 'd':
        return domination
    if code == 'c':
        return f'{capitalization} ({proc[0].text})'
    if code == 'v':
        return f'{volume} ({proc[1].text})'
    if code == 'f':
        return fear


    
def btc_price():

    data = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()

    btc = data['price'][:8]

    return btc

def usd_price():
    url_usd = 'https://www.banki.ru/products/currency/usd/'

    response_3 = requests.get(url_usd)
    

    bs_3 = BeautifulSoup(response_3.text, 'lxml')
    
    rubusd = bs_3.find('div', 'Text__sc-j452t5-0 bCCQWi').text # курс рубля к доллару

    return rubusd

def eur_price():
    url_eur = 'https://www.banki.ru/products/currency/eur/'

    response_4 = requests.get(url_eur)
    
    bs_4 = BeautifulSoup(response_4.text, 'lxml')

    rubeur = bs_4.find('div', 'Text__sc-j452t5-0 bCCQWi').text #курс рубля к евро

    return rubeur

def spx_price():
    url_spx = 'https://take-profit.org/stocks-market-rates/sp500/'

    response_5 = requests.get(url=url_spx)
    

    bs_5 = BeautifulSoup(response_5.text, 'lxml')

    spx = bs_5.find('div', 'quotation-value').text[:6] #котировка spx

    return spx

def gold_price():
    url_gold = 'https://take-profit.org/commodities-market-rates/gold/'

    response_6 = requests.get(url_gold)

    bs_6 = BeautifulSoup(response_6.text, 'lxml')

    gold = bs_6.find('div', 'quotation-value').text #курс золота

    return gold

def oil_price():
    url_oil = 'https://take-profit.org/commodities-market-rates/oil/'

    response_7 = requests.get(url_oil)

    bs_7 = BeautifulSoup(response_7.text, 'lxml')

    oil = bs_7.find('div', 'quotation-value').text
    
    return oil


def dxy_price():

    url = 'https://www.cnbc.com/quotes/.DXY'

    response = requests.get(url=url)
   

    bs = BeautifulSoup(response.text, 'lxml')

    dxy = bs.find('span', 'QuoteStrip-lastPrice').text

    return dxy

    




def dow():
    url = 'https://www.cnbc.com/quotes/.DJI'

    response = requests.get(url=url)

    bs = BeautifulSoup(response.text, 'lxml')

    dow_j = bs.find('span', 'QuoteStrip-lastPrice').text

    return dow_j



def nasq():
    url = 'https://www.marketwatch.com/investing/index/ndx'

    response = requests.get(url=url)

    bs = BeautifulSoup(response.text, 'lxml')

    nas = bs.find('h2', 'intraday__price').text
    
    return nas
   

def test():

    url = 'https://www.coingecko.com/ru/global-charts#:~:text=%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B8%20%D1%80%D1%8B%D0%BD%D0%BE%D1%87%D0%BD%D0%BE%D0%B9%20%D0%BA%D0%B0%D0%BF%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82,%D0%B8%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%203.98%25%20%D0%B3%D0%BE%D0%B4%20%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4.'

    response = requests.get(url=url)

    bs = BeautifulSoup(response.text, 'lxml')

    print(bs.find('span', 'tw-text-blue-500').text)
















    










