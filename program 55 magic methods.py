'''class family:
    def __init__(self,big,little):
        self.big=big
        self.little=little
    def __str__(self):
        return (f"here{self.little},is{self.big}")
    def total (self):
        print(f"here{self.little},is{self.big}")
ittle1=family("here","there")
print(str(ittle1))'''
class student:
    def __init__(self,boys,girls):
        self.boys=boys
        self.girls=girls
    def __ne__(self, other):
        return self.boys==other.boys and self.girls==other.girls
    def __str__(self):
        return (f"sex ={self.girls},sex ={self.boys}")
    def group (self):
        print(f"sex ={self.girls},sex ={self.boys}")
a=student("boys","girls")
a2=student("boys","girls")

#print(str(a2))
print(a!=a2)