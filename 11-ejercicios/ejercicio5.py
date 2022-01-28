"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION AVENTURA             DEPORTES        
GTA     ASSINS                  FIFA21
COD     CRASH                   PRO21
PUGB    PRINCE OF PERSIA        MOTOGP21
"""

tabla = [
    {
        "categoria": "Acción",
        "juegos": ["GTA", "Call of Duty", "Pugb"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["Assasins", "Crash Bandicot", "Prince of persia"]
    },

    {
        "categoria": "Deportes",
        "juegos": ["Fifa21", "Pes21", "Moto Gp 21"]
    }
]

for categoria in tabla:
    print(f"----------------{categoria['categoria']}------------------")
    for juego in categoria['juegos']:
        print(juego)
        