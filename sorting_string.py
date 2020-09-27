list = []
n =int(input("ENTER NUMBER OF INPUTS :"))
i = 1
while i<=n:
    stringg = input("ENTER A WORD :")
    list.append(stringg)
    list.sort()
    i=i+1
print(list)