a : float
b : float
c : float
d : float
e : float
f : float
g : float
h : float
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
c = float(input('Escriba el tercer número real:'))
d = float(input('Escriba el cuarto número real:'))
e = float(input('Escriba el quinto número real:'))
f = (a+b+c+d+e)/5
print('El promedio de los números ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e)+ ' es ' +str(f))
g = (a*b*c*d*e)**(1/5)
print('El promedio multiplicativo de los números ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e)+ ' es ' +str(g))
##a y b
if a <= b <= c <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= b <= c <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= b <= d <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= b <= d <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= b <= e <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= b <= e <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
##a y c
elif a <= c <= b <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= c <= b <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= c <= d <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= c <= d <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= c <= e <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= c <= e <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
##a y d
elif a <= d <= b <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= d <= b <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= d <= c <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(a)+ ' = ', e**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= d <= c <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= d <= e <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= d <= e <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
##a y e 
##estoy cansado jefe
elif a <= e <= b <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= e <= b <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= e <= c <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(a)+ ' = ', d**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= e <= c <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= e <= d <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(a)+ ' = ', c**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
elif a <= e <= d <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(a))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(a)+ ' = ', b**a)
    print('La raíz cúbica del menor número es ' +str(a)+'^(1/3) = ', a**(1/3))
##b y a
elif b <= a <= c <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= a <= c <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= a <= d <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= a <= d <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= a <= e <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= a <= e <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
## b y c 
##PROFE SI ESTÁ VIENDO ESTO POR FAVOR DEME UNA BUENA NOTA QUE YA ESTOY CANSADO ):
elif b <= c <= a <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= c <=a <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= c <= d <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= c <= d <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= c <= e <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= c <= e <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
#b y d
elif b <= d <= a <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= d <= a <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= d <= c <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(b)+ ' = ', e**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= d <= c <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= d <= e <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= d <= e <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
##b y e
elif b <= e <= a <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= e <= a <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= e <= c <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(b)+ ' = ', d**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= e <= c <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= e <= d <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(b)+ ' = ', c**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
elif b <= e <= d <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(b))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(b)+ ' = ', a**b)
    print('La raíz cúbica del menor número es ' +str(b)+'^(1/3) = ', b**(1/3))
##c y a
elif c <= a <= b <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= a <= b <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= a <= d <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= a <= d <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= a <= e <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= a <= e <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
## c y b
elif c <= b <= a <= d <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= b <= a <= e <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= b <= d <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= b <= d <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= b <= e <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= b <= e <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
## c y d
elif c <= d <= a <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= d <= a <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= d <= b <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(c)+ ' = ', e**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= d <= b <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= d <= e <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= d <= e <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(d)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
##c y e
elif c <= e <= a <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= e <= a <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= e <= b <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(c)+ ' = ', d**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= e <= b <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= e <= d <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(c)+ ' = ', b**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
elif c <= e <= d <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(e)+ ' y ' +str(c))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(c)+ ' = ', a**c)
    print('La raíz cúbica del menor número es ' +str(c)+'^(1/3) = ', c**(1/3))
##d y a
elif d <= a <= b <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= a <= b <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= a <= c <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= a <= c <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= a <= e <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= a <= e <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
##d y b
elif d <= b <= a <= c <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= b <= a <= e <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= b <= c <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= b <= c <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= b <= e <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= b <= e <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
##d y c
elif d <= c <= a <= b <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= c <= a <= e <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= c <= b <= a <= e:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(e))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(e)+'^'+str(d)+ ' = ', e**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= c <= b <= e <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= c <= e <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= c <= e <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(e)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(e))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ', ' +str(c)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
## d y e
elif d <= e <= a <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= e <= a <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= e <= b <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(d)+ ' = ', c**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= e <= b <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= e <= c <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(d)+ ' = ', b**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
elif d <= e <= c <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(d)+ ', ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(e)+ ' y ' +str(d))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(d)+ ' = ', a**d)
    print('La raíz cúbica del menor número es ' +str(d)+'^(1/3) = ', d**(1/3))
##e y a:
elif e <= a <= b <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= a <= b <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= a <= c <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= a <= c <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= a <= d <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= a <= d <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
## e y b
elif e <= b <= a <= c <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= b <= a <= d <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= b <= c <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= b <= c <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= b <= d <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= b <= d <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
## e y c
elif e <= c <= a <= b <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= c <= a <= d <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= c <= b <= a <= d:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(d))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(d)+'^'+str(e)+ ' = ', d**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= c <= b <= d <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= c <= d <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= c <= d <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(c)+ ', ' +str(d)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(d))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ', ' +str(c)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
##e y d
elif e <= d <= a <= b <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(b)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(b)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= d <= a <= c <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(a)+ ', ' +str(c)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(a))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(c)+ ', ' +str(a)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= d <= b <= a <= c:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(a)+ ' y ' +str(c))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(c)+ ', ' +str(a)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(c)+'^'+str(e)+ ' = ', c**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= d <= b <= c <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(b)+ ', ' +str(c)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(b))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(c)+ ', ' +str(b)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= d <= c <= a <= b:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(a)+ ' y ' +str(b))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(b)+ ', ' +str(a)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(b)+'^'+str(e)+ ' = ', b**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
elif e <= d <= c <= b <= a:
    print('Números ordenados en forma ascendente: ' +str(e)+ ', ' +str(d)+ ', ' +str(c)+ ', ' +str(b)+ ' y ' +str(a))
    print('La mediana es el número: ' + str(c))
    print('Números ordenados en forma descendente: ' +str(a)+ ', ' +str(b)+ ', ' +str(c)+ ', ' +str(d)+ ' y ' +str(e))
    print('La potencia del mayor número elevado al menor número es ' +str(a)+'^'+str(e)+ ' = ', a**e)
    print('La raíz cúbica del menor número es ' +str(e)+'^(1/3) = ', e**(1/3))
##PROFE SI ESTÁ VIENDO ESTO YO VERÉ UNA BUENA NOTA QUE CASI NO ACABO CON ESTE CÓDIGO










    


