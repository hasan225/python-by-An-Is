def square (x):
    return x*x
num =[1,2,3,4,5,6]
result=list(map(square,num))

print(result)
num =[1,2,3,4,5,6]
result=list(map(lambda x: x*x,num))
print(result)


num = [1,2,3,4,5,6,7,8]
result=list(filter(lambda x: x%2==0,num))
print(result)

def even(num):
    for x in num:
        if x%2 == 0:
            print(x)
num = [1,2,3,4,5,6,7]
print(even(num))


#trying-

def square (x):
    return x*x
num =[1,2,3,4,5]
result =list(map(square,num))
print(result)
num=[1,2,3,4,5,6]
result=list(map(lambda x: x*x,num))
print(result)
number=[1,2,3,4,5,6,7,8]
result=list(filter(lambda x: x%2==0,num))
print(result)