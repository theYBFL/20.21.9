# input() - Kullanıcıdan veri almak için kullanırız.
# input(parametre) - bir parametre alır. Bu parametre ise kullanıcıdan istenilen veriyi almak için yazılan bilgi metnidir.
# degisken=input(...)
isim=input("İsminizi giriniz: ") #Volkan
soyisim=input("Soyisminizi giriniz: ") #YILDIZ
# Merhaba, Volkan YILDIZ!
print("Merhaba",isim,soyisim,"!")


#NOT: input ile gelen veri her zaman karakter dizisi olarak gelir. 
s1=input("1. sayıyı giriniz: ") #"12"
s2=input("2. sayıyı giriniz: ") #"34"

t=s1+s2 #"12"+"34" >>> "1234"

print("Sayıların toplamı",t) # Sayıların toplamı 1234

