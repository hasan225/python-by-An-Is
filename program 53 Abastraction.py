from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def area(self):
         pass
        #print("okay to go")
class triangle(shape):
    def area(self):
     area = 0.5 * self.dim1 * self.dim2
     print("done here",area)
class rectangle(shape):
    def area(self):
     area = self.dim1 * self.dim2
     print("done here2" , area)

a=triangle(20,30)
a.area()
a2=rectangle(20,30)
a2.area()





