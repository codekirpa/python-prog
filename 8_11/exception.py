try:
    age=int(input("enter age"))
except ValueError :
    print("please enter age in num")
else:
    if age>18:
        print("you can watch movi")
    else:
        print("you cannot watch movi") 
finally:
    print("hello ")               
# while True:
#     try:
#      age=int(input("enter age"))
#      break
#     except ValueError:
#      print("please enter age in num")
# if age>18:
#     print("you can watch movi")
# else:
#     print("you cannot watch movi") 
