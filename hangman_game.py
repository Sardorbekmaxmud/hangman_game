import random

print("Xush kelibsiz!\nKeling HANGAMN o'yinini o'ynaymiz!\nSiz harf kiritasiz va meva nomini topasiz")

fruits = {'apple','banana','lemon','ananas','apelsin','anor',"Pear","Cherry"}#,"Plum","Peach","Grapes","Strawberry","Blueberry","Raspberry","Blackberry","Boysenberry","Cranberry","Lime","Grapefruit","Tangerine","Clementine"}

fruits = tuple(fruits)

rm_fruit_name = random.choice(fruits).lower()

taxminlar = set()
urunish_soni = 0
qolgan_urunish = 5

while True:
    displey = ""
    for char in rm_fruit_name:
        if char in taxminlar:
            displey+=char
        else:
            displey+="_"
    print("\n",displey)

    if displey==rm_fruit_name:
        print(f"\n🎉Siz meva nomini {urunish_soni} ta urunishda topib, yutdingiz🎉")
        break

    if urunish_soni>=len(rm_fruit_name)+5:
        print(f"Sizda {qolgan_urunish} urunish qoldi!")
        qolgan_urunish-=1

    if len(rm_fruit_name)+10==urunish_soni:
        print("Uzur, siz barcha urunishlardan foydalanib bo'ldingiz! GAME OVER")
        break

    taxmin = input("\nHarf kiriting: ").lower()
    urunish_soni+=1
    if len(taxmin)==1 and taxmin.isalpha():
        if taxmin not in taxminlar:
            taxminlar.add(taxmin)
        else:
            print("♻️  Bu harfni avval kiritgansiz!")
            continue
        if taxmin not in rm_fruit_name:
            print("\n❌ kiritdingiz!")
        else:
            print('\n✅ kiritdingiz!')
    else:
        print("so'z, bo'sh joy,belgilar va sonlar qabul qilinmaydi!")
