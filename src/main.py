import os
from pathlib import Path
from maze import Maze

def main():
    # Poprawna ścieżka do katalogu parent i pliku tekstowego
    FILE_PATH = Path(__file__).resolve().parent.parent / "labirynt.txt"
    
    # Zmieniona nazwa zmiennej z 'map' na 'gra_map', aby uniknąć konfliktu nazw
    labirynt = Maze(FILE_PATH)
    labirynt.display_maze()


if __name__ == "__main__":
    main()
