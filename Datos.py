from Cursor import CursorDelPool
from OperacionesParticulas import OperacionesParticulas

# Crear tablas
#OperacionesParticulas.crear_tabla('bariones')
#OperacionesParticulas.crear_tabla('mesones')
#OperacionesParticulas.crear_tabla('leptones')

# Insertar las partículas necesarias (u, d, s)
#OperacionesParticulas.insertar_particula('bariones', 'Protón', 'uud', 0.5, 0, 1.0, 1, 0, 938.3)  # Protón (uud)
#OperacionesParticulas.insertar_particula('bariones', 'Neutrón', 'udd', 0.5, 0, 0.0, 1, 0, 939.6)  # Neutrón (udd)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma+', 'uus', 0.5, -1, 1.0, 1, 0, 1189.4)  # Sigma+ (uus)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma0', 'uds', 0.5, -1, 0.0, 1, 0, 1192.5)  # Sigma0 (uds)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma-', 'dds', 0.5, -1, -1.0, 1, 0, 1197.4)  # Sigma- (dds)
#OperacionesParticulas.insertar_particula('bariones', 'Xi0', 'uss', 0.5, -2, 0.0, 1, 0, 1314.9)  # Xi0 (uss)
#OperacionesParticulas.insertar_particula('bariones', 'Xi-', 'dss', 0.5, -2, -1.0, 1, 0, 1321.7)  # Xi- (dss)
#OperacionesParticulas.insertar_particula('bariones', 'Delta++', 'uuu', 1.5, 0, 2.0, 1, 0, 1232.0)  # Delta++ (uuu)
#OperacionesParticulas.insertar_particula('bariones', 'Delta+', 'uud', 1.5, 0, 1.0, 1, 0, 1232.0)  # Delta+ (uud)
#OperacionesParticulas.insertar_particula('bariones', 'Delta0', 'udd', 1.5, 0, 0.0, 1, 0, 1232.0)  # Delta0 (udd)
#OperacionesParticulas.insertar_particula('bariones', 'Delta-', 'ddd', 1.5, 0, -1.0, 1, 0, 1232.0)  # Delta- (ddd)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma*+', 'uus', 1.5, -1, 1.0, 1, 0, 1382.8)  # Sigma*+ (uus)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma*0', 'uds', 1.5, -1, 0.0, 1, 0, 1383.7)  # Sigma*0 (uds)
#OperacionesParticulas.insertar_particula('bariones', 'Sigma*-', 'dds', 1.5, -1, -1.0, 1, 0, 1387.2)  # Sigma*- (dds)
#OperacionesParticulas.insertar_particula('bariones', 'Xi*0', 'uss', 1.5, -2, 0.0, 1, 0, 1531.8)  # Xi*0 (uss)
#OperacionesParticulas.insertar_particula('bariones', 'Xi*-', 'dss', 1.5, -2, -1.0, 1, 0, 1535.0)  # Xi*- (dss)
#OperacionesParticulas.insertar_particula('bariones', 'Omega-', 'sss', 1.5, -3, -1.0, 1, 0, 1672.4)  # Omega- (sss)
#OperacionesParticulas.insertar_particula('leptones', 'Electrón', 'e', 0.5, 0, -1.0, 0, 1, 0.511)  # Electrón (e)
#OperacionesParticulas.insertar_particula('leptones', 'Muon', 'μ', 0.5, 0, -1.0, 0, 1, 105.7)  # Muón (μ)
#OperacionesParticulas.insertar_particula('leptones', 'Tau', 'τ', 0.5, 0, -1.0, 0, 1, 1776.9)  # Tau (τ)
#OperacionesParticulas.insertar_particula('leptones', 'Neutrino Electrónico', 'νe', 0.5, 0, 0.0, 0, 1, 0.0)  # Neutrino Electrónico
#OperacionesParticulas.insertar_particula('leptones', 'Neutrino Muónico', 'νμ', 0.5, 0, 0.0, 0, 1, 0.0)  # Neutrino Muónico
#OperacionesParticulas.insertar_particula('leptones', 'Neutrino Tauónico', 'ντ', 0.5, 0, 0.0, 0, 1, 0.0)  # Neutrino Tauónico
#OperacionesParticulas.insertar_particula('mesones', 'Pion+', 'ud̅', 0.0, 0, 1.0, 0, 0, 139.6)  # Pion+ (ud̅)
#OperacionesParticulas.insertar_particula('mesones', 'Pion0', 'uu̅/dd̅', 0.0, 0, 0.0, 0, 0, 135.0)  # Pion0
#OperacionesParticulas.insertar_particula('mesones', 'Kaon+', 'us̅', 0.0, -1, 1.0, 0, 0, 493.7)  # Kaon+ (us̅)
#OperacionesParticulas.insertar_particula('mesones', 'Kaon0', 'ds̅', 0.0, -1, 0.0, 0, 0, 497.6)  # Kaon0
#OperacionesParticulas.insertar_particula('mesones', 'Rho+', 'ud̅', 1.0, 0, 1.0, 0, 0, 770.0)  # Rho+ (ud̅)
#OperacionesParticulas.insertar_particula('mesones', 'Rho0', 'uu̅/dd̅', 1.0, 0, 0.0, 0, 0, 775.0)  # Rho0
#OperacionesParticulas.insertar_particula('mesones', 'K*+', 'us̅', 1.0, -1, 1.0, 0, 0, 892.0)  # K*+ (us̅)
#OperacionesParticulas.insertar_particula('mesones', 'K*0', 'ds̅', 1.0, -1, 0.0, 0, 0, 896.0)  # K*0
#OperacionesParticulas.insertar_particula('bariones', 'Antiprotón', 'u̅u̅d̅', 0.5, 0, -1.0, -1, 0, 938.3)  # Antiprotón
#OperacionesParticulas.insertar_particula('bariones', 'Antineutrón', 'u̅d̅d̅', 0.5, 0, 0.0, -1, 0, 939.6)  # Antineutrón
#OperacionesParticulas.insertar_particula('bariones', 'Antisigma+', 'u̅u̅s̅', 0.5, 1, -1.0, -1, 0, 1189.4)  # Antisigma+
#OperacionesParticulas.insertar_particula('bariones', 'Antisigma-', 'd̅d̅s̅', 0.5, 1, 1.0, -1, 0, 1197.4)  # Antisigma-
#OperacionesParticulas.insertar_particula('mesones', 'Pion-', 'u̅d', 0.0, 0, -1.0, 0, 0, 139.6)  # Pion-
#OperacionesParticulas.insertar_particula('mesones', 'Kaon-', 'u̅s', 0.0, 1, -1.0, 0, 0, 493.7)  # Kaon-
#OperacionesParticulas.insertar_particula('mesones', 'Antieta', 'u̅u̅/d̅d̅/s̅s̅', 0.0, 0, 0.0, 0, 0, 547.9)  # Antieta
#OperacionesParticulas.insertar_particula('leptones', 'Positrón', 'e+', 0.5, 0, 1.0, 0, -1, 0.511)  # Positrón (e+)
#OperacionesParticulas.insertar_particula('leptones', 'Antimuón', 'μ+', 0.5, 0, 1.0, 0, -1, 105.7)  # Antimuón (μ+)
#OperacionesParticulas.insertar_particula('leptones', 'Antitau', 'τ+', 0.5, 0, 1.0, 0, -1, 1776.9)  # Antitau (τ+)
#OperacionesParticulas.insertar_particula('leptones', 'Antineutrino Electrónico', 'ν̅e', 0.5, 0, 0.0, 0, -1, 0.0)  # Antineutrino Electrónico
#OperacionesParticulas.insertar_particula('leptones', 'Antineutrino Muónico', 'ν̅μ', 0.5, 0, 0.0, 0, -1, 0.0)  # Antineutrino Muónico
#OperacionesParticulas.insertar_particula('leptones', 'Antineutrino Tauónico', 'ν̅τ', 0.5, 0, 0.0, 0, -1, 0.0)  # Antineutrino Tauónico
#OperacionesParticulas.insertar_particula('mesones', 'K-Short', 'ds̅+sd̅', 0.0, -1, 0.0, 0, 0, 497.6)  # K-Short meson
#OperacionesParticulas.insertar_particula('mesones', 'K-Long', 'ds̅+sd̅', 0.0, -1, 0.0, 0, 0, 497.6)  # K-Long meson
#OperacionesParticulas.insertar_particula('mesones', 'Eta meson', 'uu̅+dd̅+ss̅', 0.0, 0, 0.0, 0, 0, 547.9)  # Eta meson
#OperacionesParticulas.insertar_particula('mesones', 'Omega meson', 'uu̅+dd̅', 1.0, 0, 0.0, 0, 0, 782.65)  # Omega meson
#OperacionesParticulas.insertar_particula('mesones', 'Phi meson', 'ss̅', 1.0, 0, 0.0, 0, 0, 1019.46)  # Phi meson
#OperacionesParticulas.insertar_particula('mesones', 'Eta prime meson', 'uu̅+dd̅+ss̅', 0.0, 0, 0.0, 0, 0, 957.78)  # Eta prime meson
#OperacionesParticulas.insertar_particula('particulas', 'Fotón', 'γ', 1.0, 0, 0.0, 0, 0, 0.0, 'boson')  # Fotón (γ)

#OperacionesParticulas.crear_tabla_conjunta('particulas')

#OperacionesParticulas.insertar_datos_unificados()

OperacionesParticulas.mostrar_datos('particulas')


