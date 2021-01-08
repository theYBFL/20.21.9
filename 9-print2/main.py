#print() fonk.

#NOT-Birden fazla parametre varsa aralarına virgül koyarız.
print("a","b","c")
print("a",1,4.5,False)


#Özel Parametreler
  #1 - sep (seperator): Parametreler arasına hangi karakterin geleceğini belirler
  #Varsayılan değeri bir boşluk karakteridir.

print(11,12,13,14)
print(11,12,13,14,sep=" ")
print(11,12,13,14,sep="-") # parametreler arasına -(tire) ekledim
print(11,12,13,14,sep="0 ")

  #2-end : Parametrelerin sonuna hangi karakterin geleceğini belirler
  #Varsayılan değeri bir alt satıra geçmek için kullandığımız "\n" kaçış dizisidir.
print(11,12,13,14,sep="0 ",end="0\n")

print(11,12,13,14,sep="0 ",end="\n")
print(1)
print(2)
print(3)

print("1-Ali\n2-Ayşe\n3-Oğuz")

# Yıldız parametresi
# Başına yıldız parametresi eklenen K.D.nin karakterlerini ayrı ayrı parametrelere böler. 
print("YBFL")
print(*"YBFL") #print("Y","B","F","L")

print(*"YBFL",sep="-")
print(*"abcdefgh...z",sep="_")

# print("abcdefg") >>> "a","b","c","d","e","f","g"
print('"a',*'bcdefg',sep='","',end='"')
print()
# print(1234567) >>> 
"""
1
2
3
4
5
6
7
"""
print(*"1234567",sep="\n")

