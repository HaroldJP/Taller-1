n : float
n = float(input("Ingrese en Hz la frecuencia de una onda:"))
if 10**4 <= n < 10**8:
    print('Una onda cuya frecunecia es ' +str(n)+ ' Hz, es una onda como la de un radio, su longitud aproximada puede ser desde los 1000 metros hasta los 2 metros')
elif 10**8 <= n < 10**12:
    print('Una onda cuya freceuncia es ' +str(n)+ ' Hz, es una onda como la de un microondas, su longitud aproximada puede ser desde la estatura de un humano de 2m hasta el tamaño de una mariposa de 1 cm')
elif 10**12 <= n < 10**15:
    print('Una onda cuya frecuencia es ' +str(n)+ ' Hz, puede ser una onda infrarroja, su longitud aproximada puede ser desde el tamaño de la punta de una aguja de 0,01cm, hasta el tamaño de un protozoo de 0,5μm')
elif 10**15 <= n < 10**16:
    print('Una onda cuya frecuencia es ' +str(n)+ 'Hz, puede ser una onda ultravioleta, su longitud aproximada puede ser desde el tamaño de un protozoo de 0,5μm, hasta el tamaño de una partícula de 0,01μm')
elif 10**16 <= n < 10**18:
    print('Una onda cuya frecuencia es ' +str(n)+ ' Hz, puede ser una onda ultravioleta o Rayos X, su longitud aproximada puede ser desde el tamaño de una parícula de 0,01μm, hasta el tamaño de un átomo de 0,1nm')
elif 10**18 <= n < 10**20:
    print('Una onda cuya frecuencia es ' +str(n)+ 'Hz, puede ser una onda de Rayos X o Rayos Gamma, su longitud aproximada puede ser desde el tamaño de un átomo de 0,1nm, hasta el tamaño de un núcleo atómico de 0,001nm')