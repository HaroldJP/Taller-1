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










