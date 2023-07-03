import math
import re
import string
from dataclasses import dataclass, field
from typing import List, Set

# --- Constants for Strength Analysis ---
# Minimum recommended length for a strong password.
# This is a common guideline, but can be adjusted based on security policies.
MIN_RECOMMENDED_LENGTH = 12

# Character sets for entropy calculation and type checking.
# Using `string` module for standard character sets.
LOWERCASE_CHARS = string.ascii_lowercase
UPPERCASE_CHARS = string.ascii_uppercase
DIGIT_CHARS = string.digits
SYMBOL_CHARS = string.punctuation

# Pre-convert to sets for efficient `in` checks.
ALL_LOWER = set(LOWERCASE_CHARS