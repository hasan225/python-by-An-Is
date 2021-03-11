''' n =input("enter")
list = n.split ()
sum = 0
for num in list:
   sum =sum +int (num)

print (sum)
'''
numofwords = 0
numofletters = 0
numofdigits = 0

text = input ("inter text")

for x in text:
    x =x.lower()
    if x>='a' and x<='z':
        numofletters = numofletters + 1
    elif x>='0' and x<='9':
        numofdigits = numofdigits + 1
    elif x==' ':
        numofwords = numofwords + 1
print(numofwords +1)
print(numofletters)
print(numofdigits)

