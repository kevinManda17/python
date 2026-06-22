#coding:utf-8
import functools

"""
notation d'un decorateur:
    func= decorator(func)
    @decorator
"""
def decorator(func):
    print("--------------")
    return func 
@decorator
def hello():
    print("Hello !")
# hello = decorator(hello)
def hi():
    print("Hi !")
hello()
hi()


user_logged= False


def check_user_logged(func):
    def wrapper():
        if user_logged:
            return func()
        else :
            print("Vous n'etes pas connecte.")
    return wrapper 
@check_user_logged
def profile():
    print("Le profil membre...")

@check_user_logged
def articles():
    print("Les articles...")


profile()
articles()
    
print("----------------------les decorateurs avec des parametres--------------------------------")

user_name_admin="kevin"

def check_user(username):
    def decorator1(func):
        @functools.wraps(func)
        def wrapper():
            """
            avec les docstrings c'est toujours la meme histoire
            """
            if username == user_name_admin:
                return  func()
            else :
                print("Utilisateur inconnu ")
            
        return wrapper 
    return decorator1

@check_user("Kev") 
def profile_admin():
    """
     une docstring pour faire genre on en a une 
    """
    print("Vous etes l'administrateur !")


profile_admin()
# --------------------les proprietes --------------------------


help(profile_admin)
# ---------------------plusieurs decorateurs --------------------

def _user_logged():
    pass 

def check_admin():
    pass 

@_user_logged
@check_admin
def admin_panel():
    pass

admin_panel=_user_logged(check_admin(admin_panel))