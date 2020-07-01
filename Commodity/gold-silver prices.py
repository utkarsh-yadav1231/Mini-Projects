from bs4 import BeautifulSoup
import urllib.request
import time

def get_rate(item):
	url = "http://m.moneycontrol.com/commodity/%s-price.html" % item
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,}
	
	request = urllib.request.Request(url, None, headers)
	response = urllib.request.urlopen(request)
	data = response.read()
	soup = BeautifulSoup(data, 'html.parser')

	data2 = soup.find_all('div', {'class':'acctab2'})[0].contents
	rate = float(data2[1].contents[0].replace(',', ''))
	
	return rate

	
print("\n Gold   ( 10 grams )  Price currently  : {}".format(float(get_rate('gold'))))
print("\n Silver (1 kilo-gram) Price currently  : {}".format(float(get_rate('silver'))))
