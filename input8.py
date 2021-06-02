# i=1
# a=[]
# b=[]
# while i<11:
#     student_name=input("enter name :")
#     marks=input("enter marks :")
#     a.append(student_name)
#     b.append(marks)
#     i+=1
# dic={}
# j=0
# e=[]
# while j<len(a):
#     d=a[j],b[j]
#     j+=1
#     e.append(d)
# dic.update(e)
# print(dic)


dic={}
for i in range(2):
    student_name=input("enter name")
    marks=int(input("enter marks"))
    dic.update({student_name:marks})
print(dic)