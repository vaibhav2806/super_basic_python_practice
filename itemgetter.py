# itemgetter to generate multiple sort keys
from operator import itemgetter , attrgetter
list = []
n = int(input("ENTER THE NUMBER OF INPUTS YOU WANT TO MAKE :"))
i = 0
while i < n:
    p = input("ENTER DETAILS :")
    list.append(tuple(p.split(",")))
    i=i+1
print (sorted(list , key=itemgetter(0,1,2)))

