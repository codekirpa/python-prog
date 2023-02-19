name='sunil kumareee'
ch={}
for i in name:
    ch[i]=name.count(i)
print(ch)    
kt=max(ch.values())
print(kt)
for k,v in ch.items():
      if v==kt:
          print(k)