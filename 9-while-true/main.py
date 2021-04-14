"""
while True:
  print("1-Topla\n2-çıkar\n3-çarp\n4-böl\n0-Çıkış")
  secim=input("Seçiminiz: ")
  if secim=="0":
    print("Programdan çıkılıyor...")
    break #Döngüyü sonlandırır ve döngünün dışına çıkar

while True:
  s=int(input("Sayı giriniz: "))
  if s<=0:
    print("pozitif tam sayı giriniz.")
    continue #Döngüyü burada keser ve döngünün başına döner
  else:
    print(s**4)
    break #Döngüyü sonlandırır ve döngünün dışına çıkar
  print("Burası çalışmaz")
print("Burası çalışır")
"""

h=1
while True:
  k_adi=input("Kullanıcı adınız: ")
  parola=input("Parolanız: ")
  if k_adi=="a" and parola=="1":
    print("Hoşgeldiniz.")
    #....
    break
  else:
    if h==3:
      print("Hakkınız bitti")
      break
    print("Bilgilerinizi kontrol ediniz...")
    print("Kalan Hakkınız:",3-h)
    h+=1


