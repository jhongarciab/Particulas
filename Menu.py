from OperacionesParticulas import OperacionesParticulas

# Solicitar el número de partículas
estado_inicial, estado_final = OperacionesParticulas.solicitar_cantidad_particulas()
11
#Mostrar las partículas disponibles
OperacionesParticulas.mostrar_datos('particulas')

# Determinar si es un decaimiento o una interacción
if estado_inicial == 1:
    print("Este es un proceso de decaimiento.")
else:
    print("Este es un proceso de interacción.")

# Seleccionar las partículas por ID
particulas_iniciales, particulas_finales = OperacionesParticulas.seleccionar_particulas(estado_inicial, estado_final)

# Mostrar la interacción
print("La interacción es: ")
OperacionesParticulas.mostrar_interaccion(particulas_iniciales, particulas_finales)

# Obtener las propiedades de las partículas seleccionadas
propiedades_iniciales = OperacionesParticulas.obtener_propiedades_particulas(particulas_iniciales)
propiedades_finales = OperacionesParticulas.obtener_propiedades_particulas(particulas_finales)
particulas_posibles = OperacionesParticulas.obtener_todas_las_particulas()

OperacionesParticulas.verificar_leyes_conservacion(propiedades_iniciales, propiedades_finales, particulas_posibles)

