import string
import random

while True:
    print("\n" + "=" * 45)
    print("        GENERADOR DE CONTRASEÑAS V1")
    print("=" * 45)

    # 1. Validación estricta de longitud
    while True:
        try:
            longitud_str = input("Ingresa la longitud deseada (mínimo 8): ")
            longitud = int(longitud_str)
            if longitud >= 8:
                break
            else:
                print(
                    "[!] Advertencia: Por favor, ingresa un número igual o mayor a 8 para mayor seguridad."
                )
        except ValueError:
            print(
                "[!] Error: Entrada inválida. Debes ingresar únicamente un número entero."
            )

    # 2. Selección de criterios de complejidad
    print("\nResponde con 's' (sí) o 'n' (no) a los siguientes criterios:")

    while True:
        respuesta_mayus = input("- ¿Incluir letras mayúsculas? (s/n): ").strip().lower()
        if respuesta_mayus in ["s", "n"]:
            break
        print("    -> Opción no válida. Usa 's' o 'n'.")

    while True:
        respuesta_minus = input("- ¿Incluir letras minúsculas? (s/n): ").strip().lower()
        if respuesta_minus in ["s", "n"]:
            break
        print("    -> Opción no válida. Usa 's' o 'n'.")

    while True:
        respuesta_num = input("- ¿Incluir números? (s/n): ").strip().lower()
        if respuesta_num in ["s", "n"]:
            break
        print("    -> Opción no válida. Usa 's' o 'n'.")

    while True:
        respuesta_sim = (
            input("- ¿Incluir caracteres especiales? (s/n): ").strip().lower()
        )
        if respuesta_sim in ["s", "n"]:
            break
        print("    -> Opción no válida. Usa 's' o 'n'.")

    # 3. Validación de selección mínima
    if (
        respuesta_mayus == "n"
        and respuesta_minus == "n"
        and respuesta_num == "n"
        and respuesta_sim == "n"
    ):
        print(
            "\n[!] Error: No se puede generar una contraseña vacía. Debes seleccionar al menos un criterio."
        )
        continue

    # 4. Construcción del conjunto total de caracteres permitidos
    conjunto_total = ""

    if respuesta_mayus == "s":
        conjunto_total += string.ascii_uppercase
    if respuesta_minus == "s":
        conjunto_total += string.ascii_lowercase
    if respuesta_num == "s":
        conjunto_total += string.digits
    if respuesta_sim == "s":
        conjunto_total += string.punctuation

    # 5. Generación de la contraseña seleccionando al azar del conjunto total
    password_final = ""
    for _ in range(longitud):
        password_final += random.choice(conjunto_total)

    # 6. Mostrar el resultado final
    print("\n" + "-" * 45)
    print("Contraseña generada con éxito:")
    print(password_final)
    print("-" * 45 + "\n")

    # 7. Preguntar por una nueva generación
    while True:
        salir = input("¿Deseas generar otra contraseña nueva? (s/n): ").strip().lower()
        if salir in ["s", "n"]:
            break
        print("Por favor responde 's' o 'n'.")

    if salir == "n":
        print("\n¡Gracias por utilizar el Generador de Contraseñas V1! Hasta pronto.")
        break
