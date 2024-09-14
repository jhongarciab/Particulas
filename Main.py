from OperacionesParticulas import OperacionesParticulas

# Crear tablas
OperacionesParticulas.crear_tabla('bariones')
OperacionesParticulas.crear_tabla('mesones')
OperacionesParticulas.crear_tabla('leptones')

# Insertar partículas
OperacionesParticulas.insertar_particula('bariones', 'Protón', 1, 1, 0, 938.3)
OperacionesParticulas.insertar_particula('leptones', 'Electrón', -1, 0, 1, 0.511)

# Consultar una partícula
particula = OperacionesParticulas.seleccionar_particula('bariones', 'Protón')
print(particula)
