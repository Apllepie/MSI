import os

class Maze:
    def __init__(self, file_path: str):
        """
        Inicjalizuje obiekt mapy na podstawie podanej ścieżki do pliku.
        """
        self.file_path = file_path
        self.grid = []
        
        # Automatycznie wczytaj mapę przy tworzeniu obiektu
        self.load_maze()

    def load_maze(self):
        """
        Wczytuje plik tekstowy i zapisuje go jako dwuwymiarową listę (tablicę).
        """
        # Bezpieczne sprawdzenie, czy plik w ogóle istnieje
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Nie znaleziono pliku mapy pod ścieżką: {self.file_path}")
            
        with open(self.file_path, 'r', encoding='utf-8') as file:
            # Wczytujemy linię po linii, usuwając białe znaki z końca (np. \n)
            self.grid = [list(line.strip()) for line in file if line.strip()]
    def display_maze(self):
        """
        Wyświetla mapę o zbalansowanej szerokości, używając pojedynczego bloku 
        i spacji, aby zapobiec rozciąganiu w pionie i poziomie.
        """
        # Każdy element ma teraz dokładnie 2 znaki szerokości (znak + spacja)
        SCIANA = "\033[32m██ \033[0m"       # Blok i spacja
        SCIEZKA = "\033[30m░░ \033[0m"      # Kropka i spacja
        START = "\033[94m▒▒ \033[0m"        # Litera S i spacja
        META = "\033[31m▒▒ \033[0m"         # Litera G i spacja

        for row in self.grid:
            colored_row = []
            for cell in row:
                if cell == "1":
                    colored_row.append(SCIANA)
                elif cell == "0":
                    colored_row.append(SCIEZKA)
                elif cell == "S":
                    colored_row.append(START)
                elif cell == "G":
                    colored_row.append(META)
                #else:
                   # colored_row.append(cell + " ") 
            
            # Łączymy znaki bez dodatkowych spacji
            print("".join(colored_row))
