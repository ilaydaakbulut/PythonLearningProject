import modul1
import modul2

modul1.naber()
print(modul1.mutlak(-120))

from modul1 import *
from modul2 import *

naber()
"""burada modul adını yazmaya gerek yok
ama modul adıyla yazmak daha önemli çünkü 
hangi modulün fonksiyonu çağıracağını bilemez."""

import math
print(math.factorial(6))

import urllib.request

url1="https://www.google.com.tr/imgres?imgurl=https%3A%2F%2Fiasbh.tmgrup.com.tr%2Feb47ca%2F800%2F420%2F0%2F33%2F650%2F375%3Fu%3Dhttps%3A%2F%2Fisbh.tmgrup.com.tr%2Fsbh%2F2018%2F10%2F31%2Fdeneme-nedir-ve-nasil-yazilir-1540990804971.jpg&imgrefurl=https%3A%2F%2Fwww.sabah.com.tr%2Fkultur-sanat%2F2021%2F02%2F04%2Fdeneme-nedir-ve-nasil-yazilir&tbnid=8QMb4l3pTrv4sM&vet=12ahUKEwioqISC5vnxAhVR2aQKHYTDBvUQMygBegUIARDAAQ..i&docid=fA-Bsj4JHybdkM&w=800&h=420&q=deneme&hl=tr&ved=2ahUKEwioqISC5vnxAhVR2aQKHYTDBvUQMygBegUIARDAAQ"
url2="https://www.google.com.tr/imgres?imgurl=https%3A%2F%2Fwww.bilgenc.com%2Fwp-content%2Fuploads%2F2018%2F01%2Fdeneme-nedir-ozellikleri-1200x675.jpg&imgrefurl=https%3A%2F%2Fwww.bilgenc.com%2Fdeneme-nedir-ozellikleri%2F&tbnid=CwF5YLvbGv_SRM&vet=12ahUKEwioqISC5vnxAhVR2aQKHYTDBvUQMygGegUIARDKAQ..i&docid=n3GSy94HL8f9eM&w=1200&h=675&q=deneme&hl=tr&ved=2ahUKEwioqISC5vnxAhVR2aQKHYTDBvUQMygGegUIARDKAQ"

urllist=[url1,url2]
say=1
for url in urllist:
    urllib.request.urlretrieve(url,"resim"+str(say)+".jpg")
    say+=1