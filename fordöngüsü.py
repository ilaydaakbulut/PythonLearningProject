"""
string="gollum"
liste={"elma","armut","kiraz"}
for i in string:
    print(i)
for j in liste:
    print(j)

print(range(2,10,2))
print(*range(2,10,3))
for k in range(1,10):
    print(k*"*")
"""
faktoriyel=1
while True:
    sayi=int(input("lütfen negatif olmayan bir sayı girin:"))
    if(sayi<0):
        print("litfen negatif olmayan bir sayi girin")
    else:
        for i in range(1,sayi+1):
            faktoriyel*=i

        print("faktöriyel",faktoriyel)
        break