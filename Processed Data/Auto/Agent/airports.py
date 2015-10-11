from lxml import html
import requests
from pandas import *

from bs4 import BeautifulSoup




df = DataFrame(columns=('Airport', 'Code'))
# page = requests.get('http://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm')

f = open('./International airport codes IATA 3-letter code for airports - Nations Online Project.html', 'r');


hml = f.read();

soup = BeautifulSoup(hml)
for match in soup.findAll(['a']):
    match.replaceWithChildren()

print soup



tree = html.fromstring(str(soup));


for i in range(5,100):
	# print i;
	buyers = tree.xpath('//*[@id="dummybodyid"]/table['+str(i)+']/tbody/tr/td[1]/text()');
	buyers2 = tree.xpath('//*[@id="dummybodyid"]/table['+str(i)+']/tbody/tr/td[3]/text()')
	
	if (len(buyers2) > 5):
		if(buyers[0]=='\n'):
			del buyers[0]
		if(buyers2[0]=='\n'):
			del buyers2[0]
		print len(buyers) , len(buyers2);
		print buyers , buyers2;
		# del buyers2[0];
		# print buyers;
		df2 = DataFrame(zip(buyers, buyers2), columns=('Airport', 'Code'));
		df = df.append(df2, ignore_index=True);
	'end if'
'end for'


df.to_csv('./airports.csv', sep='\t')



