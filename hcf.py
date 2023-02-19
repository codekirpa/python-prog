# def hcf(a,b):
#     for i in range(1,min(a,b)+1):
#         if a%i==0 and b%i==0:
#             hcf1=i
#     return hcf1        
# print(hcf(10,20)) 
# print(hcf(10,31))
##program to find lcm cannot use prime
def lcm(a,b):
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            lcm1=i
            break
    return lcm1        
print(lcm(8,28)) 
print(lcm(10,30))