import cgi 
import http.cookies 
import datetime

expiration=datetime.datetime.now()+datetime.timedelta(days=365)
expiration =expiration.strftime("%a,%d-%b-%Y %H:%M :%S,")


my_cookie= http.cookies.SimpleCookie()
my_cookie["pref_lang"]="fr"
my_cookie["pref_lang"]["expires"]=expiration
my_cookie["pref_lang"]["httponly"]=True

print("content-type: text/type; charset=utf-8\n")
print(my_cookie.output())
html="""
<DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>ma page web pour les cookies </title>
</head>
<body>
    <h1>cookies avec python</h1>
    <p>bonjour</p>
</body>
</html>
"""
print(html)

""" expires 
path
comment 
domain
secure 
version
httponly
set-cookie; pref_lang=fr; httponly"""