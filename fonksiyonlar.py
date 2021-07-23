def merhaba():
    print("merhaba dünya")
def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
    return faktoriyel
def kokbul(a,b,c):
    delta=(b*b-4*a*c)
    if(delta<0):
        print("reel kök bulunamadı")
        return
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
    return (x1,x2)
merhaba()

sayi=int(input("sayi girin:"))
print(factoriel(sayi))

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kokbul(a,b,c)
print(sonuc)

