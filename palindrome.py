#palindrome
d=0
r=0
num = int(input("Enter a number :"))
temp = num
while (temp>0):
    d=temp%10
    r=(r*10)+d
    temp=temp//10
if num==r:
    print(True)
else:
    print(False)