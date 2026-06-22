def verif(numero):
    pays=numero[:4]
    val="le numero de telephone est de "
    inval="le numero de telephone n'est pas de "
    if pays == "+243":
        if len(numero) == 13:
            print(val,"la rdc")
        else: 
            print(inval,"la rdc")
    elif pays =="+272":
        if len(numero)== 12:
            print(val,"l'afrique du sud")
        else:
            print(inval," l'afrique du sud")
    elif pays=="+332":
        if len(numero):
            print(val," la belgique ")
        else:
            print(inval," la belgique") 
    elif pays =="+234":
        if len(numero):
            print(val,"du nigeria")
        else:
            print(f"{inval} du nigeria")
    else:
        print("Le numero n'est pas pris en charge ") 


verif(input("Entrez le numero: "))