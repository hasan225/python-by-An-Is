'''from random import randint
for x in range(1,6):
   guessnum=int(input("enter :"))

   randomnumber = randint(1,5)
   if guessnum ==randomnumber:
     print("you have won")
   else:
     print("you have lost")
     print("randomnumber",randomnumber)


from random import randint
for x in range (1,6):
  guessnum= int(input("enter"))
  randomnum = randint(1,5)
  if randomnum ==guessnum :
      print("won")

  else:
      print("lost")'''

from random import randint
guessnum =int(input("enter"))
randomnum = randint (1,6)
if randomnum == guessnum:
    print("won")
else:
    print("lost")

