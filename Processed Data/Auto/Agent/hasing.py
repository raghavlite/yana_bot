import pandas as pd
import re;
import parsedatetime;
import re, collections
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import tee, izip
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

# tablesize = 257;

# def hash(astring, tablesize):
#     sum = 0
#     for pos in range(len(astring)):
#         sum = sum + ord(astring[pos])

#     return sum%tablesize
# 'end def'



df_s = pd.read_csv('./stations.csv',sep = '\t');

ls_s = df_s['Station'].tolist();
ls_sc = df_s['Code'].tolist();

# ls_sc = [a.lower() for a in ls_sc];

cm=0
for a in ls_s:
	
	if(len(a.split())>1):
		cm+=1;
	'end'
'end for'





def words(text): return re.findall('[a-z]+', text.lower());

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(1,len(word)-1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   return set(deletes)
'end def'


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))
'end def'

def known_edits3(word):
	return set(e3 for e2 in known_edits2(word) for e3 in edits1(e2));
'end def'

def known_edits4(word):
	return set(e4 for e3 in known_edits3(word) for e4 in edits1(e3))


def known_edits(word):
	return known_edits2(word)|edits1(word)|set([word]);
'end def'


def product(lll):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = lll;
    result = [[]];
    # print pools
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    'end def'

    for prod in result:
        yield tuple(prod)
    'end'
'end def'







global commons ;
commons = ['station','railway','nagar','junction','ngr','city','road','cant','halt','cy','cty','cantt.','cantt','town','jn','upper','terminal','gate','cntl'];




def edit_dist(strng,cde):
	wrds = strng.split();
	dct ={};
	lk = {};
	for p in wrds:
		if(len(p)>3):
			# can be improved by taking a better 
			if(p not in commons):
				dct[p] = known_edits(p);
				lk.update(dict.fromkeys(dct[p],cde));
			else:
				dct[p] = known_edits(p);


		else:
			dct[p] = set([p]);
		'end if'
	'end for';	

	ll = [dct[pp] for pp in wrds];

	ll = list(product(ll));
	# print ll;
	
	for pp in ll:
		# print pp;
		lk[' '.join(pp)] = cde;
	'end for'

	return lk;

'end def'



# ///////////////////////////Part 1


def stop_wrds(text):
    # text = 'hello bye the the hi'
    text = [word for word in text.split() if word not in cachedStopWords]
    return text;
'end def'



def bigrams(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
'def'




def grams(line):
    line = line.lower();
    # line = stop_wrds(line);
    uni = stop_wrds(line)
    words = line.strip().split()
    bi = bigrams(words)

    bi_lst = [ i+' '+j for i,j in bi if(i not in cachedStopWords)&(j not in cachedStopWords)];
    # print uni
    # print list(bi)
    print uni;
    print bi_lst;
    return uni+bi_lst; 
'end def'





# part 2.//////////////////////////////









# Complexity hgere wa that i had to seperatedly bloat up 
# each word in the stations name and finaaly find a
# cross product. Also i had to do a fuzzy string match
# and not a normal one.
#  many other combinations tried nothing worked.
#  edit distance are deletions keeping first and last word common


# exact word word match vs fuzzy match 
#  fuzzy match has to be done for all the words















set_s = set(ls_s);
set_sc = set(ls_sc);

df_a = pd.read_csv('./airports.csv')

ls_a = df_a['Airport'].tolist();
ls_ac = df_a['Code'].tolist();

set_a = set(ls_a);
set_ac = set(ls_ac);

global pos_pat ;
global mng ;


bltd = {};
bltd_c = {};
i=0;
for st2,cde in zip(ls_s,ls_sc):
	


	bl_t = edit_dist(st2.lower(),cde);
	bltd.update(bl_t);
	# bltd+=bl_t;
	# bltd_c += [cde]*len(bl_t);
	i+=1;
	print i;
'end for'

# import csv

# with open('./edit_stations.csv', 'wb') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, bltd.keys())
#     w.writeheader()
#     w.writerow(bltd)




# ls_s += bltd;
# ls_sc += bltd_c;






pos_pat = ['','frm','from','to','2','to.+from','2.+from','to.+frm','source.+destination','from.+to','from.+2','frm.+2','frm.+to'];
mng = [['From','To'],['From'],['From'],['To'],['To'],['To','From'],['To','From'],['To','From'],['From','To'],['From','To'],['From','To'],['From','To'],['From','To']];



def ana_ret(sc,lm):

	# redo ...
	# lm = " ".join(lst);
	print lm;
	gmth = None;
	for p,q in zip(pos_pat,mng):
	 	mth = re.search(p, lm);
	 	if(mth!=None):
	 		gmth = q;
	 	'end if'
	'end if'
	i=0;

	if(gmth == None):
		kk=0;
	else:
		kk = len(gmth);
	'end'
	print len(sc);
	ll ={};

	if (len(sc) == kk) & (kk > 0):
		for pp1 in gmth:
			ll[pp1]=sc[i];
			i+=1;
		'end for'

		print 'jujubei',gmth;

	elif len(sc) >= 2:
		if(gmth[0] == 'From'):

			ll['From'] = sc[1];
			ll['To'] = sc[0];
		else:
			ll['From'] = sc[0];
			ll['To'] = sc[1];
		'end'
		print 'OMG'
	else:
		ll ={};
	'end if'

	return ll;

'end def'



def check_element2(txt):
	sd = [];
	sc =[];


	# lst = txt.lower().split();

	lst = txt.split();
	# codes ....
	for a in lst:
		if(a in set_sc):
			sc.append(a);
		'end if'
	'end for'

	if len(sc) > 0:
		return ana_ret(sc,lst);

	lst = grams(txt);

	# bigrams and unigrams
	# print lst;
	for a in lst:
		# print a;
		# max_m =0;
		# max_sc ='';
		# max_oo ='';
		# for oo,ii in zip(ls_s,ls_sc):
		# 	mtch = fuzz.partial_ratio(oo, a)
		# 	if (mtch > max_m):
		# 		max_m = mtch;
		# 		max_sc = ii;
		# 		max_oo = oo;
		# 	'end if'
		# 'end for'
		# print max_sc, max_m, max_oo, a;
		# if(max_m > 70):
		# 	sd.append((max_sc,max_m));
		# 'end if'
		if(a in bltd):
			print a
			sd.append(bltd[a]);
	'end for'

	# print sd;

	
	if len(sd) > 0 :
		return ana_ret(sd,txt);
	'end if'

	return {};

'end def'








 
# def check_element(lst,b):

# 	sd = [];
# 	sc = [];

# 	if (b==1) :
		
# 		for a in lst:
# 			if a in set_s:
# 				sd.append(a);
# 			elif a in set_sc:
# 				sc.append(a);
# 			else:
# 				''
# 			'end if'
# 		'end for'

# 		if len(sc) > 0:
# 			return ana_ret(sc,lst);
# 		elif len(sd) > 0 :
# 			sd[0] = df_s[df_s['Station']==sd[0]].iloc[[0]]['Code'];
# 			sd[1] = df_s[df_s['Station']==sd[1]].iloc[[0]]['Code'];

			
			
# 			return ana_ret(sd,lst);

# 		else:
# 			''
# 		'end if'


# 	elif (b==2) :
# 		''
# 	else:
# 		''
# 	'end if'


# 'end def'

























# Date parsing can also be used for other datepickers
# essentially again is a wod match (keyword)
# followed by an intelligent mechanism to pick date.




global date;

date = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st'];

date = date + [str(i) for i in range(1,32)];

global mnth;

mnth = ['january','february','march','april','may','june','july','august','september','october','november','december','jan','feb','mar','aug','sept','oct','nov','dec'];

global mnth_k; 

mnth_k = ['january','february','march','april','may','june','july','august','september','october','november','december','january','february','march','august','september','october','november','december'];




def get_date(txt):

	lst = txt.split();

	parser = parsedatetime.Calendar();
	
	for pp in lst:
		if(re.search('(\d{1,2}(/|-)\d{1,2})',pp)!=None):
			mm = re.search('(\d{1,2})(/|-)(\d{1,2})',pp);
			nn = list(mm.groups());
			temp = nn[2];
			nn[2] = nn[0];
			nn[0] = temp;
			nn[1] ='/'
			print ''.join(nn);
			ll = parser.parse(''.join(nn));
			if(ll[1]!=0):
				return { 'Date':str(ll[0][2])+'/'+str(ll[0][1])+'/'+str(ll[0][0])};
		'end'
	'end'


	res1 = '';

	for pp in lst:
		if (pp in mnth):
			res1 += mnth_k[mnth.index(pp)];
		'end'
	'end'

	res2 = '';

	for pp in lst:
		if (pp in date):
			res2 += pp;
		'end if'
	'end'

	print res1 , res2;

	if(res1 != '')&(res2 != ''):
		ll = parser.parse(res1+' '+res2);
		return { 'Date':str(ll[0][2])+'/'+str(ll[0][1])+'/'+str(ll[0][0])};
	'end'

	return {};

'end def'




# /////////////////////////////////////////////
# ///////////Name age sex picker///////////////


from nltk.tag.stanford import NERTagger
global st ;
st = NERTagger('./english.all.3class.distsim.crf.ser.gz','./stanford-ner-3.4.jar');




def namepicker(msg):
	pp = st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
	for a,b in pp:
		if(b==u'PERSON'):
			# 
			''
		'end'
	return pp;
'end def'




AGE_VAR = ['age','old'];
def agepicker(msg):

	lst = msg.split();
	for kk in lst:
		pp = re.search('[^a-zA-Z]\d{1,2}[^a-zA-Z]',kk);
		if(pp!=None):
			return pp.groups()[1];
		'end def'
	'end for' 

	return {};


'end def'



def sex_picker(msg):
	srch = re.search('[^a-zA-Z](M|F)[^a-zA-Z]',msg);
	
	if srch!=None:
		return {'sex':srch.groups()[0]};
	'end if'
	return {};

'end def'




def train_no(msg):

	# lst = ('a '+msg).split();

	# for kk in lst:
	pp = re.search('[^a-zA-Z0-9](\d{5})[^a-zA-Z0-9]',' ' + msg + ' ');
	if(pp!=None):
		return {'Train_no':pp.groups()[0]};
	'end def'
	# 'end for'

	return {};

'end def'




def is_tatkal(msg):
	return {'Tatkaal':False};
'end def'	


class_info = {'3 tier':'3-AC','3ac':'3-AC', '3 a.c.':'3-AC','three ac':'3-AC','three tier':'3-AC','third ac':'3-AC','third tier':'3-AC','2ac':'2-AC','2 tier':'2-AC','two ac':'2-AC','2 a.c.':'2-AC','second ac':'2-AC','second tier':'2-AC','1 tier':'1-AC','1ac':'1-AC','one ac':'1-AC','first ac':'1-AC','first tier':'1-AC','sleeper':'SL','slpr':'SL','SC':'SL'}


classes = ['sleeper','slpr','sc','3 tier','3ac', '3 a.c.','three ac','three tier','third ac','third tier','2ac','2 tier','two ac','2 a.c.','second ac','second tier']

def get_class(msg):

	for pp in classes:
		match = fuzz.partial_ratio(msg.lower(), pp)
		print match;
		if(match > 75):
			return {'class':class_info[pp]};

	return {};
'end def'





# def passenger_details:
























