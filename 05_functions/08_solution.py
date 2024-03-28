# * Asterisk
""" def print_kwargs(name,power):
    print("Name: ",name,"power:",power) """


""" def print_kwargs(**kwargs):
    print(kwargs) # its return dictionary
    # for key,value in kwargs.items():
        # print(f"{key}:{value}") """

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}") 

print_kwargs(name="shaktiman",power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(power="lazer")
print_kwargs(name="shaktiman",power="lazer",enemy="Dr.jackaal")