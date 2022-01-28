"""
Diccionario es un tipo de dato que almacena un
tipo de datos en formato clave > valor.
Es parecido a un objeto asociativo o un objeto json
"""

persona = {
    "nombre": "Víctor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona["web"])

#Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos[0]['nombre'])
contactos[0]['nombre'] = 'Toñito'
print(contactos[0]['nombre'])

print('\nListado de contactos')
print("----------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("----------------------------------------")