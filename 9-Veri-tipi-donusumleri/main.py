#Veri Tipi Dönüşümleri
  #1-int() fonksiyonu - int >>> integer(Tamsayı)
  #Sayı değerli karakter dizilerini veya ondalıklı sayıları tam sayıya çevirir.

a=3.14
b=int(a)
print(b)

x="12"
y=int(x)
print(y+y)

x=int("12")
print(x+x)


s1=int(input("1. sayıyı giriniz: "))
s2=int(input("2. sayıyı giriniz: "))

t=s1+s2

print("Sayıların toplamı",t)

  #2-float() fonksiyonu - Ondalıklı sayı
  # Sayı değerli karakter dizilerini veya tam sayıları ondalıklı sayıya çevirir.

x=3
y=float(x)
print(y)

x=float("5")
print(x)

  #3-str() - string - Karakter dizisi
  # Her türlü veriyi karakter dizisine çevirir.
x=3
y=3.14
print(str(x)+str(y))

  #4-bool() - Boolean Veri - Mantıksal Veri - True(1) - False(0)
print(bool(0))

#len() - length - uzunluk - Parametre olarak yazılan K.D. nin kaç karakterden oluştuğunu bulur.
c="abcdefgh"
u=len(c)
print(u)

#type()- Parametre olarak yazulan verinin tipini söyler
print(type(u))