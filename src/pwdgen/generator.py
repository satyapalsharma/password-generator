import secrets
import string
from typing import List, Optional, Set

# Define standard character sets for password generation
DIGITS: str = string.digits  # "0123456789"
LOWERCASE: str = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
UPPERCASE: str = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS: str = string.punctuation  # Common symbols like "!@#$%^&*()_+-=[]{}|;:,.<>?/"


def generate_password(
    length: int,
    include_digits: bool = True,
    include_lowercase: bool = True,
    include_uppercase: bool = True,
    include_symbols: bool = True,
    custom_symbols: Optional[str] = None,
    exclude_chars: Optional[str] = None,
    min_digits: int = 0,
    min_lowercase: int = 0,
    min_uppercase: int = 0,
    min_symbols: int = 0,
) -> str:
    """
    Generates a secure random password based on specified criteria.

    This function uses Python's `secrets` module for cryptographic randomness,
    making it suitable for generating strong, unpredictable passwords.
    It allows for fine-grained control over character types, length,
    and the enforcement of minimum counts for specific character categories.

    Args:
        length: The desired length of the password. Must be a positive integer.
        include_digits: If True, digits (0-9) will be included in the character pool.
        include_lowercase: If True, lowercase letters (a-z) will be included.
        include_uppercase: If True, uppercase letters (A-Z) will be included.
        include_symbols: If True, common symbols (from string.punctuation) will be included.
        custom_symbols: An optional string of additional symbols to include in the character pool.
                        These will be added to the pool regardless of `include_symbols`.
        exclude_chars: An optional string of characters to explicitly exclude from the
                       final password, even if they would otherwise be in the character pool.
        min_digits: The minimum number of digits to include in the password.
                    If greater than 0, `include_digits` must be True or digits must be
                    available via `custom_symbols`.
        min_lowercase: The minimum number of lowercase letters to include.
        min_uppercase: The minimum number of uppercase letters to include.
        min_symbols: The minimum number of symbols to include.

    Returns:
        A securely generated password string that meets all specified criteria.

    Raises:
        ValueError: If:
            - `length` is not a positive integer.
            - No character types are selected for the password pool.
            - No characters remain in the pool after exclusions.
            - The password `length` is too short to satisfy all minimum character type requirements.
            - A minimum character type requirement cannot be met because the
              corresponding characters are not available in the pool (e.g., due to exclusions).
    """
    # --- Input Validation ---
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Password length must be a positive integer.")

    # --- Character Pool Construction ---
    # Start with an empty list to build up character sets
    char_pool_parts: List[str] = []

    if include_digits:
        char_pool_parts.append(DIGITS)
    if include_lowercase:
        char_pool_parts.append(LOWERCASE)
    if include_uppercase:
        char_pool_parts.append(UPPERCASE)
    if include_symbols:
        char_pool_parts.append(SYMBOLS)
    if custom_symbols:
        char_pool_parts.append(custom_symbols)

    # Ensure at least one character type is selected
    if not char_pool_parts:
        raise ValueError(
            "At least one character type (digits, lowercase, uppercase, symbols) "
            "or custom symbols must be selected for password generation."
        )

    # Combine all allowed characters into a set for efficient exclusion
    # Using a set automatically handles duplicates if custom_symbols overlap with standard sets
    allowed_chars_set: Set[str] = set("".join(char_pool_parts))

    # Remove explicitly excluded characters
    if exclude_chars:
        allowed_chars_set = allowed_chars_set - set(exclude_chars)

    # After exclusions, ensure there are still characters available
    if not allowed_chars_set:
        raise ValueError("No characters available for password generation after exclusions.")

    # Convert the set back to a string for `secrets.choice`.
    # Sorting ensures a deterministic order for the pool (useful for testing, not for randomness itself).
    full_char_pool: str = "".join(sorted(list(allowed_chars_set)))

    # --- Enforce Minimum Character Type Requirements ---
    password_chars: List[str] = []
    required_chars_count: int = 0

    # Define requirements as (minimum_count, character_set, description) tuples
    # The character_set here is the *original* set (e.g., DIGITS), which will then be
    # filtered against the `allowed_chars_set` to ensure availability.
    requirements = [
        (min_digits, DIGITS, "digits"),
        (min_lowercase, LOWERCASE, "lowercase letters"),
        (