import argparse
import json
import sys
from typing import List, Dict, Any

from pwdgen.generator import PasswordGenerator, PasswordRules, GenerationError
from pwdgen.strength import PasswordStrengthAnalyzer, StrengthRating

# Define exit codes for the CLI
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def _configure_rules_from_args(args: argparse.Namespace) -> PasswordRules:
    """
    Configures PasswordRules based on parsed command-line arguments.
    This function applies presets first, then individual character set
    exclusions, custom characters, and finally minimum requirements.
    """
    # Start with a default rules object, then apply length
    rules = PasswordRules(length=args.length)

    #