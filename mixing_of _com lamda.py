# hcf=lambda a,b:[i for i in range(1,min(a,b)+1) if a%i==0 and b%i==0]
# print(hcf(10,20))
hcf=lambda a,b:[i for i in range(1,min(a,b)+1) if a%i==0 and b%i==0][-1]
print(hcf(10,20))