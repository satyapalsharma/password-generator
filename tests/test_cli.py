import pytest
import subprocess
import sys
import os
import re
from unittest.mock import patch

# --- Configuration and Helper Functions ---

# Determine the path to the cli.py script.
# This assumes the test is run from the project root or a similar structure
# where 'tests' and 'src' are direct children of the root.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
CLI_SCRIPT_PATH = os.path.join(PROJECT_ROOT, "src", "pwdgen", "cli.py")

# Regex patterns for basic password character type validation.
# These are used to check if generated passwords contain (or don't contain)
