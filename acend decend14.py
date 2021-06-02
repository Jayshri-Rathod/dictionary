new={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic={}
for i in new:
    a=new[i] 
    for i in new:
        b=new[i]
        if a>b:
            dic[i]=b            
for i in new:
    a=new[i]
    for i in new:
        b=new[i]
        if a<b:
            dic[i]=b    
print(dic)

# for i in new:
#     a=new[i] 
#     for i in new:
#         b=new[i]
#         if a<b:
#             dic[i]=b
            
# for i in new:
#     a=new[i]
#     for i in new:
#         b=new[i]
#         if a>b:
#             dic[i]=b    
# print(dic)















# a=sorted(new.values())
# print(a)
# dic={}
# for i in a:
#     for j in new.keys():
#         if new[j]==i:
#             dic[j]=new[j]
# print(dic)

