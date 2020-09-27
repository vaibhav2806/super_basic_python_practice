import re 
list = []
i=1 
n=int(input("ENTER THE NUMBER OF INPUTS: "))
while i<=n:
    p = input("ENTER A PASSWORD :")
    i = i+1
    if (len(p)>6) and (len(p)<12):
        if re.search("[0-9]", p):
            if re.search("[a-z]", p):
                if re.search("[A-Z]", p):
                    if re.search("[@#$]", p):
                        list.append(p)
    print("PASSWORD VERIFIED : ", list)