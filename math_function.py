import math
listA = []
listB = []
C = 50
H = 30
i=1
n = int(input("ENETR THE NUMBER OF INPUTS :"))
while i<=n:
    D = int(input("ENTER A NUMBER :"))
    Q = str(int(round(math.sqrt((2*C*D)/H))))
    i = i+1
    listA.append(str(D))
    listB.append(str(Q))
print(listA)
print(listB)
