import ipdb

def add_two(num):
    num = num + 2
    ipdb.set_trace()
    return num


result = add_two(3)
print(result)
