import sys
from .core import generar_password
from .config import LONGITUD_MINIMA_PASSWORD


def preguntar_si_no(pregunta: str) -> bool:
    """Pregunta al usuario por una opción de sí/no y retorna un valor booleano."""
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print("    -> Opción no válida. Usa 's' o 'n'.")


def obtener_longitud_password() -> int:
    """Obtiene y valida la longitud deseada para la contraseña por parte del usuario."""
    while True:
        try:
            longitud_str = input(
                f"Ingresa la longitud deseada (mínimo {LONGITUD_MINIMA_PASSWORD}): "
            )
            longitud = int(longitud_str)
            if longitud >= LONGITUD_MINIMA_PASSWORD:
                return longitud
            else:
                print(
                    f"[!] Advertencia: Por favor, ingresa un número igual o mayor a {LONGITUD_MINIMA_PASSWORD}."
                )
        except ValueError:
            print(
                "[!] Error: Entrada inválida. Debes ingresar únicamente un número entero."
            )


def ejecutar_cli() -> None:
    """Bucle principal de ejecución de la interfaz de línea de comandos (CLI)."""
    print("\n" + "=" * 50)
    print("        GENERADOR DE CONTRASEÑAS FINAL")
    print("=" * 50)

    while True:
        longitud = obtener_longitud_password()

        print("\nSelecciona los criterios de complejidad:")
        usar_mayusculas = preguntar_si_no("- ¿Incluir letras mayúsculas?")
        usar_minusculas = preguntar_si_no("- ¿Incluir letras minúsculas?")
        usar_numeros = preguntar_si_no("- ¿Incluir números?")
        usar_simbolos = preguntar_si_no("- ¿Incluir caracteres especiales?")

        try:
            password = generar_password(
                longitud=longitud,
                usar_mayusculas=usar_mayusculas,
                usar_minusculas=usar_minusculas,
                usar_numeros=usar_numeros,
                usar_simbolos=usar_simbolos,
            )

            print("\n" + "-" * 50)
            print("Contraseña generada con éxito:")
            print(password)
            print("-" * 50 + "\n")

        except ValueError as error_validacion:
            print(f"\n[!] Error: {error_validacion}")

        if not preguntar_si_no("¿Deseas generar otra contraseña nueva?"):
            print("\n¡Gracias por utilizar el Generador de Contraseñas! Hasta pronto.")
            sys.exit(0)
