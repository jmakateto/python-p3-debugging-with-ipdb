import ipdb

def my_function():
    my_variable = "Hello, debugging!"
    print(my_variable)
    ipdb.set_trace()
    print("After setting the trace")
my_function()
