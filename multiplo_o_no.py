a : float
b : float
a = float(input('Escriba el primer número real:'))
b = float(input('Escriba el segundo número real:'))
if a%b==0:
    print('El número ' +str(a)+ ' es múltiplo de ' +str(b))
else:
    print('El número ' +str(a)+ ' no es múltiplo de ' +str(b))