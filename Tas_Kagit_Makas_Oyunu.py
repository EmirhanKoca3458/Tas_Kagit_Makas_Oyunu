import random

print ("Hoşgeldiniz")

taş_kağıt_makas = ["Taş","Kağıt","Makas"]

taş = taş_kağıt_makas[0]
kağıt = taş_kağıt_makas[1]
makas = taş_kağıt_makas[2]

seç = input("Taş mı ? Kağıt mı ? Makas mı ?")

bot = random.choice(taş_kağıt_makas)

if seç==kağıt:
    if kağıt==bot:
        print("berabere")
    elif taş==bot:
        print("kazandınız")
    elif makas==bot:
        print("kaybettiniz")
elif seç==taş:
    if taş==bot:
        print("berabere")
    elif kağıt==bot:
        print("kaybettiniz")
    elif makas==bot:
        print("kazandınız")
elif seç==makas:
    if makas==bot:
        print("berabere")
    elif taş==bot:
        print("kaybettiniz")
    elif kağıt==bot:
        print("kazandınız")