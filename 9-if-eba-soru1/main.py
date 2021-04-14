"""
Bir kıyafet dükkanı açan Sinan, hesap işlerine bakmak için kasiyer işe almak istemiyor. Hesabı kafasından yapamayacağını düşünen Sinan, bu iş için para harcamak istemiyor. Bunun için bir kod kullanmak istiyor. Ama yazılım işinden anlamadığından sizden yardım istiyor. Dükkanda gömlek, pantolon, atkı, şapka, eldiven ve kazak satan Sinan, 500TL'yi aşan fiyatın yarısı kadar indirim yapıyor. (500 TL ve üstü değil, 500TL üzeri) Örneğin, 650TL'lik alışverişte 500TL'yi aşan 150TL'nin yarısı kadar yani 75TL indirim yapıp müşterisinden 575TL alıyor.Dükkanda:-Kazak Çeşitleri: 50TL-Pantolon Çeşitleri: 75TL-Gömlek Çeşitleri: 115TL-Atkı, Şapka ve Eldiven Çeşitlerinin Her Biri: 25TL dir.Buna göre, Sinan'a her çeşitten kaçar ürün aldığını soran ve cevaba göre hesap yapıp ödemesi gereken miktarı Sinan'a çıktı olarak veren kodu yazınız.NOT: Girdiler ve çıktılar tam sayıdır.
"""

kazak=int(input("Kazak adedi: "))*50
pantolon=int(input("Pantolon adedi: "))*75
gomlek=int(input("Gömlek adedi: "))*115
diger=int(input("Diğer adedi: "))*25

tutar=kazak+pantolon+gomlek+diger

if tutar>500:
    odenecek=tutar-((tutar-500)/2)
    print("Toplamda",tutar,"₺")
    print("İndirimle birlikte ödenecek miktar:",odenecek,"₺")
else:
    print("Ödenecek Miktar:",tutar,"₺")
