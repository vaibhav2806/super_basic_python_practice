dict = {"UPPER CASE":0 , "LOWER CASE":0}
strr = input("ENTER A STRING :")
for c in strr:
    if c.isupper():
        dict["UPPER CASE"]+=1
    elif c.islower():
        dict["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE :", dict["UPPER CASE"])
print("LOWER CASE :", dict["LOWER CASE"])
