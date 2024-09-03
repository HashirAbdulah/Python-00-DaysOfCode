# Decorators are functions that takes another functions as Arguments and returns a function.
# They can be used to modify the behavior of a function without changing its source code.



def decorator(transaction):  # The Argument can be any function name or names
    def wrapper():
        print("Transaction Initiated")
        transaction()
        print("Transaction Completed")
        # Additional functionality can be added here if needed
    return wrapper

@decorator
def transaction():
    print( "Transaction Ongoing")
transaction()
