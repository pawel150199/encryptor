from prettytable import PrettyTable
import datetime
import math
import sys



"""                         Szyfrator                 """
class Szyfrator:
    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = [] 

    def keying(self):
        return self.key# zwraca tablice która zawiera klucz potrzebny do odszyfrowania

    def code(self):
        coded_text = [] #tablica do której zapisuje zakodowany tekst
        tmp = [] # Tymczasowa tablica potrzebna do zaszyfrowania

        for i in range(0, len(self.plain_text)): 
            now = datetime.datetime.now() # zapisuję aktualny czas
            hour = now.strftime('%H') # określam w tej zmiennej akttualną godzinę i uzywam jej przy szyfrowaniu dzieki temu wazność klucza to max godzina
            tmp.append(chr(int(hour)+ i+1)) #wartości zapisuję w tabeli
        
        for i in range(0, len(self.plain_text)):
            """      Właściwe szyfrowanie      """
            x = ord(self.plain_text[i]) #w zmiennej x zapisuję wartości dziesietne kodu ASCII
            c = x * ord(tmp[i]) #dokonuję mnozenia plain_textu razy tablice ttmp ktora jest iterowana
            m = math.floor(c/60) + 65 #uzywam funkcji podloga z dzielenia aby potem w deszyfratorze odzyskac wartosc c
            self.key.append(chr(m)) #wypelniam ttablice kluczem
            d = (c % 60) + 64 #reszta z dzielenia
            coded_text.append(chr(d)) #wypełniam zaszyfrowaną tablicę


        """     Zapisuję szyfrogram w tabeli dla przejrzystości     """
        myTable = PrettyTable(["      tekst jawny      ", "          klucz           ", "       Szyfrogram       "])
        myTable.add_row(["".join(self.plain_text), "".join(self.key), "".join(coded_text)])
        print("\n\n\n")
        print("\t\t\t\tSzyfrator") #informacja dla uzytkownika
        print("\n\n")
        print(myTable) # wyświetlam tabele
        print("\n\n\n")
        return "".join(coded_text) #zwracam zakodowany text jako string dla łatwości odczytu


"""                           Deszyfrator                  """


class Deszyfrator:
    def __init__(self, coded_text, key):
        self.coded_text = coded_text
        self.key = key
    
    def encode(self):
        tmp = [] # tablica, w której zapisuje dane potrzebne do deszyfrowania
        plain_text = [] # zapisuje tu tekst rozszyfrowany

        for i in range(0, len(self.coded_text)): 
            now = datetime.datetime.now() # zapisuję aktualny czas
            hour = now.strftime('%H') # określam w tej zmiennej akttualną godzinę i uzywam jej przy szyfrowaniu dzieki temu wazność klucza to max godzina
            tmp.append(chr(int(hour)+ i+1)) #wartości zapisuję w tabeli


        for i in range(0, len(self.coded_text)):
            """   Właściwe szyfrowanie    """
            x = ord(self.coded_text[i]) #wartość dkodu ASCII dla poszczególnych wartości szyfrogramu
            d = x - 64  #wartość z dzielenia modulo - 60
            c = (ord(self.key[i]) - 65) * 60 + d # wartość c z Szyfratora
            l = c/ord(tmp[i]) #wartość c z Szyfratora
            plain_text.append(chr(int(l))) # do tablicy zapisuje poszczególne wartości szyfrogramu


        """     Zapisuję rozszyfrowaną wiadomość w tabeli dla przejrzystości     """
        myTable = PrettyTable(["        Szyfrogram       ", "          key         ", "    tekst rozszyfrowany     "])
        myTable.add_row(["".join(self.coded_text), "".join(self.key), "".join(plain_text)])
        print("\n\n\n")
        print("\t\t\t\tDeszyfrator")
        print("\n\n")
        print(myTable)
        print("\n\n\n")
        return "".join(plain_text) #zwracam zakodowany text jako sttring dla łatwości odczytu

if __name__=='__main__':

    n = True;
    while n:

        """     Spis funkcji programu    """
        print("\n\n\nFunkcje programu : \n\n\n")
        myTable = PrettyTable(['Funkcjonalność', 'Klawisz funkcyjny'])
        myTable.add_row(["Prezentacja działania", 1])
        myTable.add_row(["Szyfrowanie", 2])
        myTable.add_row(["Deszyfrowanie", 3])
        myTable.add_row(["Zaszyfrowanie pliku tekstowego", 4])
        myTable.add_row(["Odszyfrowanie pliku tekstowego", 5])
        myTable.add_row(["Wyjście z programu", 6])
        print(myTable)
        
        i = input("\t\t\nWybierz funkcję programu: ")

        if i == '1': 
            """ Szyfrowanie  i deszyfrowanie - prezentacja działania"""
            plain_text = input("Podaj tekst:  ") #wprowadzenie tekstu przez uzytkownika
            key = [] # tablica z kluczem
            example = Szyfrator(plain_text, key) #deklaracja obiektu
            
            x = example.code() # szyfrowanie 
            y = example.keying() # ta funkcja zwraca klucz aby w kolejnym kroku dokonac deszyfrowania

            encoding = Deszyfrator(x,y) # Deszyfrowanie 
            encoding.encode()


        elif  i == '2':
            text = input("\nPodaj tekst, który chcesz zaszyfrować: ") #wprowadzenie tekstu przez uzytkownika
            key = [] #tablica z kluczem
            szyfrowanie = Szyfrator(text, key) #deklaracja obiektu
            szyfrowanie.code() #Szyfrowanie 


        elif i == '3':
            szyfrogram = input("\nPodaj tekst, który chcesz odszyfrować: ") #wprowadzenie tekstu przez uzytkownika
            key = input("\nWprowadz klucz deszyfrujący") #tablica z kluczem
            deszyfrowanie = Deszyfrator(szyfrogram, key) #deklaracja obiektu
            deszyfrowanie.encode() #Deszyfrowanie 
        
        elif i == '4':
            key = [] #tablica z kluczem
            xd = [] #pomocnicza tablica

            filename = input("\t\nPodaj nazwę pliku który chcesz zaszyfrować") #nazwa szyfrowanego pliku
            with open(filename, 'r', encoding = 'utf-8') as f: #odczyt danych z pliku tekstowego
                xd = str(f.read())

            szyfrowanie = Szyfrator(xd, key) #Szyfrowanie
            x = szyfrowanie.code()  #SZyfrowanie

            print("\tZapisano do pliku zaszyfrowaną wiadomość")   
            with open (filename, 'w', encoding = 'utf-8') as f: #Zapisanie zaszyfrowaej widomości do pliku tekstowego
                f.write(x)
        
        elif i == '5':
            
            xd = []
            filename = input("\t\nPodaj nazwę pliku który chcesz odszyfrować") #nazwa szyfrowanego pliku
            key = input("Podaj klucz deszyfrujący: ")
            with open(filename, 'r', encoding = 'utf-8') as f: #odczyt danych z pliku tekstowego
                xd = str(f.read())

            deszyfrowanie = Deszyfrator(xd, key)
            x = deszyfrowanie.encode()

            print("\tZapisano do pliku odszyfrowaną wiadomość")
            with open (filename, 'w', encoding = 'utf-8') as f: #Zapisanie zaszyfrowaej widomości do pliku tekstowego
                f.write(x)

        elif i =='6':
            sys.exit(" \n\nMiło było mi zademonstrować Ci działanie szyfru zaprojektowanego przez Pawła Polskiego")
        
        else:
            sys.exit("\n\nWprowadzono błędny parametr")
