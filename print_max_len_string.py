#Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.

def sentence(s1 ,s2):
    a = len(s1)
    b = len(s2)
    if a>b:
        print(s1)
    elif a==b:
        print(s1)
        print(s2)
    else:
        print(s2)
sentence("my name" , "my name is vaibhav")
