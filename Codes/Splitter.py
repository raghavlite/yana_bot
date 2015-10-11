import os
from nltk.stem import PorterStemmer
import re
import datetime
import pandas as pd

cols_list = ['NUMBER','NXT','TYPE','MESSAGE','TIME_STAMP','IS_AGENT'];
# cols_list = ['NUMBER','NXT','TYPE','MESSSAGE','TIME_STAMP','IS_AGENT','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'];
df = pd.read_csv('./yana1_f.csv',usecols=cols_list); 



dfc_dict = {};
temp_cols_list = cols_list;
temp_cols_list.remove('MESSAGE');
temp_cols_list.remove('TIME_STAMP');



dfList = df['NUMBER'].tolist()

dfset = set(dfList);

df_list = list(dfset);






global uid;
uid=0; 
global df_chats;
df_chats = pd.DataFrame(columns=('ID', 'CHAT', 'NUMBER'));


def split(temp):

	print temp['NUMBER'].iloc[0];
	global uid;
	global df_chats;
	num = temp['NUMBER'].iloc[0];

	S = '';
	pp = re.sub('[^\d\s\/:]','',temp['TIME_STAMP'].iloc[0]);
	pp = re.search('(\d{1,2})/(\d{1,2})/(\d{4})\s(\d{1,2}):(\d{1,2})',pp);
	# pt = datetime.datetime(2013, 1, 1, 1, 1, 0, 0);
	pt = datetime.datetime(int(float(pp.group(3))), int(float(pp.group(1))), int(float(pp.group(2))), int(float(pp.group(4))), int(float(pp.group(5))), 0, 0);
	

	for idx,row in temp.iterrows():
		print 'msg'
		pp = re.sub('[^\d\s\/:]','',row['TIME_STAMP']);
		pp = re.search('(\d{1,2})/(\d{1,2})/(\d{4})\s(\d{1,2}):(\d{1,2})',pp);
		if(pp!=None):
			ct = datetime.datetime(int(float(pp.group(3))), int(float(pp.group(1))), int(float(pp.group(2))), int(float(pp.group(4))), int(float(pp.group(5))), 0, 0);
			print 'molly',ct,pt,row['IS_AGENT'],row['MESSAGE'];
			td = ct - pt;
			td = divmod(td.days * 86400 + td.seconds, 60)
			print 'td',td;
			if((row['IS_AGENT']!='incoming') & (td[0]<700) ):
				S+='\nAGENT : '+str(row['MESSAGE']);
				pt = ct;
			elif((row['IS_AGENT']!='outgoing') & (td[0]<1500)):
				S+='\nCUSTOMER : '+str(row['MESSAGE']);
				pt = ct;		
			else:	
				# write
				print 'one more'
				df_chats.loc[uid]=[uid,S,num];
				uid+=1;
				if(row['IS_AGENT']=='incoming'):
					S = 'CUSTOMER : '+ row['MESSAGE'];
				else:
					S = 'AGENT : '+row['MESSAGE'];
				pt=ct;
			'end if'
		else:
			print 'OOB';
			S+=row['MESSAGE'];
			break;
		'end if'
	'end for'

	df_chats.loc[uid]=[uid,S,num];
	uid+=1;
	S='';




'end def'	






idx=0;
for num in df_list:
	temp = df[df['NUMBER'] == num];
	# # print num,temp.shape;
	# # try:
	# # 	print temp['NUMBER'][0]
	# # except:
	# # 	break;
	split(temp);
	# print temp;
	# idx+=1;
	# if(idx==5):
	# 	break;
'end'





df_chats.to_csv('./Chats_yana.csv');


temp_cols_list = ['ID', 'CHAT', 'NUMBER'];

# for col_name in temp_cols_list:
#     clist = pd.unique(df_chats[col_name])    # no of unique entries in this column
#     df_clist = pd.DataFrame(clist)      # dataframe with 0 to n-1 entries and also the correesponding values
#     dfc_dict[col_name] = df_clist       #  dictionary can work with both column names and also the index numbers
#     numc = clist.size                   # here in the last two lines we only print out the number of unique entries 
#     print col_name, numc  


for col_name in temp_cols_list:
    print ''
    print df_chats.groupby(col_name).size()   # syntax for printing individual entries for each column



stemmer=PorterStemmer()
def p_process(S):

	S = re.sub(r'[^A-Za-z0-9]',r' ',S);
	S = S.split();
	res = '';
	return ' '.join([stemmer.stem(a) for a in S]);
'end def'






action_type = './Travel';

for idx,row in df_chats.iterrows():

	msg = row['CHAT'];
	s_msg = p_process(msg);
	# print s_msg;
	if('ticket' in s_msg):
		print 'yoyo'
		fn = str(row['NUMBER'])+'_'+str(row['ID']);
		if not(os.path.exists(action_type)):
			os.mkdir(action_type);
		f=open(action_type+'/'+fn+'.txt','w')
		f.write(msg);
		f.close();
	'end if'

'end for'





