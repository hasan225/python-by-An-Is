class student:
    roll =""
    gpa =""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def school(self):
        print(f"stu roll ={self.roll}, stu gpa ={self.gpa}")



bijoy = student(100,3.61)
print(isinstance(bijoy,student))
bijoy.school()

joy=student(102,33)
joy.school()

