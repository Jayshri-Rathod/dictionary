list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
dic={}
i=0
a=[]
while i<len(list1):
    b=list1[i],list2[i]
    i+=1
    a.append(b)
print(a)
dic.update(a)
print(dic)
# s={}
# for i in range(len(list1)):
#     s.update({list1[i]:list2[i]})
# print(s)
