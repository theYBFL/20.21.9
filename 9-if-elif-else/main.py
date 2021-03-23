x=int(input())
y=int(input())

fark=x-y

if fark>0:
  print("Sayı farkı",fark,"Fark pozitif sayı")
elif fark<0: #Yukarıdaki koşul veya koşullar yanlışsa ve .... koşulu doğruysa
  print("Sayı farkı",fark,"Fark negatif")

else:
  print("Fark yok")