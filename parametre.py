def geometri(sekil):
    if len(sekil)==3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        if (a+b)>c and (a+c)>b and (b+c)>a:
            if(a==b) and (a==c) and (b==c):
                print("eskenar ücgen")
            elif(a==b) and (a==c):
                print("eşkenar üçgen")
            else:
                print("çeşitkenar üçgen")
        else:
            print("ücgen belirtmiyor")
    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if(a==b)and (a==c) and (a==d):
            print("kare")
        elif(a==c) and (b==d):
            print("dikdörtgen")
        else:
            print("normal dörtgen")
    else:
        print("herhangi bir sekil değil")
def topla(liste):
    if(len(liste))==0:
        return 0
    else:
        return liste[0]+(topla(liste[1:]))
a=8
def fonksiyon():
    global a
    a=2
    print(a) #global eki ile degeri artık 2 normalde 8 di

"""
while(True):
    eleman_sayisi=int(input("eleman sayısınızı giriniz."))
    if(eleman_sayisi==3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri([a,b,c])
    elif(eleman_sayisi==4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geometri([a,b,c,d])
    else:
        print("lütfen tekrar giriniz.")
"""
print(topla([1,2,3,4]))
fonksiyon()
print(a)
