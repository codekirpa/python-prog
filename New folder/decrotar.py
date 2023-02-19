# def dec_(any_fun):
#     def warp_():
#         print("this is wrap func")
#         return any_fun
# #     return warp_    
# def num(n):
#     for i in range(1,n+1):
#         yield(i)
# a=num(10)  
# for i in a:
#     print(i)    
import time
t1=time.time()
g=(i**2 for i in range(10000000))
t2=time.time()
print(t2-t1) 