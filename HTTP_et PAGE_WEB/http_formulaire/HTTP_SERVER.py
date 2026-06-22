import cgi 

print("content-type: text/html; charset=utf-8\n")

html="""<doctype html>
<head>
    <meta charset="utf-8">
    <title>Mon formulaire</title>
</head>
<body>
    <h1>voici une page Web avec python CGI</h1>

    <form method="post" action="FORMULAIRE.py">
        <label for="nom">nom:</label>
        <input type="text" name="nom"></br>
        <label for="prenom">prenom:</label>
        <input type="text" name="prenom"></br>
        <label for="nom">age:</label>
        <input type="number" name="age"></br>
        <input type="submit" value="Envoyer"></br>
        <input type="submit" value='envoyer"></br>
    </form>
</html>
"""

print(html)