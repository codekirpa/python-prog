# #####revesersing integet
# A=12345
# a=str(A)
# a=a[: :-1]
# c=int(a)
# print(c)
######q3 check number is prime or not
# a1=int(input("inter an integer"))
# prime=True
# for i in range(2,a1):
#     if a1%i==0:
#         prime=False
# if prime :
#     print('number is prime')
# else :
#     print('number is not prime')  
# ######fabinoic series q444444
# a2=int(input("enter number of element of fabionic series "))  
# a3=0
# b=1
# for i in range(a2):
#     print(a3)
#     a3,b=b,b+a3
#############q55555555555555 find greatest among three
# b1,b2,b3=input("enter three number seperate by comma ").split(",")
# b1=int(b1)
# b2=int(b2)
# b3=int(b3)
# if b1>b2 and b1>b3:
#     print(b1,"is greater")
# elif b2>b1 and b2>b3:
#     print(b2,"is greater")
# else:
#     print(b3,"is greater")  
# ######q666666666 find average of n numbers
# n=int(input('inter the value of n'))  
# l1=list(range(1,n+1))  
# average=sum(l1)/len(l1)
# print(average)
########q7777777 factorial by recurtion
# a6=int(input("inter num to find factorial"))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(a6))            

########q88888######88888to chek even or odd
# k=int(input("enter number to chek "))
# chek=lambda a5:["even" if a5%2==0 else "odd"]
# print(chek(k))
#####q99999 ###############smallest number among 3
# b1,b2,b3=input("enter three number seperate by comma ").split(",")
# b1=int(b1)
# b2=int(b2)
# b3=int(b3)
# if b1<b2 and b1<b3:
#     print(b1,"is smallest")
# elif b2<b1 and b2<b3:
#     print(b2,"is smallest")
# else:
#     print(b3,"is smallest")
#########q10....10...#####lcm
# l7=[]
# a=int(input("enter first value"))
# b=int(input("enter second value"))
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         l7.append(i)
           
# lcm=(a*b)/l7[-1]
# print(lcm ,"is lcm")
#############q12.......12....12 hcf of two num
# l8=[]
# a=int(input("enter first value"))
# b=int(input("enter second value"))
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         l8.append(i)
           
# hcf=l8[-1]
# print(hcf ,"is hcf")
# #########programm to convert celsius to fahrenheitq13....13
# celsius=int(input("enter temp in celsius "))
# f=((9/5)*celsius)+32
# print(f"temp in fahrenheit is {f}")
##############q no14  .....14########## to chek vowel or consonent
A=input("enter any string ")
A1=A.lower()
if A1=="a" or A1=="e"or A1=="i"or A1=="o"or A1=="u":
    print("this is an vowel")
else:
    print("its a consonent")    




