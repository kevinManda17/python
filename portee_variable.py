#coding:utf-8

name= "kevin"
name1="Manda"
def _name():
    print(name)

print("-----------------PRINT SPECIAL--------------------\n")
def show_name():
    name="kevin17"
    print(name)

print(name)
show_name()
print("-----------------PRINT SPECIAL--------------------\n")
def print_name(prenom):
    print(prenom)

print_name(name)
print("-----------------PRINT SPECIAL--------------------\n")
def edit_name():
    global name1
    name1="Mubenga"

print(name1)
edit_name()
print(name1) 

print("-----------------PRINT SPECIAL--------------------\n")
