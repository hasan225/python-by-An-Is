try:
 num=int(input("num"))
 num2=int(input("num2"))
 sum = num / num2
 print(sum)
except (ZeroDivisionError,ValueError):
 print("susume")
#except ValueError:
 print("susume at full speed")
finally:
 print("yosh")

