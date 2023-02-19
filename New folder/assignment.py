# ##6666666666666Q 6 ######################################################################
# Number=[5,3,876,9,0,34,55,159,34,25,55,65,175]
# num=[]
# for i in Number:
#     if i%5==0 :
#         num.append(i)
#     elif i>150:
#         break    
# print(num)    
## question77777777 7 fabonic0,1,1,2,3,5,8,13,21,34....####################################
# a=0
# b=1
# c=[]
# for i in range(10):
#     c.append(a)
#     a,b=b,a+b
# print(c)    
###question 8888....888..8################################################################
# def cal(a,b):
#     return a+b,a-b
# print(cal(2,4)) 
# print(cal(6,4))  
##question 999.....99.....9###############################################################
def employ(name=" ",salary=9000):
    print(f"name of employee is {name} and it's salary is {salary}")
E1=employ("sunil",5000) 
E2=employ( "ravi") 
E3=employ("karan")
##question.......1000...... 10##########################################################
# # ###could not understand question prorerly
# l1=[7,4,2,9]
# def add(*args):
#     _s=0
#     k=0
#     while _s<=7429:
#         k+=1
#         for i in args:
#             _s+=i
#     return (f"final sum is {_s} number of iteration taken{k}") 
# print(add(*l1)) 
# ####question 11......11111..11#########################################################
# A=int(input("enter a num to chek whether it is even or not"))
# if A%2==0:
#     print("even number")
# else:
#     print("not an even number")  
# 12 12 question 12......12 find given number prime or not##########################################
# B=int(input("enter a num to chek whether it is prime or not")) 
# prime=True
# for i in range(2,B):
#     if B%i==0:
#         primr=False
#         break
# if prime:
#     print("given number is prime")
# else:
#     print("not prime") 
# question 13.......13....13.......1111133333######################################
# def hcf(a,b):
#     hcf1=[]
#     for i in range(1,min(a,b)+1):
#         if a%i==0 and b%i==0:
#             hcf1.append(i)
#     return  hcf1[-1] 
# print(hcf(10,20))
# print(hcf(9,4) )
# print(hcf(4,64)) 
# print(hcf(31,10))        
#####question 14 to check string palindromi or not "radar,level,rotor"
# A=input("inter a string  ")
# a=list(A)
# b=a.reverse
# if a==b:
#   print("it is  palindromi")
# else:
#     print("not a palendromi")
#### another method
# F=input("inter string") 
# K=F[ : :-1]
# if K==F :
#     print(" yes palendromi")
# else:
#     print("not plendromi")    
######### question 15###################################################
# l1=[3,2,6,7,8,44,66,234,244,1,65,78,22,12]
# l2=[]
# for i in l1:
#     if i%2==0:
#         l2.append(i)
#     elif i==1:
#         break
# print(l2)       

