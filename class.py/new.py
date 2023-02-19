class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_spec(self):
        return f'{self.model} {self.price} {self.brand}'
class smartphone(phone):
    def __init__(self,brand,model,price,intmem,ram):
        super().__init__(brand,model,price)
        self.intmem=intmem
        self.ram=ram
    def color(self,a):
        return f'color of phone is {a}'   
s=smartphone("apple","iphone",120000,"234gb","8gb")   
print(s.color("blue")) 
print(s.full_spec())  
pass
# pass
# class Phone:
#     def __init__(self, brand , model_name , price):
#         self.model_name = model_name
#         self.price = price
#         self.brand = brand

#     def full_spec(self):
#         return f'{self.brand} {self.model_name} {self.price}'

#     # def call(self , name):
#     #     return f'call {name}'


# class SmartPhone(Phone):
#     def __init__(self, brand, model_name, price, internal_memory , ram):
#         super().__init__(brand, model_name, price)
#         self.internal_memory = internal_memory
#         self.ram = ram
 
#     def color(self , a):
#         return f'color of phone is {a}'

# s = SmartPhone('apple' , 'iphone 14' , 120000  , '256 GB' , '8GB')


# print(s.color('blue'))
# print(s.full_spec())