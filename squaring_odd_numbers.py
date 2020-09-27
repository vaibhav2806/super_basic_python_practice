list = []
n = int(input("ENTER NUMBER OF INPUTS :"))
i = 1
while i<=n:
    num = int(input("ENTER A NUMBER :"))
    if (num % 2 != 0):
        a = num*num
        list.append(a)
        print(list)
    else:
        pass 
    i=i+1


