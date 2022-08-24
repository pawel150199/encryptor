from Encryptor import Encryptor
from Decryptor import Decryptor
import unittest

class Test(unittest.TestCase):
    def testEncryption(self):
        text = "SimpleText12344$@3"
        encryptor = Encryptor(text)
        text_enc = encryptor.code()
        key = encryptor.keying()
        self.assertIsInstance(encryptor, Encryptor)
        self.assertRaises(ValueError)

    def testE2E(self):
        text = "SimpleText12344$@3"
        encryptor = Encryptor(text)
        text_enc = encryptor.code()
        key = encryptor.keying()
        decryptor = Decryptor(text_enc, key)
        plain_text = decryptor.encode()
        self.assertIsInstance(encryptor, Encryptor)
        self.assertRaises(ValueError)
        self.assertEqual(plain_text, text)

if __name__ == "__main__":
    unittest.main()
        