###get the key corresponding to minim value of scor
# marks=[{"name":"Sampark","score":95,"age":23,},{"name":"Rahul","score":78,"age":24,},
# {"name":"Harshit","score":86,"age":22,}]
# s=min(marks,key=lambda a: a.get("score"))
# print(s.keys())
# print(s.values())
##### hcf of two num by lambda
# hcf1=lambda a,b: [i for i in range(1,min(a,b)+1) if a%i==0 and b%i==0][-1]
# print(hcf1(10,20))
# #####first 100 prime
# A=100
# i=[]
# k=1
# while len(i)<=A:
#     prime=True
#     for j in range(2,k):
#         if k%j==0:
#             prime=False
#             break
#     if prime:
#         i.append(k)
#     k+=1
# print(i)            
##### with lamba
#### with lambda and compherisition could not done
######question 4444
# marks=[{"name":"Sampark","score":95,"age":23,},{"name":"Rahul","score":78,"age":24,},
# {"name":"Harshit","score":86,"age":22,}]
# s=max(marks,key=lambda a: a.get("score"))
# print(s.keys())
# print(s.values())
#######question 5555
# Name=["krishana","prem","PK","nidhi","prem","gunjan","prem","sampark","rahul"]
# count_=0
# last_prem=-1
# count2=0
# for i in range(len(Name)):
#     if Name[i]=="prem":
#         count_+=1
# for j in range(len(Name)): 
#     if count2==count_:
#         break      
#     if Name[j]=="prem":
#         count2+=1 
#     last_prem+=1      
# print(last_prem)

 
#####question 66666
# Name="prem Bharti"
# ct={}
# for i in Name:
#     ct[i]=Name.count(i)
# print(ct)    
###### question 7
print(list(filter(lambda n:n%2==0,(3,4,5,7,8,98,56,4,55))))




   
   