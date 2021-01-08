#print() fonk. - Ekrana herhangi bir verinin çıktısını almak için kullanılır
  #print(...parametre...)
  #NOT-Birden fazla parametre varsa aralarına virgül koyarız.

print("Merhaba")
print(89)
print(8.5)
print(True)

sifre="1dg%Tr3+"
print(sifre)

#1 - Tek Tırnak ('...')
print('Tek tırnaklı yazım')

# Atatürk'ün doğum yılı 1881'dir.
#print('Atatürk'ün doğum yılı 1881'dir.') #Hata verir
print("Atatürk'ün doğum yılı 1881'dir.")

#2 - Çift Tırnak ("...")
print("Çif tırnaklı yazım")

#Bugün "print()" fonksiyonunu işledik.
#print("Bugün "print()" fonksiyonunu işledik.") #Hata verir
print('Bugün "print()" fonksiyonunu işledik.')

#3 - Üç Tırnak ("""...""")-('''...''')
# Satır satır yazı yazmak için kullanılır.
# 1-Ali
# 2-Ayşe
# 3-Oğuz
#print("1-Ali")
#print("2-Ayşe")
#print("3-Oğuz")
print("""1-Ali
2-Ayşe
3-Oğuz""")

# Hem çift hemde tek tırnak olan metinler?
# Atatürk'ün doğum yılı 1881'dir. Doğduğu yer "Selanik"tir.
#print("Atatürk'ün doğum yılı 1881'dir. Doğduğu yer "Selanik"tir.") #Hata verir
#print('Atatürk'ün doğum yılı 1881'dir. Doğduğu yer "Selanik"tir.') #Hata verir

#1.Yol - Üç tırnak ile
print("""Atatürk'ün doğum yılı 1881'dir. Doğduğu yer "Selanik"tir.""")

#2.Yol - Kaçış dizisi ile (\) 
print('Atatürk\'ün doğum yılı 1881\'dir. Doğduğu yer "Selanik"tir.')
print("Atatürk'ün doğum yılı 1881'dir. Doğduğu yer \"Selanik\"tir.")