import string

MIN_PASSWORD_LENGTH = 8
DEFAULT_PASSWORD_LENGTH = 12

CHAR_SETS = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'numbers': string.digits,
    'symbols': string.punctuation
}
