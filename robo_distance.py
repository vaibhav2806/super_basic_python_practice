import math
pos = [0,0]
i=0
n = int(input("ENTER THE NUMBER OF COMMANDS YOU WANT TO GIVE : "))
while i<n:
    steps = input("UP/DOWN/LEFT/RIGHT : ")
    if steps == "":
        print("you need to enter something!!")
    else:
        pass
    if steps == "UP":
        pos[0] = pos[0]+1
    elif steps == "DOWN":
        pos[0] = pos[0]-1
    elif steps == "LEFT":
        pos[1] = pos[1]-1
    elif steps == "RIGHT":
        pos[1] = pos[1]+1
    i = i+1
c = int(math.sqrt(pos[1]**2 + pos[0]**2))
print ("Distance =", c)
