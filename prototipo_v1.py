import string
import random

while True:
    print("\n" + "=" * 45)
    print("      GENERADOR DE CONTRASEÑAS (PROTOTIPO)")
    print("=" * 45)

    # 1. Validación de longitud
    while True:
        try:
            longitud_str = input("Ingresa la longitud deseada (mínimo 8): ")
            longitud = int(longitud_str)
            if longitud >= 8:
                break
            else:
                print("Por favor, ingresa un número igual o mayor a 8.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

    # 2. Selección de criterios
    print("\nResponde con 's' (sí) o 'n' (no) a los siguientes criterios:")
    
    while True:
        respuesta_mayus = input("- ¿Incluir mayúsculas? (s/n): ").lower()
        if respuesta_mayus in ['s', 'n']: break
        print("Opción no válida.")

    while True:
        respuesta_minus = input("- ¿Incluir minúsculas? (s/n): ").lower()
        if respuesta_minus in ['s', 'n']: break
        print("Opción no válida.")

    while True:
        respuesta_num = input("- ¿Incluir números? (s/n): ").lower()
        if respuesta_num in ['s', 'n']: break
        print("Opción no válida.")

    while True:
        respuesta_sim = input("- ¿Incluir símbolos? (s/n): ").lower()
        if respuesta_sim in ['s', 'n']: break
        print("Opción no válida.")

    # Verificar que haya seleccionado al menos uno
    if respuesta_mayus == 'n' and respuesta_minus == 'n' and respuesta_num == 'n' and respuesta_sim == 'n':
        print("\n[!] Error: Debes seleccionar al menos un criterio para generar la contraseña.\n")
        continue

    # 3. Construcción del conjunto de caracteres
    conjunto_total = ""

    if respuesta_mayus == 's':
        conjunto_total = conjunto_total + string.ascii_uppercase
    if respuesta_minus == 's':
        conjunto_total = conjunto_total + string.ascii_lowercase
    if respuesta_num == 's':
        conjunto_total = conjunto_total + string.digits
    if respuesta_sim == 's':
        conjunto_total = conjunto_total + string.punctuation

    # 4. Generación de la contraseña
    # Carencias de este prototipo:
    # - Usa 'random.choice' (que es predecible) en vez de la librería 'secrets'.
    # - Simplemente extrae letras al azar de la bolsa 'conjunto_total'.
    # - NO garantiza que haya al menos 1 caracter de cada tipo que el usuario pidió. 
    #   (Ej: Si pide números y letras, por puro azar la clave podría salir solo con letras).
    password_final = ""
    for _ in range(longitud):
        password_final = password_final + random.choice(conjunto_total)

    # 5. Mostrar resultado
    print("\n---------------------------------------------")
    print("Tu nueva contraseña es:")
    print(password_final)
    print("---------------------------------------------\n")

    # Preguntar si desea salir
    while True:
        salir = input("¿Deseas generar otra contraseña? (s/n): ").lower()
        if salir in ['s', 'n']: break
        print("Por favor responde 's' o 'n'.")
    
    if salir == 'n':
        print("Saliendo del programa...")
        break
