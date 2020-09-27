strr=input("ENTER A STRING :")
dict = {"Digits":0 , "Letters":0}
for c in strr:
    if c.isdigit():
        dict["Digits"]+=1
    elif c.isalpha():
        dict["Letters"]+=1
    else :
        pass
print  ("DIGITS =" , dict["Digits"])
print  ("LETTERS =" , dict["Letters"])