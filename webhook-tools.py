import requests
import time
import os

def spam():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('Title  Webhook-Spamer ║ BY MFR')
    print(bannerspam)
    print(copyrights)
    name = input("Bot name : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerspam)
    print(copyrights)
    webhook = input("Webhook url : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerspam)
    print(copyrights)
    message = input("Message : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Press Enter to start ")
    print("Spam start ( close windows to stop )")

    while True :
        r = requests.post(webhook,json={'content': message, 'username': name})

def delete():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('Title  Webhook-Delete ║ BY MFR')
    print(bannernuke)
    print(copyrights)
    webhook = input("Webhook url : ")
    r = requests.delete(webhook)
    os.system('cls' if os.name == 'nt' else 'clear')
    close = input("Wehbook destroyed\n\nPress enter to exit ")
    print(exit)
    os.system('cls' if os.name == 'nt' else 'clear')

def mess():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('Title  Webhook-Sender ║ BY MFR')
    print(bannermess)
    print(copyrights)
    name = input("Bot name : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannermess)
    print(copyrights)
    webhook = input("Webhook url : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannermess)
    print(copyrights)
    message = input("Message : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannermess)
    print(copyrights)
    input("Press enter to send")
    r = requests.post(webhook,json={'content': message, 'username': name})
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannermess)
    print(copyrights)
    input("Message send\n\nPress enter to exit ")
    print(exit)
    os.system('cls' if os.name == 'nt' else 'clear')

def file():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('Title  Webhook-File ║ BY MFR')
    print(bannerfile)
    print(copyrights)
    name = input("Bot name : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerfile)
    print(copyrights)
    webhook = input("Webhook url : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerfile)
    print(copyrights)
    file = input((f"Drag the file you want to send ( 8 MB max )"))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerfile)
    print(copyrights)
    input("Press enter to send")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bannerfile)
    print(copyrights)
    r =requests.post(webhook,json={'username': name}, files = {'file': open(file, 'rb')})
    input("File send\n\nPress enter to exit ")
    print(exit)
    os.system('cls' if os.name == 'nt' else 'clear')

bannerfile ="\n __    __     _     _                 _     \n/ / /\ \ \___| |__ | |__   ___   ___ | | __ \n\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / \n \  /\  /  __/ | | | |_) | (_) | (_) |   <  \n  \/  \/ \___|_| |_|_.__/ \___/ \___/|_|\_)\n _____ _ _      \n|  ___(_) |     \n| |_   _| | ___ \n|  _| | | |/ _ )\n| |   | | |  __/\n\_|   |_|_|\___|"
bannermess = "\n __    __     _     _                 _     \n/ / /\ \ \___| |__ | |__   ___   ___ | | __ \n\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / \n \  /\  /  __/ | | | |_) | |_| | |_| |   <  \n  \/  \/ \___|_| |_|_.__/ \___/ \___/|_|\_)\n _ __ ___   ___  ___ ___  __ _  __ _  ___ \n| '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ )\n| | | | | |  __/\__ \__ \ |_| | |_| |  __/\n|_| |_| |_|\___||___/___/\__,_|\__, |\___|\n                                __/ |     \n                               |___/ "
bannernuke ="\n __    __     _     _                 _     \n/ / /\ \ \___| |__ | |__   ___   ___ | | __ \n\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / \n \  /\  /  __/ | | | |_) | (_) | (_) |   <  \n  \/  \/ \___|_| |_|_.__/ \___/ \___/|_|\_\ \n             _        \n _ __  _   _| | _____ \n| '_ \| | | | |/ / _ )\n| | | | |_| |   <  __/\n|_| |_|\__,_|_|\_\___|"
bannerspam = "\n __    __     _     _                 _    \n/ / /\ \ \___| |__ | |__   ___   ___ | | __\n\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /\n \  /\  /  __/ | | | |_) | (_) | (_) |   < \n  \/  \/ \___|_| |_|_.__/ \___/ \___/|_|\_\ \n ___ _ __   __ _ _ __ ___  \n/ __| '_ \ / _` | '_ ` _ \ \n\__ \ |_) | (_| | | | | | |\n|___/ .__/ \__,_|_| |_| |_|\n    |_|"
copyrights = "╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝"
tools = "\n __    __     _     _                 _ \n/ / /\ \ \___| |__ | |__   ___   ___ | | __ \n\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / \n \  /\  /  __/ | | | |_) | (_) | (_) |   < \n  \/  \/ \___|_| |_|_.__/ \___/ \___/|_|\_\ \n _____           _      \n|_   _|         | |     \n  | | ___   ___ | |___  \n  | |/ _ \ / _ \| / __| \n  | | (_) | (_) | \__ ) \n  \_/\___/ \___/|_|___/"

os.system('Title  Webhook-Tools ║ BY MFR')
os.system('cls' if os.name == 'nt' else 'clear')
print(copyrights)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print(tools)
print(copyrights)

choix = int(input("Make your choice\n1) Spam\n2) Delete\n3) Message\n4) File\nNumber : "))
if choix == 1 :
    spam()

if choix == 2 :
    delete()

if choix == 3 :
    mess()

if choix == 4 :
    file()