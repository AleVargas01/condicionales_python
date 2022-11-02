# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Objetizo:
¡Realizar un juego de trivia!
Usted cuenta con la variables "preguntas" y "respuestas",
por cada pregunta se debe consultar al usuario que juega
cuál es la respuesta correcta.

Cada respuesta correcta otorga 10 puntos.

Importante: Ingresar los nombres sin tildes.

Alumno:
- Crear una variable llamada puntaje inicializada,
  en cero. Esta variable la deberá incrementar en 10
  por cada respuesta correcta.

- Deberá imprimir en consola una pregunta por vez,
  y con la función input en cada caso solicitar una respuesta
  por cada pregunta realizada.

- Utilizar condicionales para evaluar si la respuesta
  ingresada por el usuario coincide con la respuesta
  del programa (las variables).

- Cada respuesta ingresada por el usuario por consola
  la deberá pasar a minúsculas utilizando la función
  lower (cómo se vio los ejemplos de clase)

- Imprimir al final del programa el puntaje total
'''

print('Juego de trivia')
puntaje = 0

pregunta_1 = "¿Cuál es la capital de Argentina?"
respuesta_1 = "buenos aires"

pregunta_2 = "¿Cuál es la capital de Perú?"
respuesta_2 = "lima"

pregunta_3 = "¿Cuál es la capital de Uruguay?"
respuesta_3 = "montevideo"

pregunta_4 = "¿Cuál es la capital de Colombia?"
respuesta_4 = "bogota"

pregunta_5 = "¿Cuál es la capital de Venezuela?"
respuesta_5 = "caracas"

# Empezar aquí la resolución del ejercicio

puntaje_inicializada = 0

print (pregunta_1)
respuesta =  input()
respuesta_lower = respuesta.lower()

if respuesta_lower == respuesta_1:
    puntaje_inicializada += 10

#Siguiente pregunta
print(pregunta_2)
respuesta = input()
respuesta_lower = respuesta.lower()

if respuesta_lower == respuesta_2:
  puntaje_inicializada += 10

#Siguiente pregunta
print(pregunta_3)
respuesta = input()
respuesta_lower = respuesta.lower()

if respuesta_lower == respuesta_3:
  puntaje_inicializada += 10

#Siguiente pregunta
print(pregunta_4)
respuesta = input()
respuesta_lower = respuesta.lower()

if respuesta_lower == respuesta_4:
  puntaje_inicializada += 10

#Siguiente pregunta
print(pregunta_5)
respuesta = input()
respuesta_lower = respuesta.lower()

if respuesta_lower == respuesta_5:
  puntaje_inicializada += 10

print('*****Su puntaje final es: ',puntaje_inicializada, '*****')