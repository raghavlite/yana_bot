import pandas as pd
import re
import math

# Data read
# df = pd.read_csv('./yana1.csv'); 


# Data Analysis

cols_list = ['NUMBER','NXT','TYPE','MESSAGE','TIME_STAMP','IS_AGENT'];
# cols_list = ['NUMBER','NXT','TYPE','MESSSAGE','TIME_STAMP','IS_AGENT','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'];
df = pd.read_csv('./yana1.csv',usecols=cols_list); 



dfc_dict = {};
temp_cols_list = cols_list;
temp_cols_list.remove('MESSAGE');
temp_cols_list.remove('TIME_STAMP');


# number of different entries in a column

# df_meta = pd.DataFrame([df.columns,df.dtypes]).T
# df_meta.columns=["Attribute","dtype"]
# df_meta




for col_name in temp_cols_list:
    print ''
    print df.groupby(col_name).size()   # syntax for printing individual entries for each column



# frequency of each of different entries in the frame
for col_name in temp_cols_list:
    clist = pd.unique(df[col_name])    # no of unique entries in this column
    df_clist = pd.DataFrame(clist)      # dataframe with 0 to n-1 entries and also the correesponding values
    dfc_dict[col_name] = df_clist       #  dictionary can work with both column names and also the index numbers
    numc = clist.size                   # here in the last two lines we only print out the number of unique entries 
    print col_name, numc                 # of each of the columns excepting the last transcript column

# /////////////////////////////////////////////////////////////




# Data filtering



# def add_prev(idx,)


rm = [];
for idx,row in df.iterrows():
	# print str(row['NUMBER']);
	# print re.match("^\d{8}$", str(row['NUMBER']));
	if(re.match("^\d{8}$", str(row['NUMBER'])) == None):
		rm.append(idx);
	elif(re.match("(incoming$|outgoing$)",str(row['IS_AGENT'])) == None):
		rm.append(idx);
	# elif(re.match("[A-Za-z\\N]",str(row['NXT']))== None):
	# 	rm.append(idx);
	elif(re.match("(media$|text$)",str(row['TYPE']))== None):
		rm.append(idx);
	'end if'
'end for'

df_filtered = df.drop(df.index[rm]);



for idx,row in df_filtered.iterrows():
	if(math.isnan(float(row['NXT']))):
		print 'yoyoyyo'




for col_name in temp_cols_list:
    clist = pd.unique(df_filtered[col_name])    # no of unique entries in this column
    df_clist = pd.DataFrame(clist)      # dataframe with 0 to n-1 entries and also the correesponding values
    dfc_dict[col_name] = df_clist       #  dictionary can work with both column names and also the index numbers
    numc = clist.size                   # here in the last two lines we only print out the number of unique entries 
    print col_name, numc  


for col_name in temp_cols_list:
    print ''
    print df_filtered.groupby(col_name).size()   # syntax for printing individual entries for each column




df_filtered.to_csv('./yana1_f.csv');




