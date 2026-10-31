from collections import namedtuple, deque

Punkt = namedtuple('Punkt', ['x', 'y'])

class Object:
    def __init__(self, x: int, y: int):
        self.position = Punkt(x, y)

    def set_pos(self, pos: Punkt):
        self.position = pos


class Goal(Object):
    def check_pos(self, pos: Punkt) -> bool:
        return pos.x == self.position.x and pos.y == self.position.y


class Robot(Object):
    def get_neighbors(self, maze, pos: Punkt = None) -> list[Punkt]:
        """Zwraca dozwolonych sąsiadów dla podanej pozycji (lub pozycji robota)."""
        curr = pos if pos is not None else self.position
        x, y = curr.x, curr.y
        
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
            if 0 <= p.y < height and 0 <= p.x < width:
                if maze.grid[p.y][p.x] != "1":
                    valid_neighbors.append(p)
                    
        return valid_neighbors

    def reconstruct_path(self, parent: dict, start: Punkt, goal: Punkt) -> list[Punkt]:
        """Odtwarza ścieżkę od S do G na podstawie słownika poprzedników."""
        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = parent.get(curr)
        path.reverse()
        return path

    def bfs(self, maze):
        """Algorytm przeszukiwania wszerz (BFS). Zwraca (ścieżka, liczba_odwiedzonych_węzłów)."""
        start = maze.start_pos
        goal = maze.goal_pos

        queue = deque([start])
        visited = {start}
        parent = {start: None}
        visited_count = 0

        while queue:
            curr = queue.popleft()
            visited_count += 1

            if curr == goal:
                return self.reconstruct_path(parent, start, goal), visited_count

            for neighbor in self.get_neighbors(maze, curr):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    queue.append(neighbor)

        return None, visited_count

    def dfs(self, maze):
        """Algorytm przeszukiwania w głąb (DFS). Zwraca (ścieżka, liczba_odwiedzonych_węzłów)."""
        start = maze.start_pos
        goal = maze.goal_pos

        stack = [start]
        visited = {start}
        parent = {start: None}
        visited_count = 0

        while stack:
            curr = stack.pop()
            visited_count += 1

            if curr == goal:
                return self.reconstruct_path(parent, start, goal), visited_count

            for neighbor in self.get_neighbors(maze, curr):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    stack.append(neighbor)

        return None, visited_count