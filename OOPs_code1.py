# Define a class named American and its subclass NewYorker. 
class American(object):
    print("hello american")
class NewYorker(American):
    print("hello newyorker")
anAmerican = American()
anNewYorker = NewYorker()
print(anAmerican)
print(anNewYorker) 