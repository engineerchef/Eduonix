import random

oyunSayisi = "0"
while oyunSayisi == "0":
    try:
        oyunSayisi = int(input("How many games do you want to play?\t"))
    except:
        print("You have to enter a numeric value!!!")

for oyun in range(0, oyunSayisi):
    rastgeleSayi = random.randint(1, 26)
    tahmin = None
    deneme = 0

    while rastgeleSayi != tahmin:
        try:
            tahmin = int(input("Pick a number :\t"))
        except:
            print("You have to enter a numeric value!!!")
            continue

        if tahmin != rastgeleSayi:
            deneme += 1
            if tahmin > rastgeleSayi:
                print("Too High")
            else:
                print("Too Low")
        else:
            print("Correct Answer!\nIt took you this many guesses:\t", deneme)
