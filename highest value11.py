my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
    'h':90,
    'r':98,
    'l':123456,
    "w":123456789
    }
a=[]
for i in my_dict.values():
    a.append(i)
b=[]
for i in range(3):
    b.append(max(a))
    a.remove(max(a))
print(b)



for i in range(3):
    b.append(a[i])
print(b)

