input = [1,2,3, [1,2,3,[3,4],2]]
##output = [1,2,3,1,2,3,3,4,2]
def fltlist(lswt):
    lst=[]
    for i in lswt:
        if type(i) == list:
            lst.extend(fltlist(i))
        else:
            lst.append(i)
    return lst
print(fltlist(input))
#Q-2
input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
#output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
# Convert string tuples to nested numerical lists
def p(lst):
    for i in lst:
        if type(i) == list:
            p(i)
        else:
            lst[lst.index(i)]=[int(i) for i in i.strip("'( )'").split(",")]
    return input
print(p(input))
