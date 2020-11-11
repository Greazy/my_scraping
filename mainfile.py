from bs4 import BeautifulSoup


from lxml import html
import requests
import json
'''
usr = 'admin'
pwd = 12345
  
url = 'http://testing-ground.scraping.pro/login?mode=login'
sess = requests.Session()
  
resp = sess.post(url, data={'usr': usr, 'pwd': pwd})
  
print(resp.text)
'''


URL = "http://testing-ground.scraping.pro/blocks"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44'}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')

	items = soup.find_all('div',class_='prod2')
	items1 = soup.find_all('div', class_='prod1')
	info = []

	def get_name(items,item):
		nameof = item.find('div', class_='name').get_text()
		return nameof

	def get_description(items,item):
		description = item.find('span', style='float: left')

		if description != None:
			description.div.decompose()
			xx = description.get_text()
			return xx
		else:
			description = item.find('span', style='float: left')
			return  description

	def get_price(items,item):
		priceof = item.find('span', style="float: right")
		if priceof != None:
			return priceof.get_text().replace('discount 7%','')
		else:
			pass

	def get_discount(items,item):
		discountof = item.find('div', class_='disc')
		if discountof != None:
			return discountof.get_text().replace('discount','')
		else:
			return '0%'
	
	def get_best_price(items,item):
		best_price = item.find('span', class_='best')
		if best_price:
			return True
		else:
			return False


	for item1, item in enumerate(items):
		if item1 == 3:
			break
		else:
			info.append({
				'name': get_name(items, item),
				'description': get_description(items, item),
				'best price': get_best_price(items, item),
				'price': get_price(items, item),
				'discount': get_discount(items, item),
				})
	for item1, item in enumerate(items1):
			if item1 == 3:
				break
			else:
				info.append({
					'name': get_name(items, item),
					'description': get_description(items, item),
					'best price': get_best_price(items, item),
					'price': get_price(items, item),
					'discount': get_discount(items, item),
					})

	info1 = []
	nice = soup.find_all('div', id='case2')
	#it = soup.find_all('div',class_='left')
	#it1 = soup.find_all('div', class_='right')
	for i in nice:
		names = i.find_all('div', class_='name')
		for i in names:
			print(i.get_text())
	print()
	for i in nice:
		ss = i.find_all('div', class_='right')
		ss1 = i.find_all('div', class_='left')

		for y in ss:
			#print(y.find('div', class_='price2').get_text().replace('discount 7%',''))
			#print(y.find('div', class_='price2').find_next().find_next().find_next().get_text())
			
			disc = y.find('div', class_='disc') 
			if disc:
				print(disc.get_text().replace('discount','').replace(' ',''))
			else:
				print("0%")

			price11 = y.find('div', class_='best')
			print(price11)
			
			#best_price = y.find('div', class_='best')
			'''
			if best_price:
				print(True)
			else:
				print(False)
				'''
			
		for i in ss1:
			x1 = i.find('div', class_='prod2').find_next().find_next().find_next().find_next().find_next()
			x1.div.decompose()
			print(x1.get_text())

			#print(i.find('div', class_='prod2'))
			#print(i.find('div', class_='name').get_text())

	

	'''
	with open("data_file.json", "w") as write_file:
		json.dump(info, write_file)
		json_string = json.dumps(info)
	print(json_string)
	'''

def parse():
	html = get_html(URL)
	get_content(html.text)



parse()
