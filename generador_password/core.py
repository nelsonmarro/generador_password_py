import random
from .config import CONJUNTOS_CARACTERES


def generar_password(
    longitud: int,
    usar_mayusculas: bool,
    usar_minusculas: bool,
    usar_numeros: bool,
    usar_simbolos: bool,
) -> str:
    """Genera una contraseña segura basada en los criterios proporcionados.

    Argumentos:
        longitud: La longitud deseada de la contraseña.
        usar_mayusculas: Incluir letras mayúsculas si es True.
        usar_minusculas: Incluir letras minúsculas si es True.
        usar_numeros: Incluir números si es True.
        usar_simbolos: Incluir símbolos si es True.

    Retorna:
        Una cadena de texto con la contraseña generada de forma segura.

    Lanza:
        ValueError: Si la longitud es inválida o no se selecciona ningún conjunto de caracteres.
    """
    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor a 0.")

    pool_caracteres = ""
    if usar_mayusculas:
        pool_caracteres += CONJUNTOS_CARACTERES["mayusculas"]
    if usar_minusculas:
        pool_caracteres += CONJUNTOS_CARACTERES["minusculas"]
    if usar_numeros:
        pool_caracteres += CONJUNTOS_CARACTERES["numeros"]
    if usar_simbolos:
        pool_caracteres += CONJUNTOS_CARACTERES["simbolos"]

    if not pool_caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    caracteres_password = []

    # Aseguramos al menos un carácter de cada tipo seleccionado
    if usar_mayusculas:
        caracteres_password.append(random.choice(CONJUNTOS_CARACTERES["mayusculas"]))
    if usar_minusculas:
        caracteres_password.append(random.choice(CONJUNTOS_CARACTERES["minusculas"]))
    if usar_numeros:
        caracteres_password.append(random.choice(CONJUNTOS_CARACTERES["numeros"]))
    if usar_simbolos:
        caracteres_password.append(random.choice(CONJUNTOS_CARACTERES["simbolos"]))

    # Verificamos si la longitud solicitada es menor a la cantidad de tipos seleccionados
    if longitud < len(caracteres_password):
        raise ValueError(
            f"La longitud mínima para estos criterios es {len(caracteres_password)}."
        )

    # Rellenamos el resto usando rangos (for ... in range)
    for _ in range(longitud - len(caracteres_password)):
        caracteres_password.append(random.choice(pool_caracteres))

    # Mezclamos los caracteres para que el orden sea impredecible
    random.shuffle(caracteres_password)

    return "".join(caracteres_password)
