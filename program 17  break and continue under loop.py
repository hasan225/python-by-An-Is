#this works
'''i=1
while i<=20:
    if i ==18:
        break
    print(i)
    i = i + 1
print("hello")


#break works for this
i = 1
while i<=10:
    print(i)
    i=i + 1
    if i==7:
        break

print("hello")'''

i = 1
while i <= 10:
    if i == 7:
        continue
    print(i)
    i = i + 1

print("hello")
