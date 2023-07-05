import unittest
import string

# Import the module under test
from src.pwdgen import strength

class TestStrengthAnalysis(unittest.TestCase):
    """
    Tests for the password strength analysis functions in src/pwdgen/strength.py.
    These tests assume a specific API for the strength module, including:
    - calculate_strength_score(password: str) -> int
    - get_strength_feedback(password: str) -> list[str]
    - Constants like MIN_RECOMMENDED_LENGTH, MIN_RECOMMENDED_CHAR_TYPES
    """

    # --- Test calculate_strength_score function ---

    def test_calculate_strength_score_empty_password(self):
        """
        Test that an empty password receives the lowest possible score (0).
        """
        self.assertEqual(strength.calculate_strength_score(""), 0)

    def test_calculate_strength_score_very_weak(self):
        """
        Test scores for very weak passwords (e.g., short