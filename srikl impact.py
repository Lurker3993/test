import random
import time

def menu():
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⠟⣿⢟⣩⣦⣴⣌⣻⣿⠻⣿⣿⢟⣿⡿⣛⡛⢿⡟⢿⣿⡟⣿⣟⣛⣛⣻⣿⢛⣛⡛⢿⡿⣛⣛⣛⣿⣟⣛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⠨⣿⣍⢈⣿⢸⣿⣿⣿⣿⠾⣿⣅⠻⠟⣸⣿⢸⣿⣿⠎⣿⡘⣿⢱⣿⢏⣉⣹⣿⡧⢸⡿⢋⣼⣷⣬⣙⠻⣿⠋⣉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣦⣿⣦⡛⢻⠟⣋⣷⣿⣿⣧⣿⣿⣿⣦⣭⣥⣾⣿⣧⣥⣾⣿⣦⣭⣭⣽⣯⣼⣿⣦⣿⣿⣭⣭⣥⣿⣦⣭⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    time.sleep(1)
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠟⠹⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣶⣮⣿⢿⣿⣏⣡⣤⣼⢿⡾⣧⢤⣌⣹⡿⣿⡿⠿⣿⡍⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⠛⢻⠐⠓⡇⣈⠇⣼⡀⠙⢷⠸⠇⢸⠃⠸⣗⠐⣮⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣛⣥⣞⣬⣯⣧⣼⣧⣸⣙⣃⣞⣸⣧⣼⣧⣼⣧⣬⣿⣧⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣍⣼⣿⣩⣽⣿⣍⣿⣍⣿⣿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("\t\t\t    Coded by Lurker3993\n\n")
    print("Type anything to start the game!")
    global gamestart
    gamestart = input()
    print("⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿")
    print("⣿⣿⣿⡟⢁⢽⣿⣿⣿⣿⣿⣿⣿⠋⢀⣤⣤⣄⠈⢻⣿⣿⣿⣿⡟⡃⢽⣿⣿⡗⢘⢻⣿⣿⣿⣿⢫⠟⠛⢿⣿⣦⠈⢿⣿⣿⣿⡿⢿⡿⠿⡀⠿⢿⡿⢿⣿⣿⣿⡿⠿⢿⡏⡆⣻⠿⠿⣿⣿⣿⣿⣿⡿⢋⡾⢷⡘⢿⣿⣿")
    print("⣿⣿⠋⠣⢀⠨⠹⣿⣿⣿⣿⣿⡷⢶⣿⣁⣀⡉⢳⡄⢿⣿⣿⡟⢇⠁⢜⣿⣿⡡⠊⡸⢻⣿⣿⡇⢠⣴⣤⢿⣿⠏⠀⣯⣿⣿⣿⣿⢆⡞⣱⣶⣋⠳⡰⣿⣿⣿⣿⣿⡔⣃⣛⣙⢏⣚⣼⣿⣿⣿⣿⠟⡄⢊⠔⣆⢻⡄⠹⣿")
    print("⣿⢳⢀⡾⣭⠙⡄⡎⣿⣿⣿⣿⣷⡾⣿⠛⡙⢻⡄⡇⣽⣿⣿⣿⣄⣩⣵⢪⡥⣭⣅⣤⣿⣿⣿⡇⣿⡿⠿⢳⣿⣆⣼⣿⣿⣿⣿⣯⡎⢥⣝⣿⣯⡼⢡⣽⣿⣿⣿⣿⢏⡝⣄⢢⣌⣏⢻⣿⣿⣿⣿⡄⠱⣇⢺⡡⢎⠸⣠⣿")
    print("⣿⣷⣕⠦⣻⠺⣡⣵⣿⣿⣿⣿⣿⣶⢿⡸⠷⡾⢑⣼⣿⣿⣿⣿⣿⣿⣧⡑⢊⣽⣿⣿⣿⣿⣿⣿⣿⣿⣀⠘⠿⠿⢟⣿⣿⣿⣿⣿⣿⣶⣌⠛⣡⣶⣿⣿⣿⣿⣿⣷⣶⣾⡏⠏⣽⣶⣶⣿⣿⣿⣿⣿⣦⠙⣦⣴⢃⣴⣿⣿")
    print("⣿⣿⣿⣿⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣱⣾⣿⣿⣿")
    print("Full screen may improve your gaming experience.")
    time.sleep(0) #change to 7 once it is completed

fivestar = "Hu Tao 胡桃" #change it if you want
fivestarX = ["Jean 琴", "Diluc 迪卢克", "Qiqi 七七", "Tighnari 提纳里", "Mona 莫娜", "Keqing 刻晴", "Dehya 迪希雅"]
fourstar = ["Xingqiu 行秋", "Layla 莱依拉", "Beidou 北斗"]
fourstarX = ["The Flute", "Sike Sword", "lion roar","eye of perspective", "map mare", "fish claymore", "favonos greatsword", "sike bow", " fav bow", "dragons bane", "the catch"]
threestar = ["Debating Club", "Rascal's Blade", "black Tassel", "thrilling Tales of Dragon slayer", "Slingshot",]
fivePity = fourPity = 0
gtee5 = gtee4 = False

def fourpitysystem():
    global fourPity; global fivePity; global gtee4
    if fourPity <= 8:
        luck4 = random.randrange(1,10)
        if luck4 >= 2:
            print("*** - ", random.choice(threestar), "\n")
            fourPity += 1
            fivePity += 1
        else:
            if gtee4 == False:
                ff4 = random.randrange(1,3)
                if ff4 == 1:
                    print("**** - ", random.choice(fourstar), "\n")
                    fourPity = 0
                    fivePity += 1
                else:
                    print("**** - ", random.choice(fourstarX), "\n")
                    fourPity = 0
                    fivePity += 1
            else:
                print("**** - ", random.choice(fourstar), "\n")
                fourPity = 0
                fivePity += 1
    else:
        if gtee4 == False:
            ff4 = random.randrange(1,3)
            if ff4 == 1:
                print("**** - ", random.choice(fourstar), "\n")
                fourPity = 0
                fivePity += 1
            else:
                print("**** - ", random.choice(fourstarX), "\n")
                fourPity = 0
                fivePity += 1

def pitysystem():
    global fourPity; global fivePity; global gtee5
    if fivePity < 74:
        luck5 = random.randrange(1,101)
        if luck5 >= 2:
            fourpitysystem()
        else:
            if gtee5 == False:
                fiftyfifty = random.randrange(1,3) #1 means won #2 means lost
                if fiftyfifty == 1:
                    print("***** - ", fivestar, "(50/50 Won, Obtained at ", fivePity, " pity)\n")
                    fivePity = 0
                    fourPity = 0
                    gtee5 = False
                elif fiftyfifty == 2:
                    print("***** - ", random.choice(fivestarX), "(50/50 Lost, Obtained at ", fivePity, " pity)\n")
                    fivePity = 0
                    fourPity = 0
                    gtee5 = True
            else:
                print("***** - ", fivestar, "(Guaranteed, Obtained at ", fivePity, " pity)\n")
                gtee5 = False
                fivePity = 0
    else:
        luck5 = random.randrange(1, 101 - int(fivePity) - 10)
        if luck5 >= 2:
            fourpitysystem()
        else:
            if gtee5 == False:
                fiftyfifty = random.randrange(1,3) #1 means won #2 means lost
                if fiftyfifty == 1:
                    print("***** - ", fivestar, "(50/50 Won, Obtained at ", fivePity, " pity)\n")
                    gtee5 = False
                    fivePity = 0
                else:
                    print("***** - ", random.choice(fivestarX), "(50/50 Lost, Obtained at ", fivePity, " pity)\n")
                    gtee5 = True
                    fivePity = 0
            else:
                print("***** - ", fivestar, "(Guaranteed, Obtained at ", fivePity, " pity)\n")
                gtee5 = False
                fivePity = 0
                

menu()
time.sleep(3)
print("-------------------------\nLimited Character Banner\n-------------------------")
print("New 5* Character: ", fivestar)
print("-------------------------")
print("4* Boosted Characters:")
print(fourstar[0])
print(fourstar[1])
print(fourstar[2])
print("-------------------------")

while True:
    pulls = input("Paimon: How much pulls are you gonna wish for, mate? ")
    print("-------------------------")
    if pulls.isdigit():
        if int(pulls) < 1001:
            pulls = int(pulls)
            for x in range(0, pulls):
                pitysystem()
            break
        else:
            print("-------------")
            print("Paimon: How about we wish below 1000 for now? We don't want your device to crash!")
            print("-------------")
            continue
    else:
        print("-------------------------")
        print("Paimon: Even Paimon can do much better than you to enter a number rather than an alphabet!")
        print("-------------------------")
        continue
