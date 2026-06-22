class Time ():

    "definition d'une classe time "

    def __init__(self,hh=12,mm=30,ss=18):
        self.hour=hh
        self.minute=mm
        self.second=ss


    def display_hour(self):
        print("Voici mon heure 2 --)>","{0} : {1} : {2} ".format(self.hour, self.minute, self.second))
        
    
now=Time()
now.display_hour()
stop=Time (1,10,20)
stop_Var=stop.display_hour()
# print("Recreation :",stop_Var) # pourquoi quand on fait d'une fonction affecte a une variable on retourne |None| ?

# two others ways to display
right_now=Time(10,25)

right_now.display_hour()

just_after=Time()

just_after.display_hour()