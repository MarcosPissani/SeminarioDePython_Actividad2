def contar_puntos(jugador):
    contador = 0
    for clave,valor in jugador.items() :
        if clave == 'kills':
            contador = contador + (valor*3)
        else:
            if clave == 'assists' :
                contador = contador + (valor*1) 
            else:
                contador = contador + -1 if clave else 0
    return contador

def sumar_kills (jugador,kills):
    jugador['kills'] += kills

def sumar_assists(jugador,assists):
    jugador['assists'] += assists

def sumar_muertes(jugador,muerte):
    if muerte == True :
         jugador['deaths'] += 1

def sumar_MVPs(jugador):
    jugador['MVPs'] += 1

def sumar_puntos(jugador,puntos):
    jugador['puntos'] += puntos
                
    
def sumar_estadisticas(jugador_final , jugador , puntaje):
        sumar_kills(jugador_final,jugador['kills'])
        sumar_assists(jugador_final,jugador['assists'])
        sumar_muertes(jugador_final,jugador['deaths'])
        sumar_puntos(jugador_final,puntaje)
        
def ordenar_diccionarios(diccionario):
    aux = diccionario
    key = ""
    nuevo_diccionario = {}
    for i in range(5):
        max_puntos = -1
        for clave in aux.keys():
             player = aux[clave]
             if max_puntos < player['puntos']:
                 key = clave
                 max_puntos = player['puntos']
        nuevo_diccionario [key] = aux[key]
        del aux[key]
    return nuevo_diccionario
