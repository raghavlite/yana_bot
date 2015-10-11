from transitions import Machine
import random

from nltk.corpus import stopwords
import re
import hasing as hs
hs = reload(hs)


class NarcolepticSuperhero(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    # states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']
    states = ['Intro', 'Food', 'Travel', 'Service', 'booking','cancellation','flight','train','bus'];





    def __init__(self, name):

        # No anonymous superheroes on my watch! Every narcoleptic superhero gets 
        # a name. Any name at all. SleepyMan. SlumberGirl. You get the idea.
        self.name = name

        # What have we accomplished today?
        self.kittens_rescued = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='Intro')

        # add some transitions. We could also define these using a static list of 
        # dictionaries, as we did with states above, and then pass the list to 
        # the Machine initializer as the transitions= argument.

        # At some point, every superhero must rise and shine.
        self.machine.add_transition('Travel', 'Intro', 'Travel');

        self.machine.add_transition('Food', 'Intro', 'Food');

        self.machine.add_transition('Service', 'Intro', 'Service');

        self.machine.add_transition('booking', 'Travel', 'booking');

        self.machine.add_transition('cancellation', 'Travel', 'cancellation');


        self.machine.add_transition('train', 'booking', 'train');

        self.machine.add_transition('flight', 'booking', 'flight');

        self.machine.add_transition('bus', 'booking', 'bus');





        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        self.machine.add_transition('new', '*', 'Intro');

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print "Beauty, eh?"




ref ={'Intro':{'path_': {'Travel':['train','from','to','flight','bus','travel','ticket'],'Food':['food','hungry']},'FV':[] , 'LV' : [] ,'FFV':{} },
        'Travel': {'path_':{'booking':['book','flight','train','bus'],'cancellation':['cancel']},'FV':[],'LV':[],'FFV':{}},
                'booking':{'path_':{'flight':['flight','plane','jet'],'train':['train','railway','tier'],'bus':['bus']},'FV':['From','To','Date'],'LV':['Name','Class','Travel Time','Start Time','End Time','options'],'FFV':{'From':'check_element2','To':'check_element2','Date':'get_date'}},
                    'flight':{'path_':{},'LV':['cheapest','earliest','fastest','next'],'FV':['Flight_no','class','Passenger Details']},
                    'train':{'path_':{},'LV':['cheapest','earliest','fastest'],'FV':['Train_no','class','Tatkaal','Passenger Details'],'FFV':{'Train_no':'train_no','class':'get_class','Tatkaal':'is_tatkal','Passenger Details':'train_no'}},
                'cancellation':{'path_':{},'FV':['PNR'],'LV':[]},
};




global msg_stack;
msg_stack = [];


global querry_stack;
querry_stack=[];


global blackboard;
blackboard ={};

global bb_funcs;
bb_funcs = {};


cachedStopWords = stopwords.words("english")
cachedStopWords.remove(u'to')
cachedStopWords.remove(u'from')



def TA(msg):
    text = ' '.join([word for word in msg.split() if word not in cachedStopWords])
    return text;
'end def' 


def Re_search(v_list):

    res=v_list[0];

    for itm in v_list[1:]:
        res+='|'+itm;
    'end for'

    return res;

'end def'    

def Add_to_BB(SM):
    global blackboard;
    c_s = SM.state;

    FV = ref[c_s]['FV'];

    for itm in FV:
        blackboard[itm] = None;
    'end for'

'end def'


def Iters(SM,p_d,msg_l):

    for k,v in p_d.iteritems():
        pp = Re_search(v);
        # print pp , k, v , msg_l;
        if(re.search(pp,msg_l) != None):
            getattr(SM, k)();
            print SM.state;
            return True;
        'end if'
    'end for'
    return False;

'end def'    



def ST(SM):
    
    global bb_funcs;
    c_s = SM.state;

    newlist = msg_stack[::-1]

    for msg_l in newlist:
        p_d = ref[c_s]['path_'];
        # better state match
        km = True;

        while(km):
            km = Iters(SM , p_d , msg_l); 
            c_s = SM.state;
            Add_to_BB(SM);
            p_d = ref[c_s]['path_'];
            bb_funcs.update(ref[c_s]['FFV']);

        'end while'

    'end for'




'end def'

def TF(SM):
    global blackboard;

    c_s = SM.state;

    newlist = msg_stack[::-1]
    for msg_l in reversed(newlist):
        for k,v in blackboard.iteritems():
            if(v == None):
                methodToCall = getattr(hs,bb_funcs[k]);
                result = methodToCall(msg_l);
                print 'filler templete',result,bb_funcs[k];
                blackboard.update(result); 
            'end'
        'end'
    'end'

    
    p_d = ref[c_s]['path_'];
    res = '';
    for k,v in p_d.iteritems():

        if(k != None):
            res += '|'+k;
        'end'

    'end'


    if(res != ''):
        res = 'Please elaborate among '+res;
    
    res2 = '';
    for k,v in blackboard.iteritems():
        if(v == None):
            res2 += ','+k;
        'end'

    if(res2 != ''):
        res2 = 'Please specify ' + res2;



    # print res+'\n'+res2;
    return res+'\n'+res2;

'end def'


def Qry():    
    qry_keys = ['options','all','give','all'];

    pp = Re_search(qry_keys);

    newlist = msg_stack[::-1]

    for msg_l in newlist:

        # print pp , k, v , msg_l;
        if(re.search(pp,msg_l) != None):
            getattr(SM, k)();
            # print SM.state;
            return True;
        'end if'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'end qry'


def Ordr():
    ''
'end ordr'

def IsQ():
    ''
'end isQ'    

def IsO():
    ''
'end def'

def IsGQ():
    ''
'end def'    



def Process(msg):

    ST(SM);
    res = TF(SM);
    

    # if(IsQ(msg)):
    #     res = Qry(msg);
    # elif(IsGQ()):
    #     res = res;
    # elif(IsO()):    
    #     res = Ordr()
    # 'end'

    return res;
'end def'










SM = NarcolepticSuperhero("Batman")

ste = SM.state;

msg = raw_input("Chat Initialised..\n");

while(msg!=None):
    print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH';
    msg = TA(msg);
    msg_stack.append(msg.lower());
    res = Process(SM);
    if(res != None):
        print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH';
        msg = raw_input(res+'\n');
    else:
        msg = raw_input();
    'end if'
'end while'




















