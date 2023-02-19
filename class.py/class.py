# class laptop:
#     def __init__(self,ram,memory,price):
#         self.ram=ram
#         self.memory=memory
#         self.price=price
# l1=laptop("5","1tb",35000)
# l2=laptop("7","2tb",40000)        
# print(l1.ram)
# print(l2.memory)
# pass
# class mobile:
#     def __init__(self,gen_name,company_name):
#         self.gen_name=gen_name
#         self.company_name=company_name
# m1=mobile(4,"samsung")
# m2=mobile(5,"redme")  

# print(m1.company_name)     
class tv:
    def __init__(self,company,price):
        self.company=company
        self.price=price
    def fixdiscont(self):
        return self.price-((10/100)*self.price) 
    def vardiscont(self,a):
        return self.price-((a/100)*self.price)

        
t1=tv("samg",40000)
t2=tv("orint",50000)
print(t1.fixdiscont()) 
print(t1.vardiscont(20)) 
print(t2.vardiscont(20))      
