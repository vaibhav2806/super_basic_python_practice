# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
#  Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class shape():
    def area(self):
        return 0
class square(shape):
    def __init__(self , l):
        self.length = l
    def area(self):
        a=self.length**2
        return a
myshape = square(3)
print (myshape.area())

