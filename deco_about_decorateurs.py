#coding:utf-8

class Player():
    
    def __init__(self , name):
        self._name= name 
    
    def get_name(self):
        return self._name
    
    def set_name(self, name ):
        if len(name) <= 25 :
            self._name =name 
        else :
            print("Nom incorrect (25 caracteres max.)")
    
    def one_method():
        pass

    def another_method():
        pass 

    name= property(get_name, set_name)
    one_method= staticmethod(one_method)
    another_method=classmethod(another_method)


class Player1():

    def __init__(self , name):
        self._name= name 
    @property
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self, name ):
        if len(name) <= 25 :
            self._name =name 
        else :
            print("Nom incorrect (25 caracteres max.)")
    @property.deleter
    def del_name():
        pass


    @classmethod
    def one_method():
        pass
    @staticmethod
    def another_method():
        pass 

    
    
    