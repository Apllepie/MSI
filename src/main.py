from pathlib import Path
from maze import Maze
from object import Robot

FILE_NAME = "labirynt4.txt"


def print_cost(path):
    """Wyświetla koszt ścieżki (długość trasy w krokach)."""
    if path:
        print(f"Koszt ścieżki: {len(path) - 1} kroków.")
    else:
        print("Nie znaleziono ścieżki.")

def main():
    FILE_PATH = Path(__file__).resolve().parent.parent / FILE_NAME
    
    try:
        labirynt = Maze(FILE_PATH)
    except Exception as e:
        print(f"Błąd podczas wczytywania labiryntu: {e}")
        return

    print("--- Otwarty labirynt ---")
    labirynt.display_maze()
    print(f"\nPozycja Start (S): {labirynt.start_pos}")
    print(f"Pozycja Cel (G):   {labirynt.goal_pos}\n")

    # Inicjalizacja robota w punkcie startowym
    rob = Robot(labirynt.start_pos.x, labirynt.start_pos.y)

    # 1. Przeszukiwanie BFS
    print("=" * 40)
    print(" WYNIKI ALGORYTMU BFS ")
    print("=" * 40)
    bfs_path, bfs_visited = rob.bfs(labirynt)
    if bfs_path:
        labirynt.display_maze(path=bfs_path)
        print_cost(bfs_path)
        print(f"Liczba odwiedzonych stanów: {bfs_visited}")
    else:
        print("Brak ścieżki do celu!")

    # 2. Przeszukiwanie DFS
    print("\n" + "=" * 40)
    print(" WYNIKI ALGORYTMU DFS ")
    print("=" * 40)
    dfs_path, dfs_visited = rob.dfs(labirynt)
    if dfs_path:
        labirynt.display_maze(path=dfs_path)
        print_cost(dfs_path)
        print(f"Liczba odwiedzonych stanów: {dfs_visited}")
    else:
        print("Brak ścieżki do celu!")

if __name__ == "__main__":
    main()