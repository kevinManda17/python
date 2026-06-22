def suite_arithmetique(terme , raison , indice_final):
    U = [ terme ]
    for n in range(indice_final):
        terme += raison
        U.append( terme )
    
    return U

print(suite_arithmetique(123,456,789))