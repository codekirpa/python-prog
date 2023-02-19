# num=list(range(1,11))
# print(num)
# print(*num)
# pass
# def add(*args):
#     add=0
#     for i in args:
#         add+=i
#     return add
# num=list(range(1,11))
# print(add(*num))      
# pass
# def mul(*args):
#     mul=1
#     for i in args:
#         mul*=i
#     return mul
# num=list(range(1,6)) 
# print(mul(num)) 
# print(mul(*num))       
# #######**kwargs for 
# def fun(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}...{v}")
# fun(name="sunil",age="30",hobby="play ")   
# unpacking dict
def fun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}...{v}")
d={"A":"a","B":"b","D":"d"}
fun(**d)

