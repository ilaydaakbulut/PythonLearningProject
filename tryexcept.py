sayi1=input("sayi1:")
sayi2=input("sayi2:")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)
except ValueError:
    print("lütfen 10'luk tabanda  bir sayı girin.")

except ZeroDivisionError:
    print("bir sayi 0'a bölünemez.")

except(EnvironmentError,OverflowError):
    print("hata")
