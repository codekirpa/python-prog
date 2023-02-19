# class emp:
#     company="goole"  ###class attributes for each object
#     location="delhi"
# rajni=emp()    
# ravi=emp()
# print(rajni.company)
# print(ravi.location)
# emp.company="traning basket"
# ravi.location="mumbai"
# print(rajni.company)
# print(ravi.location)
# print(rajni.location)
class emp:
    def getdet(self):
        print(f"name is {self.nam} and salary is  {self.sal} ")
harrydet=emp()
harrydet.nam="harry"  
harrydet.sal=100      
savitadet=emp()
savitadet.nam="savita"
savitadet.sal=50
harrydet.getdet() ####emp.getdet(harrydet)
emp.getdet(savitadet)#####savitadet.getdet()