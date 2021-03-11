file= open ("student.txt","r")
print(file.readable())

text=file.read()
print(text)
size=len(text)
print(size)
text=file.readlines()
print(text)

for line in file:
 print(line)

file.close()
'''
print(file.readable())
print(file.readlines())
for line in file:
text=file.read()
print(text)
 print(line)'''
file=open("student.txt","r")

print(file.readlines()[0])
file.close()