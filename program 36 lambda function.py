'''def cod (a,b):
    return a*a + 2*a*b + b*b
print(cod(2,3))'''

a= (lambda a,b:a*a + 2*a*b + b*b)(2,3)
print(a)
a=(lambda a,b:a*a+2*a*b+b*b) (2,3)
print(a)

a = (lambda x: x*x*x) (3)
print(a)

def cube (x):
    return x*x*x

print(cube(2))