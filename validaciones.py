def validaciondni(dni):
    if len(dni) != 9:
        return False
    
    if dni[8].isdigit():
        return False

    for numero in dni[:8]:
        if numero.isdigit() == False:
            return False

    return True