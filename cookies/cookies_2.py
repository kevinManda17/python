import cgi 
import http.cookies
import os 

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

if "HTTP_COOKIE"  in os.environ:
    print(os.environ["HTTP_COOKIE"])
else : 
    print("HTTP_COOKIR n'existe pas ")
html="""
</body>
</html>
"""
print(html)