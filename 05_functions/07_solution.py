""" def sum_all(*chai):
    return sum(chai) """

# take error need * before parameter *args
""" 
def sum_all(args):
    return sum(args)
 """

""" 
def sum_all(*args):
    return sum(args)
 """

 
def sum_all(*args):
    # print(*args) # return parameter 
    # print(args) # return parameter in under tuple
    # for i in args:
        # print(i**2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

def sum_all_one(*args):
    s=0
    for i in args:
        s=s+i
    return s

print(sum_all_one(1,2,3))