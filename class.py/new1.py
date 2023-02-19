class phone:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def getdetail(self):
        return f'specif are {self.model} {self.price}' 
class smartphone(phone):
    def __init__(self,model,price,ram,mem):
        super(). __init__(model,price)
        self.ram=ram
        self.mem=mem
    def color(self,a):
        return f'color is {a}'
s1=smartphone('apple',120000,'12gb','5gb')  
print(s1.color("geer"))  
print(s1.getdetail())  

