
key = 'colors'

delimitador_i = f'% {key}'
delimitador_f = f'% {key}end'

str_test = """
Esto es una prueba de reemplazar dentro de un limite

% COLOR

color1
color2
color3

% COLOREND

Acá inicia el contenido adicional
"""

str_inside = """

rgb(1,2,3)
rgb(4,5,6)
rgb(3,4,8)
rgb(2,1,3)

"""

antes = str_test[:str_test.index(delimitador_i) + len(delimitador_i)]
despues = str_test[str_test.index(delimitador_f):]

print(antes + str_inside + despues)
#print('INICIO: ',str_test.index('% COLOR'))
#print('FIN: ', str_test.index('% COLOREND'))
