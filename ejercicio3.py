def ejercicio3(var1):
    return ganadorDeLiga(var1)
def diccionarioEquipos(listaDeResultados):
    """
        PRE: Recibo una lista de tuplas con los resultados de los partidos
        POS: Devuelvo un diccionario donde cada clave es un equipo y para cada clave
             hay una lista donde cada posición son los puntos correspondientes a cada partido según el resultado
        """
    diccionario={}
    for x in listaDeResultados:
        diccionario[x[0]] = []
        diccionario[x[2]] = []
    for x in listaDeResultados:
        if x[1] > x[3]:  # Gano el equipo 1
            diccionario[x[0]].append(2)
        if x[3] > x[1]:  # Gano el equipo 1}
            diccionario[x[2]].append(2)
        if x[3] == x[1]:  # x[1 es el primero alfabeticamente
            diccionario[x[0]].append(1)
            diccionario[x[2]].append(1)

    return diccionario
def listaEquipos(diccionario):
    """
       PRE: Recibo un diccionario
       POS: Devuelvo una lista de listas, donde cada sublista tiene dos posiciones, la primera corresponde al equipo, la
            segunda es una lista donde se almacena en cada posición el puntaje correspondiente a cada partido disputado.
       """
    sublista=[]
    lista=[]
    for equipo, puntos in diccionario.items():
        sublista.append(equipo)
        sublista.append(puntos)
        lista.append(sublista)
        sublista = []
    return lista
def listaEquiposConPuntosSumados(lista):
    sublista2=[]
    lista2=[]
    for x in range(len(lista)):
        for c in range(len(lista[x])):
            sublista2 = []
            if c == 0:
                nombre = lista[x][c]
            if c == 1:
                suma = 0
                for f in range(len(lista[x][c])):
                    suma = suma + (lista[x][c][f])
                sublista2.append(nombre)
                sublista2.append(suma)
                lista2.append(sublista2)
    return lista2

def ordenarPorCantidadDePuntos(lista2):
    lista2.sort(key=lambda x: x[1])
    return lista2

def devolverListaConEquiposEmpatados(lista):
    sublista = []
    x = len(lista) - 1
    puntajeMax = lista[x][1]
    while lista[x][1] == puntajeMax and x >= 0:
        if lista[x][1] not in sublista:
            sublista.append(lista[x][0])
        x = x - 1
    return sublista

def ordenarPorOrdenAlfabetico(lista):
    lista.sort(key=lambda x: x[0])
    return lista

def ganadorDeLiga(listaDeResultados):
    diccionario={}
    lista=[]
    lista2=[]
    if listaDeResultados!=[]:
        diccionario=diccionarioEquipos(listaDeResultados)
        lista=listaEquipos(diccionario)
        lista2=listaEquiposConPuntosSumados(lista)
        lista2=ordenarPorCantidadDePuntos(lista2)
        sublista = devolverListaConEquiposEmpatados(lista2)
        if len(sublista)==1:
            return sublista[0]
        else:
            sublista = ordenarPorOrdenAlfabetico(sublista)
            return sublista[0]
    else:
        return ""

