from prettytable import PrettyTable
import datetime
import math
import sys

class Encryptor:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.key = [] 

    def keying(self):
        # Return table with key nessesary to decryption
        return self.key

    def code(self):
        # Storage for encrypted information
        coded_text = []
         # Temporary table to encryption process
        tmp = []

        for i in range(0, len(self.plain_text)):
            # Current time
            now = datetime.datetime.now()
            # Current time needed to set lifetime of key
            hour = now.strftime('%H')
            tmp.append(chr(int(hour)+ i+1))
        
        for i in range(0, len(self.plain_text)):
            """Encryption process"""
            x = ord(self.plain_text[i])
            c = x * ord(tmp[i])
            m = math.floor(c/60) + 65
            self.key.append(chr(m))
            d = (c % 60) + 64
            # Store encrypted value in table
            coded_text.append(chr(d))


        """Print encrypted information"""
        myTable = PrettyTable(["      plain text      ", "          key           ", "       Encrypted information       "])
        myTable.add_row(["".join(self.plain_text), "".join(self.key), "".join(coded_text)])
        print("\n\n\n")
        print("\t\t\t\tEncryptor")
        print("\n\n")
        print(myTable)
        print("\n\n\n")
        # Return Encrypted value as a string
        return "".join(coded_text)
