from prettytable import PrettyTable
import datetime

class Decryptor:
    def __init__(self, coded_text, key):
        self.coded_text = coded_text
        self.key = key
    
    def encode(self):
        tmp = []
        plain_text = []

        for i in range(0, len(self.coded_text)): 
            now = datetime.datetime.now()
            hour = now.strftime('%H')
            tmp.append(chr(int(hour)+ i+1))


        for i in range(0, len(self.coded_text)):
            """Decryption"""
            x = ord(self.coded_text[i])
            d = x - 64
            c = (ord(self.key[i]) - 65) * 60 + d
            l = c/ord(tmp[i])
            plain_text.append(chr(int(l)))


        """Decrypted information"""
        myTable = PrettyTable(["        Encrypted information       ", "          key         ", "    Decrypted information     "])
        myTable.add_row(["".join(self.coded_text), "".join(self.key), "".join(plain_text)])
        print("\n\n\n")
        print("\t\t\t\tDecryptor")
        print("\n\n")
        print(myTable)
        print("\n\n\n")
        # Return plain text as a string
        return "".join(plain_text)
        