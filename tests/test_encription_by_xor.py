import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from encription_by_xor import xor_conversion

class TestEncryptionByXOR(unittest.TestCase):

    @patch('os.getenv')
    def test_that_encryption_can_be_performed_successfully_even_when_the_calculation_results_include_characters_with_numbers_smaller_than_the_start_of_the_character_code(self, mock_getenv):
        mock_getenv.return_value = '3'

        info = "test"
        encrypted_info = xor_conversion(info)
        decrypted_info = xor_conversion(encrypted_info)
        
        self.assertEqual(info, decrypted_info)

if __name__ == "__main__":
    unittest.main()
