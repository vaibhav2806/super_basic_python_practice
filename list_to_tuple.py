n = int(input("ENTER NUMBER OF ELEMENTS :"))
i = 1
list = []
while i<=n:
    num = int(input("ENTER A NUMBER :"))
    i=i+1
    list.append(num)
    t = tuple(list)
print(list)
print(str(t))