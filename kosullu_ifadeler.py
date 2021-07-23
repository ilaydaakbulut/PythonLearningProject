yas=int(input("yaşınızı girin:"))
if yas>=18:
    print("girebilirsiniz.")
else:
    print("giremezsiniz.")
print("-----------------------------------")
note= int(input("notunuzu girin:"))
if note>= 90:
    print("A aldınız")
elif note>= 80:
    print("B aldınız")
elif note>= 70:
    print("C aldınız")
else:
    print("kaldınız")
print("-----------------------------------")
defkullanici="yazilimci"
defparola="134"
kullanici=input("kullanıcı adı:")
parola=input("parola:")
if((defkullanici==kullanici) and (parola==defparola)):
    print("yazilim bilimi sitesine hoş geldiniz.")
elif((defkullanici!=kullanici) and (parola==defparola)):
    print("kullanıcı adi yanlış.")
elif((defkullanici==kullanici) and (parola!=defparola)):
    print("parola yanlış")
else:
    print("tekrar deneyin")
