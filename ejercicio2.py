def contarColumnasPorFila(mapa):
    """
    PRE: Recibo una lista de cadenas que representa un mapa de caracteres
    POS: Devuelvo 1 si en el mapa hay las misma cantidad de filas que de columnas, 0 ebn caso contrario.
    """
    ok=0
    for x in range(len(mapa)):
        if x!=len(mapa)-1:
            if len(mapa[x])==len(mapa[x+1]):
                ok=1
            else:
                ok=0
        else:
            if len(mapa[x]) == len(mapa[x-1]):
                ok = 1
            else:
                ok=0

    return ok
def devolverBarcosNoHundidos(mapa,listaDeTuplas):
    """
    PRE: Recibo una lista de cadenas que representa un mapa de caracteres y una lista de tuplas con las posiciones donde
         se hundirán los barcos
    POS: Devuelvo una lista de tuplas de la forma (x,y) representando la posición donde quedan barcos
    """
    lista = []
    sublista = []
    listaADevolver = []
    tupla = []
    fila = 0
    columna = 0
    ok=contarColumnasPorFila(mapa)
    if mapa!=[] and ok==1:
        if len(mapa)>1:
            if mapa[0][0]=="b" or mapa[0][0]==".":
                for x in mapa:
                    sublista=[]
                    for c in x:
                        sublista.append(c)
                    lista.append(sublista)
                print(lista)
                for f in listaDeTuplas:
                    x1=f[0]
                    y1=f[1]
                    print(x1,y1)
                    lista[x1-1][y1-1]='.'
                print(lista)
                for x in lista:#x recorre las filas
                    tupla=[]
                    for c in x:#c recorre las columnas
                        tupla = []
                        if lista[fila][columna]=='b':
                            tupla.append(fila+1)
                            tupla.append(columna+1)
                            tupla=tuple(tupla)
                            if (tupla != ()):
                                listaADevolver.append(tupla)
                        columna=columna+1
                    fila=fila+1
                    columna=0
    return listaADevolver

def ejercicio2(var1,var2):
    return devolverBarcosNoHundidos(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])
