# def greet(name):
#     print(f"hello {name}")
# print(greet("sunil"))
# greet("ravi")   
# def add(n1,n2):
#     result=n1+n2
#     return result
# a=4
# b=4
# print(add(a,b)) 
# k=add(5,6)
# print(k) 
# def greet(name):
#     print(f"hello {name}")
#     return
#     print("not excute")
# greet("harry")    
######
# def add(*args):
#     add=0
#     for i in args:
#         add+=i
#     return add   
# print(add(1,2,3,4,5))
# num=list(range(6)) 
# print(add(*num))  
def fun(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}.......{v}')
fun(name="s",age=30,) 
d={"A":"a","B":"b"}       
fun(**d)

