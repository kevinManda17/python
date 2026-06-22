import cgi 
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
print("content-type: text/html; charset=utf-8\n")

html="""<!DOCTYPE html>
    <head>
        <meta charset='utf-8'>
        <title>Ma page web</title>
    </head>
    <body>
        <h1>Page de resultats</h1>
        <p>On ecrit du texte pour voir</p>
    """
print(html)


if form.getvalue("username"):
    username=form.getvalue("username")
else :
    raise Exception("pseudo non transmis !")


print(f"Bonjour {username} !")

html="""
    </body>
    </html>
"""

print(html)