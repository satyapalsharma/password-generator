"""
Password Generator Package

This package provides functionalities for generating secure passwords,
analyzing their strength, and defining custom rules.

Key components:
- `generate_password`: Function to generate a password based on specified rules.
- `analyze_strength`: Function to assess the strength of a given password.
- `PasswordRules`: Class to define and manage password generation and validation rules.
- `StrengthResult`: Data class representing the outcome of a strength analysis.
- `RuleViolation`: Exception class for when a password violates a rule.
"""

# Define the package version. This is a common practice for Python packages.
# It allows users to check the version of the installed package programmatically.
__version__ = "0.1.0"

# Import core functionalities from submodules to make them directly accessible
# from the top-level `pwdgen` package. This simplifies imports for users
# (e.g., `from pwdgen import generate_password` instead of `from pwdgen.generator import generate_password`).

from .generator import generate_password
from .strength import analyze_strength, StrengthResult
from .rules import PasswordRules, RuleViolation

# Define `__all__` to explicitly list the public API of the package.
# This controls what symbols are imported when `from pwdgen import *` is used.
# While `import *` is generally discouraged, defining `__all__` is good practice
# for clarity and to prevent accidental exposure of internal components.
__all__ = [
    "__version__",
    "generate_password",
    "analyze_strength",
    "StrengthResult",
    "PasswordRules",
    "RuleViolation",
]