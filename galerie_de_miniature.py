from PIL import Image, ExifTags
from os import listdir,remove
from os.path import isfile

def miniatures(rep = '.' , columns = None , width = 800, esp = 5, extensions = ['jpg','jpeg','bmp','png']):
    """
    width = largeur de l'image contenant les miniatures (en px)
    esp = espaces entre les miniatures (en px)
    """
    
    # on liste toutes les images
    img = dict()
    largeur, hauteur = 0,0
    
    for f in listdir( rep ):
        if f[-3:] in extensions:
            i = Image.open(rep + '/' + f)
            img[ f ] = i.size
            if largeur == 0:
                largeur, hauteur = i.width, i.height
    
    # on crée les miniatures
    
    largeur_miniatures = (width - columns*esp) // columns
    hauteur_miniatures = int( (largeur_miniatures/largeur) * hauteur )
    
    if len(img)%columns == 0:
        lines = len( img ) // columns
    else:
        lines = len( img ) // columns + 1
    hauteur_totale = lines * (hauteur_miniatures + esp)
            
    miniatures = Image.new('RGBA', ( width , hauteur_totale ))
    
    n = 1
    
    MAX_SIZE = (largeur_miniatures, hauteur_miniatures)
    
    for f in listdir( rep ):
        if f[-3:] in extensions:
            if n == 1:
                x,y = esp//2,esp//2
            elif n%columns == 1:
                y += hauteur_miniatures + esp
                x = esp//2
            else:
                x += esp + largeur_miniatures
                
            print(rep + '/' + f)
            i = Image.open(rep + '/' + f)
            i.thumbnail(MAX_SIZE)
            print('Sauvegarde de la miniature.')
            i.save(rep + '/mini_' + f)
            i_mini = Image.open(rep + '/mini_' + f).convert("RGBA")
            miniatures.alpha_composite(i_mini, dest=(x,y))
            print(f'Mise de la miniature en {(x,y)}.')
            n += 1
            
            remove(rep + '/mini_' + f)
            print('Suppression de la miniature.')
            
    miniatures = miniatures.convert("RGB")
    miniatures.save( 'miniatures.jpg' )
    miniatures.show()