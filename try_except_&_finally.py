# Write a function to compute 5/0 and use try/except to catch the exceptions.
def throw():
    return 5/0
try:
    throw()
except ZeroDivisionError:
    print ("Division by zero!!")
except Exception:
    print("Caught an Error!!")
finally:
    print("finally in the finally block.")
