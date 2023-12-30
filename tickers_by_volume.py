import requests
from bs4 import BeautifulSoup
 
 #거래량 순으로 티커 불러오기
url = "https://coinmarketcap.com/exchanges/upbit/"
res = requests.get(url)
 
bs = BeautifulSoup(res.text, 'html.parser')
selector = "tbody > tr > td > div > a"
columns = bs.select(selector)
 
ticker_list = [x.text.strip().replace('/', '-') for x in columns]
print(ticker_list)