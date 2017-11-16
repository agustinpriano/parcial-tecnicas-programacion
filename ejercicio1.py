def generoListaDeCaracteres(palabra):
    """
    PRE: Recibo una palabra del tipo string
    POS: Devuelvo una sublista donde en cada posicion guardo un caracter de la palabra
    """
    sublista=[]
    for x in palabra:
        sublista.append(x)
    return sublista

def comprueboValidezDePalabra(listaDeCaracteres,palabra):
    """
    PRE: Recibo una lista de caracteres
    POS: Devuelvo True si la lista es sólo de espacios en blanco, False en caso contrario
    """
    espaciosEnBlanco=0
    for x in listaDeCaracteres:
        if x==' ':
            espaciosEnBlanco=espaciosEnBlanco+1
    if espaciosEnBlanco<len(palabra):
        return True
    else:
        return False

def generoListasDePalabrasRotadas(sublista,palabra):
    """
    PRE: Recibo una lista de caracteres
    POS: Devuelvo una lista donde en cada posicion guardo una palabra diferente surgida de la rotación de la palabra original
    """
    lista=[]
    lista.append("".join(sublista))
    for x in range(len(palabra) - 1):
        cont = 0
        primeraLetra = sublista[0]
        while cont <= len(palabra) - 2:
            sublista[cont] = sublista[cont + 1]
            cont = cont + 1
        sublista[len(palabra) - 1] = primeraLetra
        lista.append("".join(sublista))
    return lista

def rotarPalabra(palabra):
    sublista=generoListaDeCaracteres(palabra)
    lista=[]
    palabraValida = comprueboValidezDePalabra(sublista,palabra)
    if palabraValida==True:
        lista = generoListasDePalabrasRotadas(sublista,palabra)
    return lista

def ejercicio1(var1):
    return rotarPalabra(var1)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])


