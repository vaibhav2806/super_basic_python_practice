# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.
def printLIST():
    list = []
    for i in range (1,21):
        list.append(i**2)
    print(list)
    print(list[-5:])
    print(list[0:-5])
printLIST()