from collections import namedtuple


Punkt = namedtuple('Punkt', ['x', 'y'])

class Object:
    def __init__(self, x, y):
        # 2. Przypisujemy instancję Punktu do atrybutu self.position
        self.position = Punkt(x, y)

    def set_pos(self, pos: Punkt):
        self.position = pos

    
class Goal(Object):
    def check_pos(self, pos: Punkt):
        if pos.x == self.position.x and pos.y == self.position.y:
            return True
        else:
            return False


class Robot(Object):
    def get_neighbors(self, maze):
        """
        Zwraca tylko DOZWOLONE punkty sąsiadujące (bez ścian i poza granicami).
        """
        x, y = self.position.x, self.position.y
        
        potentials = [
            Punkt(x, y - 1),  # Góra
            Punkt(x, y + 1),  # Dół
            Punkt(x - 1, y),  # Lewo
            Punkt(x + 1, y)   # Prawo
        ]
        
        valid_neighbors = []
        height = len(maze.grid)
        width = len(maze.grid[0]) if height > 0 else 0

        for p in potentials:
            # 1. Sprawdzenie granic labiryntu
            if 0 <= p.y < height and 0 <= p.x < width:
                # 2. Sprawdzenie, czy to nie jest ściana ("1")
                if maze.grid[p.y][p.x] != "1":
                    valid_neighbors.append(p)
                    
        return valid_neighbors