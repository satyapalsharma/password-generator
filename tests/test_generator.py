import pytest
import string
from collections import Counter
from src.pwdgen.generator import (
    generate_password,
    DEFAULT_LENGTH,
    LOWERCASE_CHARS,
    UPPERCASE_CHARS,
    DIGIT_CHARS,
    SYMBOL_CHARS,
    AMBIGUOUS_CHARS,
)

# --- Helper functions for assertions ---

def _contains_any(password: str, char_set: str) -> bool:
    """Checks if the password contains at least one character from the given set."""
    return any(c in char_set for c in password)

def _contains_only(password: str, char_set: str) -> bool:
    """Checks if all characters in the password are exclusively