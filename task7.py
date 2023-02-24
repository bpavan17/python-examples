
'''
def decorater(n: int):
    def inner(func):
        def a():
            a.count+=1
            if a.count>n:
                raise Exception("invoked only n times.")
            return func()
        a.count=0
        return a
    return inner

@decorater(3)
def funtion():
    print("function")
for i in range(5):
    funtion()



def decoraters(n:int):
    def inner(func):
        func.count=0
        def pavan():
            func.count+=1
            if func.count>n:
                raise Exception("invoked onlu {n} times ")
            return func()
        return pavan
    return inner
    
@decoraters(3)
def foo():
    print('hai this is pavan')
for i in range(5):
    foo()
'''

#Create a decorator function such that when a function is invoked more than N times 
# it should throw an error. 
#Example: 
#@only_n_times(n) 
#def foo(): 


def only_n_times(n: int):
    def decorator(func):
        func.count = 0
        def fun():
            func.count += 1
            if func.count > n:
                raise Exception("Function can only be called " +str(n)+ " times.")
            return func()
        return fun
    return decorator

@only_n_times(3)
def foo():
    print("Function foo is being called.")
for i in range(6):
        foo()