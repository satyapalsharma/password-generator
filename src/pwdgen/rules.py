import string
from typing import Set, List, Union, Optional

# --- Predefined Character Sets ---
# These sets are defined as strings for easy concatenation and use with secrets.choice.
# They represent common categories of characters used in passwords.

LOWERCASE_CHARS: str = string.ascii_lowercase
UPPERCASE_CHARS: str = string.ascii_uppercase
DIGIT_CHARS: str = string.digits

# Using string.punctuation as the base for symbols.
# This includes a wide range of common symbols.
SYMBOL_CHARS: str = string.punctuation

# Characters that are often considered visually ambiguous or difficult to type.
# This includes 'l', 'I', '1', 'o', 'O', '0' (letters/