# and or not
# if x and y: >>> hem x hemde y koşulu true olmalı
# if x or y: >>> ya x, ya y ya da hem x hem y koşulu true
# if not x==y: >>> x ve y nin eşit olmadığı durumlar

s=-1

if s>9 and s<100: # 9<s<100 olmaz.
  print("Sayı iki basamaklı")


if s>9 or s<100: # 9<s<100 olmaz.
  print("Sayı iki basamaklı")


if not s<0:
  print("Sayı ya sıfıra eşit ya da pozitif")

"""
Ders sınav ortalamasının 5 lik not sistemindeki karşılığını gösteren program
0-50 >>> 1
50-60 >>> 2
60-70 >>> 3
70-85 >>> 4
85-100 >>> 5
"""

n1=int(input("1. yazılı:"))
n2=int(input("2. yazılı:"))

ort=(n1+n2)/2 #45

if 0<=ort and ort<50:
  print("Ortalamanız",ort,"yani 1 oldu.")
elif 50<=ort and ort<60:
  print("Ortalamanız",ort,"yani 2 oldu.")
elif 60<=ort and ort<70:
  print("Ortalamanız",ort,"yani 3 oldu.")
elif 70<=ort and ort<85:
  print("Ortalamanız",ort,"yani 4 oldu.")
elif 85<=ort and ort<=100:
  print("Ortalamanız",ort,"yani 5 oldu.")
else:
  print("Not girişini yanlış yaptınız.")