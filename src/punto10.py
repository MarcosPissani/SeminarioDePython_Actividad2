from funciones import funcion10
rounds = [
     {
         'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
         'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
         'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
         'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
     },
     {
         'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
         'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
         'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
         'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
         'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
     },
     {
         'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
         'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
         'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
         'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
     },
     {
         'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
         'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
         'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
         'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
     },
     {
         'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
         'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
         'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
         'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
         'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
     }
 ]

ranking_final = {'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs' : 0, 'puntos' : 0 },
                 'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs' : 0, 'puntos' : 0},
                 'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs' : 0, 'puntos' : 0},
                 'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs' : 0, 'puntos' : 0},
                 'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs' : 0, 'puntos' : 0}}

for i in range(5):
  print(f"---------------ronda {i+1}---------------")
  print("jugador  :   puntos")
  rondas_stats = {}
  mvp_nombre = ""
  maximo_puntos=0
  for clave in rounds[i].keys():
     puntaje = funcion10.contar_puntos(rounds[i][clave])
     funcion10.sumar_estadisticas(ranking_final[clave] , rounds[i][clave],puntaje)
     rondas_stats[clave] = puntaje
     if puntaje > maximo_puntos :
        maximo_puntos = puntaje
        mvp_nombre = clave
  funcion10.sumar_MVPs(ranking_final[mvp_nombre])
  for clave,valor in rondas_stats.items() :
     nombre = clave
     punto = valor  
     print(f"{clave} : {valor} " + ("mvp" if clave == mvp_nombre else " "))
ranking_ordenado = funcion10.ordenar_diccionarios(ranking_final)
print("------------------ranking final---------------------")
for clave,valor in ranking_ordenado.items():
   print(f"{clave} : {valor}") 
