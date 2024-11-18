LETTER_SOPU 
JAIME ANDRES GIRALDO MEJIA 

Recordemos un juego que aparecía en los periódicos denominado sopa de letras, el cual
consiste en:
• Una cuadricula de 𝑛 × 𝑚, donde, 𝑛 es el número de filas y 𝑚 el número de columnas
de dicha cuadricula.
• Cada casilla 𝐴𝑛𝑚 contiene una letra del abecedario en mayúscula
• Hay un listado de palabras que se deben encontrar dentro de la cuadricula
Y el juego tenía las siguientes reglas:
• Para señalar una palabra, todas las letras deben estar en casillas contiguas (seguidas)
• Todas las letras de la palabra deben estar en la misma dirección, ver ejemplo 1
A M A R S
S T E R I
O M A Z C
A L C R H
P O L O S
Ejemplo 1: Palabras válidas e inválidas

Palabras válidas: Amar, Osa, Atar, Solo, Polos, …
Palabras inválidas: Mezclar, Palo, …
Con esto en mente, lo han contratado a usted para que construya un algoritmo que resuelva
este juego. Para ello, deberá construir las siguientes funciones:
• Función para chequear si una palabra está dentro de la sopa de letras. Sugerencia:
La función se puede llamar find_word(letter_soup, word)
• Función para chequear si una lista de palabras existe dentro de la sopa de letras.
Sugerencia: La función se puede llamar find_words(letter_soup, words)
• Generar reporte de las palabras que se lograron encontrar y de las palabras que no
se lograron encontrar. Esta función, debe recibir, la sopa de letras y las palabras a
buscar, para poder retornar un diccionario donde las llaves de este son cada una de
las palabras a buscar y el valor asociado a cada llave es un booleano (si se encontró
o no)

teniendo en cuanta lo s requerimientos del parcial para poder hacer una ejecucion corresta del codigo se debe hacer el ingreso de la sopa de letras la cual puede ser cualquier realmente despues de que cumpla con el numero de filas y colubnas , las palabras a encontar tambien pueden ser a criterio propio siguiendo las regras de la sopa tradicion en direcciones orisotal bertical o diagonal teniendo esto claro se puede hacer un uso correcto del codigo 