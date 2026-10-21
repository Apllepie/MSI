import os
from pathlib import Path
from maze import Maze
from object import Robot

def main():
    # Poprawna ścieżka do katalogu parent i pliku tekstowego
    FILE_PATH = Path(__file__).resolve().parent.parent / "labirynt.txt"
    
    # Zmieniona nazwa zmiennej z 'map' na 'gra_map', aby uniknąć konfliktu nazw
    labirynt = Maze(FILE_PATH)
    labirynt.display_maze()

    rob = Robot(1,1)
    nei = rob.get_neighbors(labirynt)
    print (nei)


if __name__ == "__main__":
    main()
