# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def printLIST():
    list = []
    for i in range(1,21):
        list.append(i**2)
    print(list)
    print(list[0:5])
printLIST()