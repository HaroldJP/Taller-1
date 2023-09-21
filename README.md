## Taller-1
El punto número 1 que consistía en subir un pantallazo del Quiz de pyhton.



El punto número 2 que consistía en desarrollar un programa que sirviera para insertar 3 números reales cualesquiera y determinar cuál es el número mayor lo hice de la siguiente forma:

```python
a : float
b : float
c : float
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
c = float(input('Escriba el tercer número real:'))
if a <= b <= c:
    print('El número mayor es ' +str(c))
elif a <= c <= b:
    print('El número mayor es ' +str(b))
elif b <= a <= c:
    print('El número mayor es ' +str(c))
elif b <= c <= a:
    print('El número mayor es ' +str(a))
elif c <= a <= b:
    print('El número mayor es ' +str(b))
elif c <= b <= a:
    print('El número mayor es ' +str(a))
```


El punto número 3 que consistía en realizar un programa que sirviera para insertar un número real y determinar si es par o impar o hice de la siguiente forma:

```python
a : float
a = float(input('Inserte un número real:'))
if a%2==0:
  print('El número ' +str(a)+ ' es un número par.')
else:
  print('El número ' +str(a)+ ' es un número impar.')
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


El punto número 5 que consistía en hacer un programa que sirva para insertar tres números reales y determinar si la suma del primer número es mayor, menor o igual al tercer número lo hice de la siguiente forma:

```python
a : float
b : float 
c : float
d : float 
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
c = float(input('Escriba el tercer número real:'))
d = a+b
if d > c:
  print('La suma de los números ' +str(a)+ ' y ' +str(b)+ ' es igual a ' +str(d)+ ', y por lo tanto, es mayor que ' +str(c) )
elif d < c:
    print('La suma de los números ' +str(a)+ ' y ' +str(b)+ ' es igual a ' +str(d)+ ', y por lo tanto, es menor que ' +str(c) )
elif d==c:
  print('La suma de los números ' +str(a)+ ' y ' +str(b)+ ' es igual a ' +str(d)+ ', y por lo tanto, es igual que ' +str(c) )
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


El punto número 7 aún está en proceso pipipipi



El punto número 8 también está en proceso pipipipi



El punto número 9 que consistía en crear un programa que sirviera para insertar un país del continente americano y que dijera cuál es su capital se hizo de la siguiente forma:

```python
lang = input('Escriba en minúsculas y sin tildes un país de américa:')
match lang:
    case 'colombia':
        print('La capital de ' +str(lang)+ ' es Bogotá')
    case 'ecuador':
        print('La capital de ' +str(lang)+ ' es Quito')
    case 'venezuela':
        print('La capital de ' +str(lang)+ ' es Caracas')
    case ' peru':
        print('La capital de ' +str(lang)+ ' es Lima')
    case 'brasil':
        print('La capital de ' +str(lang)+ ' es Brasilia')
    case 'bolivia':
        print('La capital de ' +str(lang)+ 'es La Paz')
    case 'uruguay':
        print('La capital de'  +str(lang)+ ' es Montevideo') 
    case 'paraguay':
        print('La capital de ' +str(lang)+ ' es Asunción')
    case 'argentina':
        print('La capital de ' +str(lang)+ ' es Buenos Aires')
    case 'chile':
        print('La capital de ' +str(lang)+ ' es Santiago de Chile')
    case 'estados unidos':
        print('La capital de ' +str(lang)+ ' es Washington')
    case 'canada':
        print('La capital de ' +str(lang)+ ' es Ottawa')
    case 'mexico':
        print('La capital de ' +str(lang)+ ' es Ciudad de México')
    case 'costa rica':
        print('La capital de ' +str(lang)+ ' es San José')
    case 'republica dominicana':
        print('La capital de ' +str(lang)+ ' es Santo Domingo')
    case 'cuba':
        print('La capital de ' +str(lang)+ ' es La Habana')
    case 'puerto rico':
        print('La capital de '  +str(lang)+ ' es San Juan')
    case 'el salvador':
        print('La capital de ' +str(lang)+ ' es San Salvador')
    case 'jamaica':
        print('La capital de ' +str(lang)+ ' es Kingston')
    case 'panama':
        print('La capital de ' +str(lang)+ ' es Panamá')
    case 'bahamas':
        print('La capital de ' +str(lang)+ ' es Nasáu')
    case 'haiti':
        print('La capital de ' +str(lang)+ ' es Puerto Príncipe')
    case 'guatemala':
        print('La capital de ' +str(lang)+ ' es Ciudad de Guatemala')
    case 'aruba':
        print('La capital de ' +str(lang)+ ' es Oranjestad')
    case 'curazao':
        print('La capital de ' +str(lang)+ ' es Willemstad')
    case 'honduras':
        print('La capital de ' +str(lang)+ ' es Tegucigalpa') 
    case 'belice':
        print('La capital de ' +str(lang)+ ' es Belmopán')
    case 'nicaragua':
        print('La capital de ' +str(lang)+ ' es Managua')
    case 'guyana':
        print('La capital de ' +str(lang)+ ' es Georgetown')
    case 'barbados':
        print('La capital de ' +str(lang)+ ' es Bridgetown')
    case 'surinam':
        print('La capital de ' +str(lang)+ ' es Paramaribo')
    case 'guayana francesa':
        print('La capital de ' +str(lang)+  ' es Cayena')
    case _:
        print('País no identificado')
```


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









