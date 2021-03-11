'''import re
pattern = "col"
if(re.match(pattern,"red is my favorite colour")):
    print("match")
else:
    print("not match")
import re
pattern=r"school"
text="our school is near our house , it takes us like 10 minutes to reach school, school "
find=re.search(pattern,text)
print(find.start())
print(find.end())
print(find.span())

import re
pattern=r"kind"
print(re.search(pattern,"i have been kind, i have been cruel"))
print(re.match(pattern,"you can rather be kind then telling someone to be kind"))
print(re.findall(pattern,"you cant expect someone to be kind in this cruel world"))

import re
pattern="you
text="you never get what you actually want"li
program=re.search(pattern,text)
if program:
    print(program.start())
    print(program.end())
    print(program.span())
import re
pattern=r"you"
text="hey there how are you im doing okay thanks for asking"
program =re.search(pattern,text)
if program:
    print(program.start())
    print(program.end())
    print(program.span())'''

import re
pattern=r"im"
text="im bijoy im a student"
method=re.match(pattern,text)
if method:
    print(method.start())
    print(method.end())
    print(method.span())
