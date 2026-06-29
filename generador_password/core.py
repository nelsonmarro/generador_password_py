import random
from .config import CHAR_SETS


def generate_password(
    length: int, use_upper: bool, use_lower: bool, use_numbers: bool, use_symbols: bool
) -> str:
    """Generates a secure password based on provided criteria.

    Args:
        length: The desired length of the password.
        use_upper: Include uppercase letters if True.
        use_lower: Include lowercase letters if True.
        use_numbers: Include numbers if True.
        use_symbols: Include symbols if True.

    Returns:
        A securely generated string password.

    Raises:
        ValueError: If length is invalid or no character sets are selected.
    """
    if length <= 0:
        raise ValueError("La longitud debe ser mayor a 0.")

    char_pool = ""
    if use_upper:
        char_pool += CHAR_SETS["uppercase"]
    if use_lower:
        char_pool += CHAR_SETS["lowercase"]
    if use_numbers:
        char_pool += CHAR_SETS["numbers"]
    if use_symbols:
        char_pool += CHAR_SETS["symbols"]

    if not char_pool:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    password_chars = []

    # Aseguramos al menos un carácter de cada tipo seleccionado
    if use_upper:
        password_chars.append(random.choice(CHAR_SETS["uppercase"]))
    if use_lower:
        password_chars.append(random.choice(CHAR_SETS["lowercase"]))
    if use_numbers:
        password_chars.append(random.choice(CHAR_SETS["numbers"]))
    if use_symbols:
        password_chars.append(random.choice(CHAR_SETS["symbols"]))

    # Verificamos si la longitud solicitada es menor a la cantidad de tipos seleccionados
    if length < len(password_chars):
        raise ValueError(
            f"La longitud mínima para estos criterios es {len(password_chars)}."
        )

    # Rellenamos el resto usando rangos (for ... in range)
    for _ in range(length - len(password_chars)):
        password_chars.append(random.choice(char_pool))

    # Mezclamos los caracteres para que el orden sea impredecible
    random.shuffle(password_chars)

    return "".join(password_chars)
