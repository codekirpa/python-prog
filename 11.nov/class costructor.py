class emp:
    def __init__(self,name,salary,company):
        self.nam=name
        self.sal=salary
        self.comp=company
        print("emplyoee is created")
    def getdet(self):
        print(f"name of emplyoee is {self.nam} and")
        print(f"his salary is {self.sal}") 
        print(f"company name is{self.comp}")   
harry=emp("harry",100,"goole")
punit=emp("punit",100,"youtube")
harry.getdet()####emp.getdet(harry)
emp.getdet(punit)#####punit.getdet()