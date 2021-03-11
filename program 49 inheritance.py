class phone:
    def message (self):
        print("message")
    def call (self):
        print ("call")
    def photo (self):
        print("photo")
class samsung(phone):
    pass
a=samsung()
a.call()
a.photo()
a.message()
print(issubclass(samsung,phone))