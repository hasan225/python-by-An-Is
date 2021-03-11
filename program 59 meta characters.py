import re
#1 pattern ..= r"s..p."
#2 pattern ^$= r"^s..p.$"
#3 pattern *= r"(ab)*"
#4 pattern += r"b+"
#5 pattern ?= r"ice(-)?cream"
#6 pattern {}$= r"a{1}$"
#7 pattern \= r"sha\.p."
#8 pattern []= r"sh[ae]pe"
#9 pattern [^]= r"[^0-5]"
#10 pattern  \(|)= r"[\w.]+@\w+\.(net|edu|com)"
pattern = r"[\w.]+@\w+\.(net|edu|com)"
if re.match(pattern,"uzumakibijoy2017@gmail.com uzumakibijoy2017@gmail.net uzumakibijoy2017@gmail.edu"):
    print("matched")
else:
    print("not matched")





