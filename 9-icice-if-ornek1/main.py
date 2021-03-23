""" Okul yemekhanesinde
- Öğrenci ise yemek ücreti 10₺
  - 9 ve 10. sınıflara %10 indirim
  - 11 ve 12. sınıflara %15 indirim
- Öğretmen ise yemek ücreti 15₺
ücretler yukarıdaki gibidir.
Ekranda ödenecek tutarı gösteriniz.
"""

durum=input("1-Öğrenci \n2-Öğretmen \nSeçiminiz:")

if durum=="1":
  sinif=input("Kaçıncı sınıf (9-10-11-12): ")
  if sinif=="9" or sinif=="10":
    print(10-10*0.1,"₺")
  elif sinif=="11" or sinif=="12":
    print(10-10*0.15,"₺")
  else:
    print("Yanlış bir seçim yaptınız.")

elif durum=="2":
  print("Ödenecek tutar 15₺")
else:
  print("Yanlış bir seçim yaptınız.")



