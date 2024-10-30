from random import randint
question = str(input("Question: "))
random = randint(1,9)
if random == 1:
  print("Yes - definitely.")
elif random == 2:
  print("It is decidedly so.")
elif random == 3:
  print("Without a doubt.")
elif random == 4:
  print("Reply hazy, try again.")
elif random == 5:
  print("Ask again later.")
elif random == 6:
  print("Better not tell you now.")
elif random == 7:
  print("My sources say no.")
else:
  print("Outlook not so good.")

