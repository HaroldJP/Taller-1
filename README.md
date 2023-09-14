## Taller-1
En este repositorio vamos a inciar con los programas individuales que correspondían a los puntos pares del taller.

El punto número 2 que consistía en desarrollar un programa que sirviera para insertar 3 números reales cualesquiera y determinar cuál es el número mayor lo hice de la siguiente forma:

```python
a : float
b : float
c : float
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
c = float(input('Escriba el tercer número real:'))
if a <= b < c:
    print('El número mayor es ' +str(c))
elif a <= c < b:
    print('El número mayor es ' +str(b))
elif b <= a < c:
    print('El número mayor es ' +str(c))
elif b <= c < a:
    print('El número mayor es ' +str(a))
elif c <= a < b:
    print('El número mayor es ' +str(b))
elif c <= b < a:
    print('El número mayor es ' +str(a))
elif a == b == c:
    print('El número mayor es ' +str(a))
```


El punto número 4 que consistía en desarrollar un programa que sirviera para insertar 2 números reales cualesquiera y determinar si el primero es múltiplo del segundo lo hice de la siguiente forma:

```python
a : float
b : float
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
if a%b==0:
    print('El número ' +str(a)+ ' es múltiplo de ' +str(b))
else:
    print('El número ' +str(a)+ ' no es múltiplo de ' +str(b))
```


El punto número 6 que consistía en desarrollar un programa que sirva para insertar una letra cualquiera y determinar si es un vocal o una consonante lo hice de la siguiente forma:

```python
lang = input('Escriba una letra:')
match lang:
    case 'a':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'e':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'i':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'o':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'u':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'A':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'E':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'I':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'O':
        print('La letra ' +str(lang)+ ' es una vocal')
    case 'U':
        print('La letra ' +str(lang)+ ' es una vocal')
    case _:
        print('La letra ' +str(lang)+ ' es una consonante')
````


El punto número 10 que consistía en crear un programa que sirva para insertar una distancia y que determine cuánto tardaría la luz, el sonido, el auto comercial más vendido y Usain Bolt en recorrer dicha distancia se desarrolló teniendo en cuenta que la distancia se debe insertar en kilómetros y que en este caso el vehículo comercial más rápido es el SS Tuatara.

De este modo, así quedó el programa:

```python
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
```









