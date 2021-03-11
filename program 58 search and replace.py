import re
pattern= r"a"
text="a is a letter,a is used in many places,a is the first word every one begin with"
change=re.sub(pattern,"e",text,count=1)
print(change)
0