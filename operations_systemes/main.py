import sys 
import os 

need = False 

if need : 
    # pour le module sys : 
    print(sys.version)
    print(sys.version_info)
    pyversion = sys.version_info 
    if pyversion.major <= 3 and pyversion.minor < 13 and pyversion.micro == 2: 
        print("Une version superieure a la 3 ")
    #quel est l'emplacement de l'interpreteur python 
    print(f"Mon emplacement est : {sys.executable}" )
    print(f"La valeur par defaut de l'encodage: {sys.getdefaultencoding()}")
    print(f"Voir les emplacements: {sys.path}")
    for p in sys.path: 
        print(f"Voir les emplacements: {p}")
    # comment verifier la plateforme associer aux codes
    """ 
        win32 : window
        linux: GNU/Linux
        darwin: MacOS 
        cygwin: Cygwin
    """
    print(f" La plateforme : {sys.platform}")
    if sys.platform == "win32":
        print("Nous sommes sur Window.")
    elif sys.platform == "linux":
        print("Nous sommes sur GNU/Linux.")
    else : 
        print("Nous ne connaissons pas ce systeme ou systeme inexistant.")
    probleme = "Je suis un probleme "
    if probleme :
        probleme 
        sys.exit(1)
    args = sys.argv 
    print(f"Il y a ceci : {args[0]} ")
    for arg in sys.argv : 
        print(f" la longueur:{len(arg)} and arg: { arg }")
    #pour le module os 
    try :
        print(os.getcwd())
        os.chdir("C:/Users/kevin_manda/Documents/KEVIN/programming")
        print(os.getcwd())
        print(f" La liste de fichiers: {os.listdir()}")
        false = False 
        for path, directories, files in os.walk('C:/Users/kevin_manda/Documents/KEVIN/programming'):
            print(directories)
        os.mkdir('./test', )
        os.makedirs('retest/programming/project/oop')
        os.rename('rapport', 'report')
        os.remove('muche.txt')
        os.remove('muche')
        os.removedirs("programming/project/oop") 
        print(os.path.exists('text.txt'))
        print(os.path.exists('muche.txt'))
        print(os.path.realpath("muche.txt"))
        base = "programming\\project\\oop"
        filename="prog.py"
        conmplete_path= os.path.join(base, filename )
        p= "C:\\Users\\kevin_manda\\Documents\\KEVIN\\programming\\HOLIDAYS_CURRENT_PROGRAMMING_LEARNING\\PYTHON\\operations_systemes\\doing_test\\doing_test.jpg"
        tpl=os.path.split(p)
        i =1 
        for item in tpl : 
            print(F"The item number {i} : {item}")
        i += 1
        goodpath="C:\\Users\\kevin_manda\\DocumentsKEVIN\\programming\\HOLIDAYS_CURRENT_PROGRAMMING_LEARNING\\PYTHON\\operations_systemes\\doing_test" 
        user_input_path="C:/Users/kevin_manda/Documents/KEVIN/programmingHOLIDAYS_CURRENT_PROGRAMMING_LEARNING/PYTHON/operations_systemes/doing_test"
        print(os.path.samefile(goodpath, user_input_path))
        print(os.path.isdir('test'))
        print(os.path.islink('test'))
        file_stats =os.stat("main.py")
        print(file_stats)
    except Exception as err: 
        print(err)
