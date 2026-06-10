import string
import secrets


def mostrar_encabezado():
    print("=" * 45)
    print("      GENERADOR SEGURO DE CONTRASEÑAS")
    print("=" * 45)
    print("Asegura tus cuentas con una clave robusta.\n")


def leer_boolean(mensaje):
    """
    Estructura repetitiva (while) para asegurar que el usuario
    responda 's' o 'n'.
    """
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Entrada inválida. Por favor, ingresa 's' para Sí o 'n' para No.")


def generar_password():
    # 1. LEER la longitud deseada
    while True:
        try:
            longitud = int(input("Ingresa la longitud de la contraseña (mínimo 8): "))
            # Estructura condicional (if) para validar la longitud
            if longitud >= 8:
                break
            else:
                print("Error: La longitud mínima debe ser de 8 caracteres.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

    print("\nSelecciona los criterios que deseas incluir:")

    # 2. LEER los criterios
    usar_mayusculas = leer_boolean("¿Incluir mayúsculas (A-Z)?")
    usar_minusculas = leer_boolean("¿Incluir minúsculas (a-z)?")
    usar_numeros = leer_boolean("¿Incluir números (0-9)?")
    usar_simbolos = leer_boolean("¿Incluir símbolos (!@#$...)?")

    # 3. VALIDACIÓN LÓGICA (Condicional)
    if not (usar_mayusculas or usar_minusculas or usar_numeros or usar_simbolos):
        print(
            "\n[!] Error: Debes seleccionar al menos un criterio para generar la contraseña."
        )
        return

    # 4. INICIALIZAR variables y conjuntos de caracteres
    caracteres_activos = {}
    if usar_mayusculas:
        caracteres_activos["mayusculas"] = string.ascii_uppercase
    if usar_minusculas:
        caracteres_activos["minusculas"] = string.ascii_lowercase
    if usar_numeros:
        caracteres_activos["numeros"] = string.digits
    if usar_simbolos:
        caracteres_activos["simbolos"] = "!@#$%^&*()_+~`|}{[]:;?><,./-="

    password_final = []
    conjunto_total = ""

    # 5. GARANTÍA DE DIVERSIDAD (Bucle for)
    # Nos aseguramos de incluir al menos un carácter de cada tipo seleccionado
    for tipo, caracteres in caracteres_activos.items():
        conjunto_total += caracteres
        # Seleccionamos un carácter aleatorio criptográficamente seguro
        caracter_aleatorio = secrets.choice(caracteres)
        password_final.append(caracter_aleatorio)

    # 6. COMPLETAR LA CONTRASEÑA (Bucle while)
    while len(password_final) < longitud:
        caracter_aleatorio = secrets.choice(conjunto_total)
        password_final.append(caracter_aleatorio)

    # 7. BARAJAR EL RESULTADO
    # Para que los caracteres iniciales no sigan un patrón predecible
    # secrets.SystemRandom().shuffle es la forma criptográficamente segura de mezclar
    rng_seguro = secrets.SystemRandom()
    rng_seguro.shuffle(password_final)

    # Convertir la lista a un string final
    password_str = "".join(password_final)

    print("\n" + "=" * 45)
    print("¡CONTRASEÑA GENERADA CON ÉXITO!")
    print(f"Resultado: {password_str}")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    mostrar_encabezado()

    # Bucle principal para permitir al usuario generar múltiples contraseñas
    while True:
        generar_password()

        # Condicional para salir o continuar
        if not leer_boolean("¿Deseas generar otra contraseña?"):
            print(
                "\n¡Gracias por usar el Generador Seguro de Contraseñas! Hasta luego."
            )
            break
        print("-" * 45)
