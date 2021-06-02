dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# dic2.update(dic3)
# dic1.update(dic2)
# dic1[2]=20+50
# print(dic1)                                                                                                                                                                                               
dict4={}
dict4.update(dic1)
dict4.update(dic2) 
dict4.update(dic3)
# print(dic)

dic4={}

for i in dic1:
    for j in dic2:
        for b in dic3:
            if i==j:
                a=dic1[i]+dic2[j]
                dic4[i]=a
# print(dic)

dict4={}      
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)

for k in dic4:
    for l in dict4:
        if k==l:
            dict4[k]=dic4[l]
            break
print(dict4)
        



