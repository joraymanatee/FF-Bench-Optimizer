from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

insider_trading_data = pd.read_csv('guru_insider_trading/insider_trading_table_2020_12_27_buy.csv')

price_change = insider_trading_data['\n        Price Change Since Insider Trade (%)\n        ']
price_change = [float(p[0:len(p)-1].replace(',','')) for p in price_change]
insider_trading_data['\n        Price Change Since Insider Trade (%)\n        '] = price_change

insider_trading_data = insider_trading_data[insider_trading_data['\n        Price Change Since Insider Trade (%)\n        '] < 1000]

price_change = insider_trading_data['\n        Price Change Since Insider Trade (%)\n        ']
dates = insider_trading_data['\n        Date\n        ']
ymd = "%Y-%m-%d"
dates = [datetime.strptime(d.strip(), ymd).date() for d in dates]


plt.plot(dates, price_change, 'bo')
plt.show()


import requests
from bs4 import BeautifulSoup

"""URL = "https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php" 
r = requests.get(URL) 
#print(r.content)

soup = BeautifulSoup(r.content, 'html.parser') 
# print(soup)
table = soup.find('div', class_='player-cell player-cell__td')
#rows = table.find('tbody').find_all('tr')


#print(soup.prettify)

res = soup.find(class_= 'inner')
#print(res)
rankings = res.find(class_= 'rankings-table__wrapper')
#print(rankings)

#table = soup.find('table', id='ranking-table')
#print(table)

res=soup.find("div", id = 'main-container')
#print(res.prettify)
res2 = res.find("div", class_="inner")
#res2 = res.find("")
#print(res2.prettify)

content_sections = res2.find('section', class_='rankings-table rankings-table__container mobile-table sticky-table')
print(content_sections"""