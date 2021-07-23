sozluk={"python":"güzel bir dil","php":"script dili","Java":"compile edilen dil"}
print(sozluk["python"])
for i in sozluk.items():
    print(i)
print("-----------------------")
for i in sozluk.items():
    print(i[0]+" "+i[1])
print("-----------------------")
for i,j in sozluk.items():
    print(i+" "+j)

dersler={"Ahmet":["vt","is"],"oguz":["script","python"]}
isim=input("isim girin: ")
print("{} in aldığı derlser".format(isim))
for i in dersler[isim]:
    print(i)