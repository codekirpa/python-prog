# def square(n):
#     return n**2
# num=list(range(1,11))
# print(list(map(square,num)))   
#with lamda
# n=list(map(lambda n: n**2,list(range(1,11))))
# print(n)
#withot using map
def square(n):
    return n**2
num=list(range(1,11))
def my_map(fun,iterables):
    new=[]
    for i in iterables:
        new.append(fun(i))
    return iter(new)   
print(list(my_map(square,num)))
     
