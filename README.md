# Información del repo

Este repositorio es parte del curso avanzado de Estructura de datos y Algoritmos: Patrones de arreglos y Strings

## Patrón de Dos Apuntadores

El patrón de dos apuntadores es una técnica de programación que se utiliza para resolver problemas que involucran arrays o strings. Este patrón utiliza dos apuntadores para recorrer el array o string en direcciones opuestas y realizar alguna operación en el proceso. Por ejemplo, se puede utilizar el patrón de dos apuntadores para encontrar la subcadena más larga sin caracteres repetidos en un string

No siempre se usan en la dirección opuesta, también pueden ser útil cuando quieres comparar dos valores, uno después del otro.


### Analisis del problema: Verifying Alien Dictionary

En este problema, se nos da un diccionario de palabras en orden alfabético de un idioma alienígena, y el orden de las letras en el alfabeto. Se nos pide determinar si el orden de las letras en el alfabeto es correcto o no.

ejemplo:

```python
palabras = ["hello","leetcode"]
orden = "hlabcdefgijkmnopqrstuvwxyz"
# Esto devuelve True porque el orden de las letras en el alfabeto es correcto

palabras = ["word","world","row"]
orden = "worldabcefghijkmnpqstuvxyz"
# Esto devuelve False porque el orden de las letras en el alfabeto es incorrecto

```