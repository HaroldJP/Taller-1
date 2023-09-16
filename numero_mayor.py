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
