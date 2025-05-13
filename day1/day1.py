D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
for i,j in D2.items():
    if i not in D1:
        D1[i]=j
print(D1)               
D1 = {'ok': 1, 'nok': 2}
D_INTERSECTION={}
for i,j in D2.items():
    if i in D1:
        D_INTERSECTION[i]=j
print(D_INTERSECTION)       
subs={}
for i,j in D1.items():
    if i not in D2:
        subs[i]=j
print(subs)                  
for i,j in D1.items():
    if i not in D2:
        D2[i]=j
    else:
        D2[i]+=j
print(D2)
       
