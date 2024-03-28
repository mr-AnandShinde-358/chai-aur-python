username="chaiaurcode"

""" function test(){

} """

""" if True{

} """


# def test():
#     pass

# if True:
#     pass

""" def fun():
    username="chai"
    print(username)

print(username)
fun() """

# scope also called namespace

x=9
""" 
def func2(y):
    z=x+y
    return z

result = func2(1)

print(result) """


#  donot do this
""" def func3():
    global x
    x=88
   
func3()
print(x) """

""" def f1():
    x=88
    def f2():
        print(x)
    return f2
myresult= f1()
myresult() """

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)
# newChai()
# f(2)
print(f(2))
print(g(3))
