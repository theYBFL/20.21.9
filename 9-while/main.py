#while Döngüsü (...olduğu sürece)

"""
dd=x

while koşul: #koşul True olduğu sürece döngüye girer
  kod
  veya
  kodlar
  ....
  dd(döngü değişkeni) artır ya da azalt

"""
"""
#1 – ismini 5 defa ekrana yaz
dd=0 #1 2 3 4
while dd<5:
  print("Volkan")
  dd=dd+1
"""
"""
#2 – Klavyeden girilen bir kelimeyi 5 defa ekrana yazdıran akış şeması
x=0
ad=input("İsminiz: ")
while x<5:
  print(ad)
  x=x+1
"""
"""
#3 – 1’den 10’a kadar olan sayıları ekrana yaz
c=1
while c<=10:
  print(c)
  c=c+1
""" 

"""
#4 – Klavyeden girilen bir metni, klavyeden girilen sayı kadar ekrana yaz
x=0
ad=input("İsminiz: ")
defa=int(input("kaç defa: "))
while x<defa:
  print(ad)
  x=x+1
"""
"""
#5 – 5’ten 55’e kadar olan tek sayıları ekrana yaz
g=5

while g<55:
  print(g)
  g=g+2"""

"""
#6) 21’den -21’e kadar olan tek sayıları ekrana yaz
t=21 #20 19 18
while t>-21:
  print(t)
  t=t-2
"""

"""
# 0’dan kullanıcının girdiği sayıya (pozitif tam sayı girdiği varsayılarak) kadar olan sayıları ekrana yaz
y=0
k=int(input("kaça kadar... "))
while y<=k:
  print(y)
  y=y+1

# 0’dan kullanıcının girdiği sayıya (pozitif tam sayı girdiği varsayılarak) kadar olan sayıları artış miktarınıda kullanıcının belirlemesiyle ekrana yaz
y=0
k=int(input("kaça kadar... "))
artis=int(input("kaçar kaçar... "))
while y<=k:
  print(y)
  y=y+artis


# 1’den 10’a kadar olan sayıların toplamını ekranda göster
r=1
t=0
while r<=10:
  t+=r #t=t+r
  r+=1 #r=r+1
print(t)

# 1’den 10’a kadar olan tek sayıların çarpımı ekranda göster
r=1
c=1
while r<=10:
  c*=r #c=c*r
  r+=2 #r=r+1
print(c)

# Kullanıcının girdiği on sayının toplamını ekrana yaz
v=0
t=0
while v<10:
  sayi=int(input("Sayı giriniz: "))
  t+=sayi #t=t+sayi
  v+=1 #v=v+1
print(t)

#Kullanıcının istediği sayıda sayı girişi olacaktır. Girilen sayıların toplamını ekrana yaz
d=0
son=int(input("Kaç sayı toplayacaksın "))
t=0
while d<son:
  sayi=int(input("Sayıyı giriniz "))
  t+=sayi
  d+=1
print(t)
"""
"""
# 134’dan 998’a kadar olan 17’ya tam bölünebilen sayıları ekrana yaz
y=134
while y<=998:
  if y%17==0:
    print(y)
  y+=1

# 1’den 100’e kadar içinde 3’e tam bölünebilen sayıların bulunmadığı sayıları ekrana yaz
h=1
while h<100:
  if h%3!=0: #not h%3==0
    print(h)
  h+=1
"""

# Ekrana “1/2 2/3 3/4 4/5 5/6 7/8 8/9 9/10” şeklinde yaz
# 1 2 3 4 5 7 8 9
g=1
while g<10:
  if not g==6: #g!=6
    print(g,"/",g+1,sep="",end=" ")
  g+=1



