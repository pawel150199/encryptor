import sys
from prettytable import  PrettyTable
from decryptor import Decryptor
from encryptor import Encryptor

# Main part
if __name__=='__main__':
    
    n = True;
    while n:

        """Function of this script"""
        print("\n\n\n Simple Encryption app: \n\n\n")
        myTable = PrettyTable(['Function', 'key'])
        myTable.add_row(["Demo", 1])
        myTable.add_row(["Encryption", 2])
        myTable.add_row(["Decryption", 3])
        myTable.add_row(["Encryption text file", 4])
        myTable.add_row(["Decryption text file", 5])
        myTable.add_row(["Exit", 6])
        print(myTable)
        
        i = input("\t\t\nChose function: ")

        if i == '1': 
            """Demo of usage program"""
            plain_text = input("Input text:  ")
            key = []
            example = Encryptor(plain_text)
            
            x = example.code()
            y = example.keying()

            encoding = Decryptor(x,y)
            encoding.encode()


        elif  i == '2':
            text = input("\nInput text to encryption: ")
            key = []
            szyfrowanie = Encryptor(text)
            szyfrowanie.code()


        elif i == '3':
            szyfrogram = input("\nInput text to decryption: ")
            key = input("\nInput key: ")
            deszyfrowanie = Decryptor(szyfrogram, key)
            deszyfrowanie.encode()
        
        elif i == '4':
            key = []
            xd = []

            filename = input("\t\nInput filename to encryption: ")
            with open(filename, 'r', encoding = 'utf-8') as f:
                xd = str(f.read())

            szyfrowanie = Encryptor(xd)
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
