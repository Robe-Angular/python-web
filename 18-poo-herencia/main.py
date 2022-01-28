import clases

persona = clases.Persona()
persona.setNombre("Víctor")
persona.setApellidos("Robles")
persona.setAltura("190cm")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martínez")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print('-------------------------------------------------------------------')

tecnico = clases.TecnicoRedes()
print(f'{tecnico.auditarRedes} {tecnico.getLenguajes()}')