# def outerfun(msg):
#     def innerfun():
#         print(f"inner function {msg}")
#     return innerfun
# a=outerfun("hello sunil") 
# a()      
# def to_power(x):
#     def cal_pow(n):
#         return n**x
#     return cal_pow
# cube=to_power(2)
# print(cube(3)) 
# def dec_fun(any_fun):
#     def wrappfun():
#         print("fist execution")
#         any_fun()
#         print("second execution")   
#     return wrappfun  
# def helloji():
#     print("in between")
# a=dec_fun(helloji)    
# a()
def dec_fun(any_fun):
    def wrappfun():
        print("fist execution")
        any_fun()
        print("second execution")   
    return wrappfun
@dec_fun      
def helloji():
    print("in between")
helloji()  



           