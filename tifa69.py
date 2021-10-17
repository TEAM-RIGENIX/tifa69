#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes Akil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Tifa m10 bot


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;96m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;94m'

##### LOGO #####
logo1 = """
\033[1;93m.    __  __ _  __    ___      _   
\033[1;93m     |  \/  / |/  \    | _ ) ___| |
\033[1;93m     | |\/| | | () | | _ \/ _ \  _|
\033[1;93m     |_|  |_|_|\__/  |___/\___/\__|

\033[1;91m--> WordPress er   culer Web developer
\033[1;92m--> Trainer   :- Tifa m10 web development center
\033[1;93m-->  Utuber   :- Gaming with m10 gamer
\033[1;95m--> TIFA RATE       :- 69

"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;91mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;93m.    __  __ _  __    ___      _   
\033[1;93m     |  \/  / |/  \    | _ ) ___| |
\033[1;93m     | |\/| | | () | | _ \/ _ \  _|
\033[1;93m     |_|  |_|_|\__/  |___/\___/\__|

\033[1;91m--> WordPress er   culer Web developer
\033[1;92m--> Trainer   :- Tifa m10 web development center
\033[1;93m-->  Utuber   :- Gaming with m10 gamer
\033[1;95m--> TIFA RATE       :- 69


"""

CorrectUsername = "tifabotm10"
CorrectPassword = "piruwebdeveloper"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;97mTool Username \x1b[1;97m------- \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m\x1b[1;97mTool Password  \x1b[1;97m------- \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Ijaz
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/Your')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/your')

