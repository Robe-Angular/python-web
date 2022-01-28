"""
Variables
"""
frase1 = 'frase1 Global'
frase = "jejeje"

print(frase)
print(frase1)

def holaMundo():
    global frase
    frase = 'Hola mundo!!'
    frase1 = 'frase1 Local'
    print(frase)
    print(frase1)

holaMundo()
print(frase)
print(frase1)