import cgi 

print("content-type: text/html; charset=utf-8\n")

html="""<doctype html>
<head>
    <meta charset="utf-8">
    <title>Mon formulaire</title>
</head>
<body>
    <h1>voici une page Web avec python CGI</h1>

    <form method="post" action="monForm.py">
        <p><input type="text" name="username">
        <input type="submit" value='envoyer"></p>
    </form>
</html>
"""

print(html)