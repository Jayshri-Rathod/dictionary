var="MISSISSIPPI"
new_dict={}
for i in var:
    if i not in new_dict:
        new_dict[i]=1
    else:
        new_dict[i]+=1
print(new_dict)
    

