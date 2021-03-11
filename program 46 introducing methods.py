class student:
    roll =""
    gpa =""


    def value (self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def school(self):
        print(f"stu roll ={self.roll}, stu gpa ={self.gpa}")



bijoy = student()
print(isinstance(bijoy,student))
bijoy.value(100,3.61)
bijoy.school()

joy = student()
print(isinstance(joy,student))
joy.roll= 101
joy.gpa=3.68
joy.school()

jui = student()
print(isinstance(jui,student))
jui.roll= 102
jui.gpa=3.65
jui.school()









'''class student:
    roll =""
    gpa =""

    def school(studen):
        print(f"roll: {studen.roll}, gpa :{studen.gpa}")
bijoy = student()
print(isinstance(bijoy,student))
bijoy.roll= 100
bijoy.gpa=3.61
bijoy.school()


joy = student()
print(isinstance(joy,student))
joy.roll= 101
joy.gpa=3.68
joy.school()

jui = student()
print(isinstance(jui,student))
jui.roll= 102
jui.gpa=3.65
jui.school()'''

