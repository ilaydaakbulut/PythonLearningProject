"""
i=0
while(i<10):
    print("i nin degeri",i)
    i+=2
"""
defkullanici="yazilimcibebe"
defparola="1234"

while(True):
    kullanici=input("kullaniciadi: ")
    parola=input("parola: ")
    if((kullanici==defkullanici)and(parola==defparola)):
        print("hosgeldiniz",kullanici)
        break
    elif((kullanici!=defkullanici) and (parola==defparola)):
        print("kullanıcı adi yanlis")
    elif((kullanici==defkullanici)and (parola!=defparola)):
        print("sifrenizi mi unuttunuz?")
        print("sifreniiz değiştirmek ister misiniz? (E/H)")
        cevap=input()
        if(cevap=="E"):
            yeniparola=input("yeni parola:")
            defparola=yeniparola
            print("şifre başarıyla değiştirildi")
    else:
        print("tekrar deneyin")

