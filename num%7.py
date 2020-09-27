n = int(input("ENTER THE LIMIT : "))
def putnum(n):
    i=0
    while i < n:
        j = i
        temp = j%7
        if temp == 0:
            print ("NUMBER DIVISIBLE BY 7 IS :", i)
        else:
            pass
        i=i+1
putnum(n)