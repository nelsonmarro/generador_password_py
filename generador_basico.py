import string
import secrets

print("=" * 45)
print("      GENERADOR SEGURO DE CONTRASEÑAS")
print("=" * 45)
print("Asegura tus cuentas con una clave robusta.\n")

# Bucle principal del programa que se repite hasta que el usuario decida salir
while True:

    # 1. PEDIR LA LONGITUD DESEADA
    # Usamos un bucle para insistir hasta que el usuario ingrese un número válido
    while True:
        # try/except sirve para evitar que el programa se caiga si el usuario escribe letras en vez de números
        try:
            texto_ingresado = input("Ingresa la longitud de la contraseña (mínimo 8): ")
            longitud = int(texto_ingresado)

            # Condicional para verificar que el número sea 8 o mayor
            if longitud >= 8:
                break  # Rompe este pequeño bucle porque el dato es correcto
            else:
                print("Error: La longitud mínima debe ser de 8 caracteres.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero.")

    print("\nSelecciona los criterios que deseas incluir:")

    # 2. PEDIR CRITERIOS AL USUARIO
    # Bucle para preguntar por Mayúsculas
    while True:
        respuesta_mayus = input("¿Incluir mayúsculas (A-Z)? (s/n): ").strip().lower()
        if respuesta_mayus == "s" or respuesta_mayus == "n":
            break  # Si la respuesta es s o n, avanzamos
        else:
            print("Entrada inválida. Ingresa 's' para Sí o 'n' para No.")

    # Bucle para preguntar por Minúsculas
    while True:
        respuesta_minus = input("¿Incluir minúsculas (a-z)? (s/n): ").strip().lower()
        if respuesta_minus == "s" or respuesta_minus == "n":
            break
        else:
            print("Entrada inválida. Ingresa 's' o 'n'.")

    # Bucle para preguntar por Números
    while True:
        respuesta_num = input("¿Incluir números (0-9)? (s/n): ").strip().lower()
        if respuesta_num == "s" or respuesta_num == "n":
            break
        else:
            print("Entrada inválida. Ingresa 's' o 'n'.")

    # Bucle para preguntar por Símbolos
    while True:
        respuesta_sim = input("¿Incluir símbolos (!@#$...)? (s/n): ").strip().lower()
        if respuesta_sim == "s" or respuesta_sim == "n":
            break
        else:
            print("Entrada inválida. Ingresa 's' o 'n'.")

    # 3. VALIDACIÓN: Comprobar que al menos dijo que 's' a una opción
    if (
        respuesta_mayus == "n"
        and respuesta_minus == "n"
        and respuesta_num == "n"
        and respuesta_sim == "n"
    ):
        print(
            "\n[!] Error: Debes seleccionar al menos un criterio para generar la contraseña.\n"
        )
        continue  # El 'continue' hace que el programa vuelva directamente al inicio del bucle principal

    # 4. PREPARACIÓN DE DATOS
    # Variables vacías donde iremos guardando cosas
    conjunto_total = ""  # Aquí juntaremos todas las letras y números permitidos
    password_final = []  # Una lista donde iremos metiendo la contraseña letra por letra

    # 5. GARANTÍA DE DIVERSIDAD (Usando puros condicionales)
    # Si dijo que sí a una opción, le agregamos un carácter obligatorio de ese tipo a la contraseña
    # y guardamos todo el abecedario de esa opción en 'conjunto_total'
    if respuesta_mayus == "s":
        conjunto_total = conjunto_total + string.ascii_uppercase
        caracter_aleatorio = secrets.choice(string.ascii_uppercase)
        password_final.append(caracter_aleatorio)  # Agrega el carácter a la lista

    if respuesta_minus == "s":
        conjunto_total = conjunto_total + string.ascii_lowercase
        caracter_aleatorio = secrets.choice(string.ascii_lowercase)
        password_final.append(caracter_aleatorio)

    if respuesta_num == "s":
        conjunto_total = conjunto_total + string.digits
        caracter_aleatorio = secrets.choice(string.digits)
        password_final.append(caracter_aleatorio)

    if respuesta_sim == "s":
        simbolos = "!@#$%^&*()_+~`|}{[]:;?><,./-="
        conjunto_total = conjunto_total + simbolos
        caracter_aleatorio = secrets.choice(simbolos)
        password_final.append(caracter_aleatorio)

    # 6. COMPLETAR LA CONTRASEÑA
    # Bucle que se repite MIENTRAS el tamaño de la contraseña sea menor a la longitud pedida
    while len(password_final) < longitud:
        # Saca una letra al azar de todo el conjunto mezclado que preparamos antes
        caracter_aleatorio = secrets.choice(conjunto_total)
        password_final.append(caracter_aleatorio)

    # 7. MEZCLAR EL RESULTADO
    # Barajamos la lista para que las letras obligatorias no queden siempre al inicio
    rng_seguro = secrets.SystemRandom()
    rng_seguro.shuffle(password_final)

    # 8. CONVERTIR LISTA A TEXTO
    # Usamos un bucle 'for' muy simple para unir las letras en una sola palabra
    password_str = ""
    for letra in password_final:
        password_str = password_str + letra

    # 9. MOSTRAR EL RESULTADO
    print("\n" + "=" * 45)
    print("¡CONTRASEÑA GENERADA CON ÉXITO!")
    print("Resultado: " + password_str)
    print("=" * 45 + "\n")

    # 10. PREGUNTAR SI DESEA SALIR
    while True:
        salir = input("¿Deseas generar otra contraseña? (s/n): ").strip().lower()
        if salir == "s" or salir == "n":
            break
        else:
            print("Entrada inválida. Ingresa 's' o 'n'.")

    # Si la respuesta es 'n' (No quiero generar otra), rompemos el bucle más grande de todos
    if salir == "n":
        print("\n¡Gracias por usar el Generador! Hasta luego.")
        break  # Esto termina el programa por completo
