# İç içe if 

k_adi="admin"
parola="123"

k_adi2=input("Kullanıcı adınızı giriniz: ")

if k_adi==k_adi2:
  parola2=input("Parolanızı giriniz: ")
  if parola==parola2:
    print("Sisteme hoşgeldiniz.")
  else:
    print("Merhaba",k_adi,"parolanızı kontrol ediniz.")
else:
  print("Kullanıcı adınız yanlış")


# Yapay zeka ile iş görüşmesi :)
# Kullanıcıdan eğitim durumu istenecek(y.lisans-lisans-lise-ortaokul) lisans mezunları kabul edilecek. Kabul edilenlerden mezuniyet derecesi 90-100 arasında ise işe alınacak, 80-90 arasında ise tekrar görüşme yapılacak.

e_durum=input("Eğitim Durumunuz:\n 1-yüksek lisans \n 2-lisans \n 3-lise \n 4-ortaokul \n Seçiminiz: ")

if e_durum=="1" or e_durum=="2":
  print("İlk görüşme olumlu")
  
  m_der=input("Mezuniyet derece notunuz (0-100 arası): ")
  
  if 90<=m_der and m_der<101:
    print("İşe kabul edildiniz.")
  elif 80<=m_der and m_der<90:
    print("Tekrar görüşmek için çağrılacaksınız.")
  else:
    print("Mezuniyet dereceniz bizim için yeterli değil.")

else:
  print("Eğitim durumunuz bizim için yeterli değil.")