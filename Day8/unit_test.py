import unittest
import change_text

class TestChangeText(unittest.TestCase):
    def test_all_upper(self):
        msg = "Good morning"
        result = change_text.all_upper(msg)
        self.assertEqual(result, 'GOOD MORNING', 'Expected: GOOD MORNING')

if __name__ == '__main__':
    unittest.main()