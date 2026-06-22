import crypt 


class User():
    def __init__(self, id , name , password ):
        self.id = id 
        self.name = name 
        self._salt =crypt.mksalt()
        self._password = self._crypt_pwd(password)

    def _crypt_pwd(self, password ):
        return crypt.crypt(password, self._salt)
    
    def check_pwd(self , password ):
        return self._password == self._crypt_pwd(password)
    

kev= User()

kev.check_pwd('kevin')