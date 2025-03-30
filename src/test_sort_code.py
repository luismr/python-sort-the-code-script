import unittest
from sort_code import sort_code

class TestSortCode(unittest.TestCase):
    def test_basic_sorting(self):
        """Test basic sorting functionality"""
        self.assertEqual(sort_code("acbdfe"), "abcdef")
        self.assertEqual(sort_code("pqksuvy"), "kpqsuvy")

    def test_empty_string(self):
        """Test handling of empty string"""
        self.assertEqual(sort_code(""), "")

    def test_single_character(self):
        """Test handling of single character"""
        self.assertEqual(sort_code("a"), "a")

    def test_all_letters(self):
        """Test sorting with all letters of the alphabet"""
        self.assertEqual(sort_code("zyxwvutsrqponmlkjihgfedcba"), "abcdefghijklmnopqrstuvwxyz")

    def test_case_sensitivity(self):
        """Test that the function is case-sensitive"""
        self.assertEqual(sort_code("aBc"), "Bac")

if __name__ == '__main__':
    unittest.main() 