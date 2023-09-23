import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from encription_by_shift import encrypt, decrypt

class TestEncryptionByShift(unittest.TestCase):

    @patch('os.getenv')
    def test_that_encryption_can_be_performed_successfully_even_when_the_calculation_results_include_characters_with_numbers_smaller_than_the_start_of_the_character_code(self, mock_getenv):
        mock_getenv.return_value = '3'
        
        info = "xyz"
        encrypted_info = encrypt(info)
        decrypted_info = decrypt(encrypted_info)
        
        self.assertEqual(info.upper(), decrypted_info)

if __name__ == "__main__":
    unittest.main()
