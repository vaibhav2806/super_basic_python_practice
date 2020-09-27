# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
def printTUPLE():
    tp = (1,2,3,4,5,6,7,8,9,10)
    list=[]
    for i in tp:
        if tp[i]%2 == 0:
            list.append(tp[i])
            print(tuple(list))
printTUPLE()
