# def fun():
#     print("sunil")
# fun2=fun
# del fun
# # fun2()   
# def fun3(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# print(fun3(0)) 
# l1=[1,2,3]           
# def exe(fun1):
#    print(fun1(l1))
# exe(sum)
def dec1(fun1):
    def nowex():
        print("exe1")
        fun1()
        print("exe2")
    return nowex
@dec1    
def who_is():
    print("harry good boy")
# who_is=dec1(who_is) 
who_is()       

