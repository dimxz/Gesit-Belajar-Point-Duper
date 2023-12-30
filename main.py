import requests
import os
import sys
import time
from datetime import datetime
from pystyle import Colors,Colorate

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.red_to_green,"""

░██████╗░██████╗░░░░░░░░░░░██████╗░██╗░░██╗██████╗░███████╗██████╗
██╔════╝░██╔══██╗░░░░░░░░░░██╔══██╗██║░░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝░███████╗░██║░░██║██║░░██║██████╔╝███████╗██████╔╝
██║░░╚██╗██░░░██╗░╚══════╝░██║░░██║██║░░██║██╔═══╝░██╔════╝██╔══██╗ By
╚██████╔╝██████╔╝░░░░░░░░░░██████╔╝███████║██║░░░░░███████╗██║░░██║ Dimxz
░╚═════╝░╚═════╝░░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

"""))

def delay(amount):
    time.sleep(amount)

def tambah(token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'api.gesitbelajar.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.0',
    }

    # Prompt the user for the desired date
    #payload = input("Enter the desired date (YYYY-MM-DD): ")
    payload = "26eg39ge37ge7ge3e"
        # Define the JSON data with the user's input
    data = {
        "todolist_values": [
            {"todolist_detail_id":"2328","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2329","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2342","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2343","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2344","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2345","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2346","value":"yes","d_date":payload,"poin":20},
            {"todolist_detail_id":"2331","value":"5","d_date":payload,"poin":100},
            {"todolist_detail_id":"2333","value":"10","d_date":payload,"poin":80},
            {"todolist_detail_id":"2332","value":"5","d_date":payload,"poin":75},
            {"todolist_detail_id":"2334","value":"yes","d_date":payload,"poin":40},
            {"todolist_detail_id":"2335","value":"yes","d_date":payload,"poin":50},
            {"todolist_detail_id":"2336","value":"yes","d_date":payload,"poin":50},
            {"todolist_detail_id":"2338","value":"yes","d_date":payload,"poin":75},
            {"todolist_detail_id":"2337","value":"yes","d_date":payload,"poin":75}
        ]
    }

    url = 'https://api.gesitbelajar.com/api/todolist/detail/action'
    
    try:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.orange,"[+] Duping...  (Tekan Ctrl + C untuk menghentikan script)"))
        while True:
            req = requests.post(url, headers=headers, json=data)
            hasil = req.json()
            status = hasil["status"]
            total = hasil["data"]["poin_total"]
            if status == 200:
                now = datetime.now()
                timenow = now.strftime("%H:%M:%S")
                print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.green,"[+] Berhasil menambahkan poin, Total poin => ") , Colorate.Color(Colors.white,"{}".format(total)))
            else:
                now = datetime.now()
                timenow = now.strftime("%H:%M:%S")
                print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Login failed, code => {}".format(status)))
    except KeyboardInterrupt:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Ctrl + C pressed, script stopped"))
    except requests.exceptions.ConnectionError:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] You're offline / Unable to connect to GB server."))
    except requests.exceptions.Readtimeout:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Unable to connect to GB server."))



def getbearer(username, password):
    url = "https://api.gesitbelajar.com/api/login"

    headers = {
        'Accept': 'application/json',
        'Content-Lenght': '38',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'api.gesitbelajar.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.0',
    }
    isi = {
        'username': username,
        'password': password,
    }

    try:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.green,"[+] Getting bearer token."))
        hasil1 = requests.post(url, headers=headers, data=isi)
        if hasil1.status_code == 422:
            now = datetime.now()
            timenow = now.strftime("%H:%M:%S")
            print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Fill out that form, nigga!"))
        else:
            hasil2 = hasil1.json()
            status = hasil2["status"]
            if status == 200:
                now = datetime.now()
                timenow = now.strftime("%H:%M:%S")
                bearer = hasil2["token"]["original"]["token"]
                print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.green,"[+] Berhasil => ") ,Colorate.Color(Colors.white, "{}".format(bearer)))
                delay(1)
                tambah(bearer)
            elif status == 401:
                now = datetime.now()
                timenow = now.strftime("%H:%M:%S")
                print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Username or password is wrong."))
                sys.exit(0)
            else:
                now = datetime.now()
                timenow = now.strftime("%H:%M:%S")
                print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Unable to connect to GB server."))
    except KeyboardInterrupt:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Ctrl + C pressed, script stopped"))
    except requests.exceptions.ConnectionError:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] You're offline / Unable to connect to GB server."))
    except requests.exceptions.Readtimeout:
        now = datetime.now()
        timenow = now.strftime("%H:%M:%S")
        print(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.red,"[!] Unable to connect to GB server."))

now = datetime.now()
timenow = now.strftime("%H:%M:%S")
username = input(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.orange,"[?] Input username => "))
password = input(Colorate.Color(Colors.yellow,"[{}] ".format(timenow)) + Colorate.Color(Colors.orange,"[?] Input password => "))

getbearer(username,password)
