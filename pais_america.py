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
