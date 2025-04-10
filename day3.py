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
#Q-2
input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
#output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
# Convert string tuples to nested numerical lists
output = [[[list(map(int, eval(t))) for t in sublist] for sublist in mainlist] for mainlist in input]

print(output)
