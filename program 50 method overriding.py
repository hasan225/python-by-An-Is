'''class phone:
    def __init__(self):
        print("im here")
class samsung(phone):
    def __init__(self):
        super().__init__()
        print("im there")

a =samsung()

'''

class phone:
    def test(self):
        print("im here")
class samsung(phone):
    def test(self):
        super().test()
        print("im there")
   

a =samsung()
a.test()

