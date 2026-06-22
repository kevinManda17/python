#coding:utf-8

class Time ():
    
    "defintion temporel's object "


period = Time()
period.hour=00
period.minute=20
period.second=21

def display_hour(t):
    print("Voici mon heure --)>",str(t.hour) + ":"+str(t.minute)+ ":" + str(t.second))


def display_hour2(r):
    print("Voici mon heure 2 --)>","{0} : {1} : {2} ".format(r.hour, r.minute, r.seccond))