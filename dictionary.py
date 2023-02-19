# name="sunil kumar mehto nipun darpan"
# emptdict={}
# for i in name:
#     emptdict[i]=name.count(i)
# print(emptdict)    
#same prog with help 
# name="sunil kumar mehto nipun darpan"
# emptdict1={i:name.count(i) for i in name}
# print(emptdict1)
# even1={i:"even" for i in range(1,11) if i%2==0}
# print(even1)
odd_and_even={i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(odd_and_even)

