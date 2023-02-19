# def even(n):
#     return n%2==0
# num=list(range(1,11))
# print(list(filter(even,num)))   
# another
def even(n):
    return n%2==0
num=list(range(1,11))
def my_filter(fun,iterable):
    new=[]
    for i in iterable:
        if fun(i)==True:
            new.append(i)
    return iter(new)
print(list(my_filter(even,num)))            