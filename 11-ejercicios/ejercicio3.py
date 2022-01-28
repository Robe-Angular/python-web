"""
Ejercicio 3. Programa que compruebe si una variable está vacía y si está vacía,
rellenar con un texto en minpusculas y mostrarlo en mayúsculas
"""
texto = "conteNiDo"

if len(texto.strip()) <= 0:
    texto = 'hola soy un texto en minúsculas'
    print(texto.upper())
else:
    print(f'La variable tiene contenido {texto}')
