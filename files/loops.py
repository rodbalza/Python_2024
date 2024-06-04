MAX_SALUDOS = 4
nro_saludos = 0
saludo = 'S'

while saludo == 'S':
    print('¡Hola qué tal!')
    nro_saludos += 1
    if nro_saludos == MAX_SALUDOS:
        print('Máximo nro de saludos alcanzados')
        break
    saludo = input('¿Quiere otro saludo? [S/N]')
else:
    print('Usted no quiere mas saludos')
print('¡Que tenga un buen día!')