a : float ##esta es la distancia en kilómetros que pone el ususario
b : float = 299792458 ##esta es la velocidad de la luz en km/s
c : float = 1235.5 ##esta es la velocidad del sonido en km/h
d : float = 508 ##esta es la velocidad del SS Tuatara, el vehículo comercial más rápido del mundo dada en km/h
e : float = 44.72 ##esta es la velocidad de Usain Bolt en km/h
f : float ##este es el cálculo del tiempo que tardaría la luz
g : float ##este es el cálculo del tiempo que tardaría el sonido en el aire
h : float ##este es el cálculo del tiempo que tardaría el SS Tuatara
i: float ##Este es el cálculo del tiempo que tardaría Usain Bolt
a = float(input('Inserte una distancia en kilómetros:'))
f = a/b
print('La luz tardará ' +str(f)+ ' segundos en recorrer ' +str(a)+ ' kilómetros')
g = a/c
print('El sonido tardará ' +str(g)+ ' horas en recorrer ' +str(a)+ ' kilómetros')
h = a/d
print('El auto comercial más rápido SS Tuatara tardará ' +str(h)+ ' horas en recorrer ' +str(a)+ ' kilómetros')
i = a/e
print('Usain Bolt tardará ' +str(i)+ ' horas en recorrer ' +str(a)+ ' kilómetros')


