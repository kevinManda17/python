import cgi 
import http.cookies
import os 
import sys 
import codecs

sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type: text/type; charset=utf-8\n")

html="""<DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>ma page web pour les cookies </title>
</head>
<body>
    <h1>cookies avec python</h1>
    <p>bonjour</p>
"""
print(html)

try :
     user_lang=http.cookies.SimpleCookie(os.environ)
     print("la langue utiisateur est :",user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
     print("Non trouve")

html="""
</body>
</html>
"""
print(html)