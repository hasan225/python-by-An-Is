'''#map
num = [1,2,3,4,5,6,7,8]
#[expression for item(x) in list]
result=[x*x for x in num]
print(result)
#filter
num =[1,2,3,4,5,6,7,8]
result=[x for x in num if x%2==0 ]
print(result)'''
#test subs
num=[2,23,4,4,5,6,78,8]
result=[x*x for x in num]
print(result)
result=[x for x in num if x%2==0]
print(result)
result=[x+x for x in num]
print(result)
result=[x-x for x in num]
print(result)b