import string
import random

print("--- Generador de Contraseñas (Prototipo V1) ---")

# En este prototipo NO hay bloque try/except, 
# si el usuario escribe texto en lugar de un número, el programa fallará.
# Tampoco valida si la contraseña es muy corta (menor a 8 caracteres).
longitud_str = input("Ingresa la longitud deseada para la contraseña: ")
longitud = int(longitud_str)

# En esta versión básica NO le preguntamos al usuario qué criterios quiere.
# Simplemente juntamos todas las letras, números y símbolos en un solo bloque.
conjunto_total = string.ascii_letters + string.digits + string.punctuation

password = ""

# Se usa un bucle for muy básico y la librería estándar 'random' 
# (la cual NO es criptográficamente segura, a diferencia de 'secrets').
# Tampoco se garantiza diversidad (por mala suerte, podría dar una contraseña de puros números).
for iteracion in range(longitud):
    caracter_aleatorio = random.choice(conjunto_total)
    password = password + caracter_aleatorio

print("\nLa contraseña generada es:")
print(password)
print("\n--- Fin del programa ---")
