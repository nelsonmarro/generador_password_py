import random

print("--- Generador de Contraseñas (Primer Avance) ---")

# En este avance inicial no hay validaciones de errores.
# Si el usuario ingresa texto en lugar de números, el programa fallará.
longitud = int(input("¿Cuántos caracteres quieres para tu contraseña?: "))

# Por ahora no pedimos opciones al usuario, 
# simplemente usamos letras minúsculas y números fijos.
caracteres_disponibles = "abcdefghijklmnopqrstuvwxyz0123456789"

password_generada = ""

# Bucle básico para ir concatenando caracteres al azar
for iteracion in range(longitud):
    caracter_aleatorio = random.choice(caracteres_disponibles)
    password_generada = password_generada + caracter_aleatorio

print("\nLa contraseña generada es:")
print(password_generada)
print("\n--- Fin del programa ---")
