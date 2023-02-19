# class circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return f' {circle.pi*self.radius**2}'   
# c1=circle(4)
# print(c1.area())
######## inheritance 
class phone:
    def _init_(self,brand,model,price):
        self.model=model
        self.price=price
        self.brand=brand
    def full_spec(self):
        return f'{self.model} {self.price} {self.brand}'
class smartphone(phone):
    def __init__(self,brand,model,price,intmem,ram):
        super().__init__(model,price,brand)
        self.intmem=intmem
        self.ram=ram
    def color(self,a):
        return f'color of phone is {a}'   
s=smartphone("apple","iphone",120000,"234gb","8gb")   
print(s.color("blue")) 
print(s.full_spec())    
             