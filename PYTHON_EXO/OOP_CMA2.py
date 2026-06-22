#coding:utf-8

class Time ():
    
    "definition temporel's object "


period = Time()
period.hour=00
period.minute=20
period.second=21

def display_hour(t):
    print("Voici mon heure --)>",str(t.hour) + ":"+str(t.minute)+ ":" + str(t.second))

display_hour(period)

def display_hour(r):
    print("Voici mon heure 2 --)>","{0} : {1} : {2} ".format(r.hour, r.minute, r.second))

display_hour(period)

# help('FORMATTING')
print('{0}{1}{0}{1}'.format('abra', 'cad'))
 
