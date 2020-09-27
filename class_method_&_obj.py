class with2methods:
    def __init__(self):
        self.stringg = " "

    def getString(self):
        self.stringg = input("ENTER A STRING :")

    def printString(self):
        print(self.stringg.upper())

strOBJ = with2methods()
strOBJ.getString()
strOBJ.printString()