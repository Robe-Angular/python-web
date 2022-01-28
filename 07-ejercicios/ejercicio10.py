"""
Ejercicio10
    El programa tiene que pedir la nota de 15 alumnos
    y sacar cuánntos han aprobado y cuántos han suspendido
"""
contador = 1
aprobados = 0
suspendidos = 0
numero_almunos= int(input('¿Cuántos alumnos tienes? '))

while contador <= numero_almunos:
    nota = int(input(f'¿Qué nota quieres ponerle al alumno \"{contador}\"? '))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f'Suspendidos: {suspendidos}')

print(f'Aprobados: {aprobados}')