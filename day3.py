input = [1,2,3, [1,2,3,[3,4],2]]
##output = [1,2,3,1,2,3,3,4,2]
def fltlist(lswt):
    lst=[]
    for i in lswt:
        if isinstance(i, list):
            lst.extend(fltlist(i))
        else:
            lst.append(i)
    return lst
print(fltlist(input))
