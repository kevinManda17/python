
class space():

    'space for an object '

    kk= 33
    def display(self,):
        print(kk,space.kk,self.kk)

kk=12
attempt=space()
attempt.kk=67
attempt.display()

print("we display variables with: ",kk,space.kk,attempt.kk)

# help(space)