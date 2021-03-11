class student:
    roll =""
    gpa =""
bijoy = student()
print(isinstance(bijoy,student))
bijoy.roll= 100
bijoy.gpa=3.61
print(f"bijoy roll ={bijoy.roll}, bijoy gpa ={bijoy.gpa}")

joy = student()
print(isinstance(joy,student))
joy.roll= 101
joy.gpa=3.68
print(f"joy roll ={joy.roll}, joy gpa ={joy.gpa}")

jui = student()
print(isinstance(jui,student))
jui.roll= 102
jui.gpa=3.65
print(f"jui roll ={jui.roll}, jui gpa ={jui.gpa}")



