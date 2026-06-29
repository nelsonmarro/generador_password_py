import sys
from .core import generate_password
from .config import MIN_PASSWORD_LENGTH

def prompt_yes_no(question: str) -> bool:
    """Prompts the user with a yes/no question and returns a boolean."""
    while True:
        response = input(f"{question} (s/n): ").strip().lower()
        if response in ['s', 'n']:
            return response == 's'
        print("    -> Opción no válida. Usa 's' o 'n'.")

def get_password_length() -> int:
    """Gets and validates the desired password length from the user."""
    while True:
        try:
            length_str = input(f"Ingresa la longitud deseada (mínimo {MIN_PASSWORD_LENGTH}): ")
            length = int(length_str)
            if length >= MIN_PASSWORD_LENGTH:
                return length
            else:
                print(f"[!] Advertencia: Por favor, ingresa un número igual o mayor a {MIN_PASSWORD_LENGTH}.")
        except ValueError:
            print("[!] Error: Entrada inválida. Debes ingresar únicamente un número entero.")

def run_cli() -> None:
    """Main CLI execution loop."""
    print("\n" + "=" * 50)
    print("        GENERADOR DE CONTRASEÑAS FINAL")
    print("=" * 50)
    
    while True:
        length = get_password_length()
        
        print("\nSelecciona los criterios de complejidad:")
        use_upper = prompt_yes_no("- ¿Incluir letras mayúsculas?")
        use_lower = prompt_yes_no("- ¿Incluir letras minúsculas?")
        use_numbers = prompt_yes_no("- ¿Incluir números?")
        use_symbols = prompt_yes_no("- ¿Incluir caracteres especiales?")
        
        try:
            password = generate_password(
                length=length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_numbers=use_numbers,
                use_symbols=use_symbols
            )
            
            print("\n" + "-" * 50)
            print("Contraseña generada con éxito:")
            print(password)
            print("-" * 50 + "\n")
            
        except ValueError as e:
            print(f"\n[!] Error: {e}")
            
        if not prompt_yes_no("¿Deseas generar otra contraseña nueva?"):
            print("\n¡Gracias por utilizar el Generador de Contraseñas! Hasta pronto.")
            sys.exit(0)
