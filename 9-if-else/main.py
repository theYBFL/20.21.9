# Koşullu Durumlar
# if koşul:
    #koşul doğru(True) olduğu zaman çalışacak kod(lar)
  #else: #Yukarıdaki koşul veya koşullar sağlanmazsa (False olursa)

s=2

if s==1:
  print("Sayı bire eşit")
else: # yukarıdaki koşul veya koşullar olmazsa
  print("Sayı bire eşit değil")


#Girilen doğum yılına göre yaşını hesaplayan ve yaşı 13’ten küçükse ekranda “Giriş İzni YOK”, 13’e eşit veya büyükse “Giriş İzni VAR” yazan program

bYil=2021

dYil=int(input("Doğum yılınız: "))

yas=bYil-dYil

if yas<13:
  print("Yaşınız",yas,"Giriş izni yok")
else:
  print("Yaşınız",yas,"Giriş izni var")
örnek