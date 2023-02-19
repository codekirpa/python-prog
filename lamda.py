# add1= lambda a, b: a+b
# print(add1(2,7))
#another one
# hello=lambda : print("hello")
# print(hello())
#another
# func=lambda name: True if len(name)>5 else False
# print(func("sunil"))
# print(func("sunilkumar"))
#comprehention
# num=[i for i in range(1,10)]
# num2={j for j in range(1,5)} # append,loop
# print(num)
# print(num2)
#append,loop , condition (single condition)
# odd=[i for i in range(1,11) if i%2!=0]
# print(odd)
# append condition loop (two condition)
mix={i*2 if i%2==0 else i*3 for i in range(1,11)}
print(mix)
