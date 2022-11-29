borrado = True
cadena = 'oatcm(ajajq)(h))uumf)trcwc'
cadena2 = ''

cadena = ''.join(c for c in cadena if c == '(' or c == ')')
cadena2 = cadena
if len(cadena) % 2 == 0:
    while borrado:
        cadena = cadena2
        cadena2 = cadena.replace('()', '')
        if cadena == cadena2:
            borrado = False
if cadena2 == '':
    print('Valido')
else:
    print('Invalido')
