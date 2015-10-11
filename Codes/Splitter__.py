import csv
import re


myfile = open('./errors', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(rm)









f1 = open('yana_1_iitk.xlsx', 'r')
f2 = open('yana_tab_removed.xlsx', 'w')
for line in f1:
    f2.write(re.sub('(\t){2,}', '\t',line));
f1.close()
f2.close()




