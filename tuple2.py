# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
def printTUPLE():
    tuple = (1,2,3,4,5,6,7,8,9,10)
    t1 = tuple[0:5]
    t2 = tuple[-5:]
    print(t1)
    print(t2)
printTUPLE()