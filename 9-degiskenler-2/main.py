# 1- Aynı değere sahip birden fazla değişken tanımlamak

a=5
b=5
c=5

a=b=c=5

print(c)

k1="a"
k2="a"
k3="a"
k4="a"
k5="a"

k1=k2=k3=k4=k5="a"

print(k4)

kasim=aralik=ocak="KIŞ"
subat=mart=nisan="İLKBAHAR"

# 2- Değişkenlerin değerlerini takas etme
a=5
c=10
print(a/c)

a,c=c,a

print(a/c)

a=8
b=4
c=16

print(c/(a*b)) #16/32 = 0.5

c,a,b=b,c,a

print(c/(a*b))

sinif_baskani="Ali"
sinif_baskan_yard="Ayşe"

sinif_baskani,sinif_baskan_yard=sinif_baskan_yard,sinif_baskani

print(sinif_baskani)
print(sinif_baskan_yard)
