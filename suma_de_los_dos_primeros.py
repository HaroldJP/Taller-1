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