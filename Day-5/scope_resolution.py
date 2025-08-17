#variable scope = where a variable is both visible and accessible
#Scope Resolution = Local -> Enclosed -> Global -> Built-in

def func1():
    x=1
    print(x)
def func2():
    y=2
    print(y)
# x and y have local scope and cant use in different function

func1()
func2()

x=3
def func1():
    print(x)
def func2():
    print(x)
#Here x has a global scope
func1()
func2()

from math import e
def func1():
    print(e)
#e has built-in scope. But if we declare e inside the function "e=4" then it will have local scope coz of the LEGB order
func1()