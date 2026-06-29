import string

LONGITUD_MINIMA_PASSWORD = 8
LONGITUD_POR_DEFECTO_PASSWORD = 12

CONJUNTOS_CARACTERES = {
    "mayusculas": string.ascii_uppercase,
    "minusculas": string.ascii_lowercase,
    "numeros": string.digits,
    "simbolos": string.punctuation,
}
