# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
def filter():
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in list:
        if (list[i]%2 == 0):
            print(list[i])
        else:
            pass
filter()
            