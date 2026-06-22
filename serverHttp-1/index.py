import cgi 

print("content-type: text/html; charset=utf-8\n")

html="""<!DOCTYPE html>
<head>
    <meta charset='utf-8'>
    <title>Ma page web</title>
</head>
<body>
    <h1>Bonjour</h1>
    <p>On ecrit du texte pour voir</p>

    <form method="post" action="results.py">
        <p><input type="text" name="username">
        <input type="submit" value="Envoyer">
            
    </form>
</body>
</html>  
"""
print(html)
