import cgi
import cgitb

cgitb.enable()

form= cgi.FieldStorage()

if form.getvalue("prenom"):
    prenom=form.getvalue("prenom")
else:
    raise Exception("Prenom non transmis")
if form.getvalue("nom"):
    nom=form.getvalue("nom")
else:
    raise Exception("Nom non transmis")
if form.getvalue("age"):
    age=form.getvalue("age")
else:
    raise Exception("Age non transmis")

print("content/type: text/html; charset=utf-8\n")

html="""<DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>ma page web</title>
</head>
<body>
"""
print(f"bonjour {prenom} {nom} vous avez {age} ans ")
html="""
</body>
</html>
"""