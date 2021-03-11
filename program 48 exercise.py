class triangle():
    def __init__(area,base,height):
        area.base=base
        area.height=height
    def calculate(area):
        area= 0.5 * area.base * area.height
        print(area)

a=triangle(10,20)
a.calculate()
b=triangle(20,30)
b.calculate()
