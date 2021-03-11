'''def sum (num,num2):
    print(num + num2)
    print(num,num2)
sum (10,34)'''

def sum (*num):
     print(num)
#sum (10 + 20 + 30)
sum (10+20+30+40)
sum (10 -20-30,40)
sum (10 *20*30,40)
sum (10 /20,30,40)
sum (10 % 20,30,40)
sum (10 //20,30,40)

def add (*bio):
    print(bio)
add (102,"bijoy", 120)
add (103,"hasan", 130)

def num (*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        print(sum)
num(10,20,30)
num(10,20,30,20,32,45)
num(10,20,30)
num(10,20,30)