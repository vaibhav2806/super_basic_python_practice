#  Define a custom exception class which takes a string message as attribute.
class myerror(Exception):
    """My own exception class
    Attributes:
         
        msg  -- explanation of the error

    """
    def __init__(self, msg):
        self.msg = msg

error = myerror("something is wrong")
