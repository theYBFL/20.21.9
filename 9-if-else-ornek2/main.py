# Kullanıcıdan üç sınav notu istenecektir. Sınav notlarının ortalaması 50 veya üstüyse ekranda "Dersen Geçtin" yazsın, altındaysa "Dersten Kaldın" yazsın.

n1=int(input("1. Not: "))
n2=int(input("2. Not: "))
n3=int(input("3. Not: "))

ort=(n1+n2+n3)/3

if ort>=50:
  print("Not ortalamınız",ort,"! Dersten Geçtiniz")
else:
  print("Not ortalamınız",ort,"! Dersten Kaldınız")