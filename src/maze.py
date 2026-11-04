import os
from object import Punkt

class Maze:
    def __init__(self, file_path: str):
        self.file_path = str(file_path)
        self.grid = []
        self.start_pos = None
        self.goal_pos = None
        
        self.load_maze()

    def load_maze(self):
        """Wczytuje plik tekstowy, waliduje dane i ustala pozycje S oraz G."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Nie znaleziono pliku mapy pod ścieżką: {self.file_path}")
            
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip().replace(' ', '') for line in file if line.strip()]
        
        if not lines:
            raise ValueError("Błąd walidacji: Plik labiryntu jest pusty.")

        # 1. Walidacja prostokątności planszy
        width = len(lines[0])
        if not all(len(line) == width for line in lines):
            raise ValueError("Błąd walidacji: Plansza labiryntu nie jest prostokątna.")

        # 2. Walidacja dozwolonych znaków i zliczanie S oraz G
        allowed_chars = {'0', '1', 'S', 'G'}
        start_count = 0
        goal_count = 0

        self.grid = []
        for r, line in enumerate(lines):
            row = list(line)
            for c, char in enumerate(row):
                if char not in allowed_chars:
                    raise ValueError(f"Błąd walidacji: Niedozwolony znak '{char}' na pozycji ({r}, {c}).")
                if char == 'S':
                    start_count += 1
                    self.start_pos = Punkt(c, r)  # x=kolumna, y=wiersz
                elif char == 'G':
                    goal_count += 1
                    self.goal_pos = Punkt(c, r)
            self.grid.append(row)

        # 3. Sprawdzenie jednoznaczności S i G
        if start_count != 1:
            raise ValueError(f"Błąd walidacji: Oczekiwano 1 punktu S, znaleziono: {start_count}.")
        if goal_count != 1:
            raise ValueError(f"Błąd walidacji: Oczekiwano 1 punktu G, znaleziono: {goal_count}.")

    def display_maze(self, path=None):
        """Wyświetla planszę z opcjonalnym nakładaniem ścieżki."""
        SCIANA = "\033[32m██ \033[0m"
        SCIEZKA = "\033[30m░░ \033[0m"
        START = "\033[94m▒▒ \033[0m"
        META = "\033[1;37m▒▒ \033[0m"
        TRASA = "\033[33m** \033[0m"

        path_set = set(path) if path else set()

        for y, row in enumerate(self.grid):
            colored_row = []
            for x, cell in enumerate(row):
                p = Punkt(x, y)
                if cell == "S":
                    colored_row.append(START)
                elif cell == "G":
                    colored_row.append(META)
                elif p in path_set:
                    colored_row.append(TRASA)
                elif cell == "1":
                    colored_row.append(SCIANA)
                elif cell == "0":
                    colored_row.append(SCIEZKA)
            print("".join(colored_row))