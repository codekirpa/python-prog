def funct(**kwarg):
    for k,v in kwarg.items():
        print(f"{k}....{v}")
funct(sunil="name",age="30",hobby="play") 
d={"A":"a","B":"b","Q":"q"} 
funct(**d)     