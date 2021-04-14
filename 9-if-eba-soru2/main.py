"""
Murat, işe alacağı kişiler arasında torpil yapmamak için her sorduğu soruya puan veriyor. Hesap işiyle uğraşmamak için bir kod yazmak istiyor. Ama kod yazacak vakti yok. Murat için bu kodu yazar mısınız? Sorular:Kaç dil biliyorsun? Dil başına 5 puan.İngilizce seviyen 6 seviyeden(A1 A2 B1 B2 C1 C2) kaçıncısı? Verdiği sayının 4 katı puan.Staj yapalı kaç yıl oldu? Yıl sayısı x 4 puan47 puan ve üstü işe alınır. İşe alınan kişiye "Ise Alindiniz", alınmayan kişiye ise "Maalesef Sizinle Calisamayacagiz" yazdırmalıdır.NOT: Tüm girdiler tamsayıdır.
"""

kac_dil=int(input("Kaç dil biliyorsunuz: "))*5
ing_seviye=int(input("1-A1\t2-A2\t3-B1\t4-B2\t5-C1\t6-C2\nİngilizce seviyeniz(1..6): "))*4
staj_yili=int(input("Kaç yıl staj yaptınız:"))*4

puan=kac_dil+ing_seviye+staj_yili

if puan>=47:
    print("İşe alındınız.")
else:
    print("Maalesef sizinle çalışamayacağız.")
