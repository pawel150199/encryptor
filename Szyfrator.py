from prettytable import PrettyTable
import datetime
import math
import sys



"""ENCRYPTOR"""
class Encryptor:
    def __init__(self, plain_text, key):
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
        print("\t\t\t\tSzyfrator")
        print("\n\n")
        print(myTable)
        print("\n\n\n")
        # Return Encrypted value as a string
        return "".join(coded_text)


"""                           Deszyfrator                  """


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
            """   Właściwe szyfrowanie    """
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

if __name__=='__main__':

    n = True;
    while n:

        """Function of this script"""
        print("\n\n\nFunctions : \n\n\n")
        myTable = PrettyTable(['Function', 'key'])
        myTable.add_row(["demo", 1])
        myTable.add_row(["Encryption", 2])
        myTable.add_row(["Decryption", 3])
        myTable.add_row(["Encryption text file", 4])
        myTable.add_row(["Decryption text file", 5])
        myTable.add_row(["Exit", 6])
        print(myTable)
        
        i = input("\t\t\nChose function: ")

        if i == '1': 
            """ Szyfrowanie  i deszyfrowanie - prezentacja działania"""
            plain_text = input("Input text:  ")
            key = []
            example = Encryptor(plain_text, key)
            
            x = example.code()
            y = example.keying()

            encoding = Decryptor(x,y)
            encoding.encode()


        elif  i == '2':
            text = input("\nInput text to encryption: ")
            key = []
            szyfrowanie = Szyfrator(text, key)
            szyfrowanie.code()


        elif i == '3':
            szyfrogram = input("\nInput text to decryption: ")
            key = input("\nWprowadz klucz deszyfrujący")
            deszyfrowanie = Deszyfrator(szyfrogram, key)
            deszyfrowanie.encode()
        
        elif i == '4':
            key = []
            xd = []

            filename = input("\t\nInput filename to encryption: ")
            with open(filename, 'r', encoding = 'utf-8') as f:
                xd = str(f.read())

            szyfrowanie = Encryptor(xd, key)
            x = szyfrowanie.code()

            print("\tSaved to file encrypted information")
            with open (filename, 'w', encoding = 'utf-8') as f:
                f.write(x)
        
        elif i == '5':
            
            xd = []
            filename = input("\t\nInput filename to decryption")
            key = input("nInput key: ")
            with open(filename, 'r', encoding = 'utf-8') as f:
                xd = str(f.read())

            deszyfrowanie = Decryptor(xd, key)
            x = deszyfrowanie.encode()

            print("\tSaved plain text to file")
            with open (filename, 'w', encoding = 'utf-8') as f:
                f.write(x)

        elif i =='6':
            sys.exit(" \n\nGoodbye")
        
        else:
            sys.exit("\n\nIncorrect value, please try one more time")
