#multi level inheritance
'''
class a:
    def call(self):
        print("called")
class b(a):
    def call2 (self):
        print("called2")
class c(b):
    def call3 (self):
        super().call()
        super().call2()
        print("called3")
m =c()
m.call3()

'''

#multiple inheritance


class a:
    def call(self):
        print("called")
class b:
    def call (self):
        print("called2")
class c(b,a):
    pass
q=c()

q.call()
