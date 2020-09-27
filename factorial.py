list = []
i = 1
fact = 1
num = int(input("ENTER A NUMBER :"))
while i<=num:
    fact=fact*i
    i=i+1
    list.append(fact)
print(list)