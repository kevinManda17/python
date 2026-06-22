#coding: utf-8 

# user= " kevin"
user =" keven"

def deco(fonction):
    
    def other_function():
        print("action refusee ")

    if user == "kevin ":
        return other_function()
    
    return fonction

@deco
def do_that():
    print("Execution des instructions ")

do_that()

def deco1(fonction):
    def other_function1(*param, **param2):
        print("Action avant ... ")
        fonction(*param , **param2)
        print("Action apres ...")

    return other_function1()

@deco1 
def do_that(k):
    print(f"Executions des instructions {k}")


do_that("delete ")