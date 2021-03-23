#Kullanıcıdan iki sayı istenecektir. 1. sayının 2. sayı kuvvetini bulup ekranda "Bulunan ? sayının basamak sayısı ?"

# 3 4 >>> 3**4 >>> 81 >>> Bulunan 81 sayısının basamak sayısı 2
# 4 5 >>> 4**5 >>> 1024 >>> Bulunan 1024 sayısının basamak sayısı 4

s1=int(input("1. Sayı: "))
s2=int(input("2. Sayı: "))

sonuc=s1**s2
basamak=len(str(sonuc))

print("Bulunan",sonuc,"sayısının basamak sayısı",basamak)