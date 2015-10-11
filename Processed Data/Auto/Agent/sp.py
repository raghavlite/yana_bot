from lxml import html
import requests

df = DataFrame(columns=('Station', 'Code'))

page = requests.get('https://www.cleartrip.com/trains/stations/list')
tree = html.fromstring(page.text)
buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
for i in range(1000):
	df.loc[i] = [buyers2[i], buyers[i]]


page = requests.get('https://www.cleartrip.com/trains/stations/list?page=2')
tree = html.fromstring(page.text)
buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
for i in range(1000):
	df.loc[1000+i] = [buyers2[i], buyers[i]]


page = requests.get('https://www.cleartrip.com/trains/stations/list?page=3')
tree = html.fromstring(page.text)
buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
for i in range(1000):
	df.loc[2000+i] = [buyers2[i], buyers[i]]


page = requests.get('https://www.cleartrip.com/trains/stations/list?page=4')
tree = html.fromstring(page.text)
buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
for i in range(1000):
	df.loc[3000+i] = [buyers2[i], buyers[i]]


page = requests.get('https://www.cleartrip.com/trains/stations/list?page=5')
tree = html.fromstring(page.text)
buyers = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[1]/text()')
buyers2 = tree.xpath('//*[@id="ContentFrame"]/div[2]/div/table/tbody/tr/td[2]/a/text()')
for i in range(465):
	df.loc[4000+i] = [buyers2[i], buyers[i]]




















