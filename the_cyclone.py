# Write code below 💖

hight = float(input("Qual é sua altura: "))
credits = float(input("Quanto de credito você tem: "))
if hight >= 1.37 and credits >= 10:
  print("Aprovita o passeio!")
elif hight < 1.37 and credits >= 10:
  print("Você não é alto o suficiente para montar.")
elif hight >= 1.37 and credits < 10:
  print("Você não tem creditos não tem creditos suficientes.")
else:
  print("você não cumpriu nenhum dos requesitos.")