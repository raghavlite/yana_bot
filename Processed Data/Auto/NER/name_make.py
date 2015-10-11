import pandas as pd
import math
df = pd.read_csv('./names_indian.csv');



ll = df['FN']
ll = ll.append(df['MN'])
ll = ll.append(df['LN'])

ll = ll.append(df['HFN'])
ll = ll.append(df['HMN'])
ll = ll.append(df['HLN'])



ll = ll.tolist();


ll = set(ll);

ll = list(ll);

pp = [];
x=float('nan')
for kk in ll:
	if(type(kk)==float):
		continue;
	# print typ
	if(len(kk)>2):
		pp.append(kk.lower());
'end for'




df = pd.DataFrame(pp)


# import pickle

# pickle.dump(pp, './names_list');


# itemlist = pickle.load('./names_list');








