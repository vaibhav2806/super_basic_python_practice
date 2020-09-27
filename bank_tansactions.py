dict = {"BALANCE":10 , "DEPOSIT":0 , "WITHDRAW":0}
if dict["BALANCE"]==0:
     print ("DEPOSIT MONEY INTO YOUR BANK ACCOUNT ")
     D = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT :"))
     dict["BALANCE"]+= D
     dict["DEPOSIT"] = D    
     print("DEPOSIT = ", dict["DEPOSIT"])
     print("BALANCE = ", dict["BALANCE"])
     print("""TRANSACTION COMPLETED.
     THANK YOU""")
elif dict["BALANCE"]!=0:
     print ("YOU WANT TO DEPOSIT OR WITHDRAW AMOUNT???")
     CHOICE = input("ENTER YOUR CHOICE D OR W :")
     print
     if CHOICE=="D":
         D = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT :"))
         dict["BALANCE"] += D
         print("DEPOSIT = ", dict["DEPOSIT"])
         print("BALANCE = ", dict["BALANCE"])
         print("""TRANSACTION COMPLETED.
         THANK YOU""")
     elif CHOICE=="W":
          W = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW :"))
          dict["BALANCE"] -= W
          print("WITHDRAWAL = ", dict["WITHDRAW"])
          print("BALANCE = ", dict["BALANCE"])
          print("""TRANSACTION COMPLETED.
          THANK YOU""")
     else:
          print("""WRONG CHOICE!!! PLEASE CHOOSE AMOUNG D AND W.
          THANK YOU.""" )
else:
    pass


