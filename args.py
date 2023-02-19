# def add(*args):
#     add=0
#     for i in args:
#         add+=i
#     return add
# print(add(1,2,2,3,4,1)) 
# ###another 
def add(*args):
    add=0
    for i in args:
        add+=i
    return add  
num=list(range(1,6))
print(add(*num))
# ###another mul
# def mul(*args):
#     mul=1
#     for i in args:
#         mul*=i
#     return mul
# num=list(range(1,6)) 
# print(mul(num))
# print(mul(*num))   
