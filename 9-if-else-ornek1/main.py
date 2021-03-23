parola="baskan123"

k_parola=input("Parolanızı giriniz: ")

if k_parola==parola:
  print("Sisteme hoşgeldiniz...")
  print("12 ile 12nin toplamı",12+12)
else:
  print("Parolanız yanlış ")
  print("32 ile 32nin toplamı",32+32)


#Örnek-1
#1. sayının 2. sayıya tam olarak bölünüp bölünmdiğini ekrana yazan program

# 12 3 >>> 12 sayısı 3 e tam olarak bölünür
# 14 5 >>> 14 sayısı 5 e tam olarak bölünmez

s1=int(input("1. Sayıyı giriniz: "))
s2=int(input("2. Sayıyı giriniz: "))

if s1%s2==0:
  print(s1,"sayısı",s2,"e tam olarak bölünür")
else:
  print(s1,"sayısı",s2,"e tam olarak bölünmez. Kalan",s1%s2,"dir.")