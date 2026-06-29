from .cli import ejecutar_cli

if __name__ == "__main__":
    try:
        ejecutar_cli()
    except KeyboardInterrupt:
        print("\n\nSaliendo del programa...")
