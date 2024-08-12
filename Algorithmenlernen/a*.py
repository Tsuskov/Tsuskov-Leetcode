import random
import heapq
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource


# Maze generation
def generate_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    stack = []

    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def is_wall(x, y):
        return maze[y][x] == '#'

    def set_path(x, y):
        maze[y][x] = ' '

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and is_wall(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def remove_wall(x1, y1, x2, y2):
        maze[(y1 + y2) // 2][(x1 + x2) // 2] = ' '

    start_x, start_y = random.randint(0, width // 2) * 2, random.randint(0, height // 2) * 2
    stack.append((start_x, start_y))
    set_path(start_x, start_y)

    while stack:
        x, y = stack[-1]
        neighbors = get_neighbors(x, y)
        if neighbors:
            nx, ny = random.choice(neighbors)
            remove_wall(x, y, nx, ny)
            set_path(nx, ny)
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# A* search algorithm
def heuristic(a, b):
    """Calculate the Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal, grid):
    """Perform A* search on the grid."""
    width, height = len(grid[0]), len(grid)
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    open_set = {start}

    while open_list:
        _, current_g, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        open_set.remove(current)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < width and 0 <= neighbor[1] < height:
                if grid[neighbor[1]][neighbor[0]] == ' ':
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                        if neighbor not in open_set:
                            heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))
                            open_set.add(neighbor)

    return []  # Return an empty list if no path is found

# Plotting with Bokeh
def update_plot(path, grid, start, goal, width, height):
    """Update the plot based on the path found."""
    x, y, color = [], [], []
    if path is None:
        path = []  # Ensure path is always a list

    for i in range(width):
        for j in range(height):
            x.append(i)
            y.append(j)
            if grid[j][i] == '#':
                color.append('black')
            elif (i, j) == start:
                color.append('blue')
            elif (i, j) == goal:
                color.append('red')
            elif (i, j) in path:
                color.append('yellow')
            else:
                color.append('white')
    
    return x, y, color

# Configuration
width, height = 100, 100
start = (0, 0)
goal = (55, 88)

# Generate maze
maze = generate_maze(width, height)

# Solve maze
path = a_star_search(start, goal, maze)

# Prepare Bokeh plot
x, y, color = update_plot(path, maze, start, goal, width, height)
source = ColumnDataSource(data=dict(x=x, y=y, color=color))

plot = figure(title="A* Pathfinding", x_range=(-1, width), y_range=(-1, height), 
              width=500, height=500)
plot.rect(x='x', y='y', width=1, height=1, source=source, color='color', line_color=None)

# Output to file
output_file("a_star_pathfinding.html")

# Configuration
width, height = 200, 200  # Increase the width and height for better resolution
start = (0, 0)
goal = (55, 88)
# Generate maze
maze = generate_maze(width, height)
# Solve maze
path = a_star_search(start, goal, maze)
# Prepare Bokeh plot
x, y, color = update_plot(path, maze, start, goal, width, height)
source = ColumnDataSource(data=dict(x=x, y=y, color=color))
plot = figure(title="A* Pathfinding", x_range=(-1, width), y_range=(-1, height), 
              width=800, height=800)  # Increase the width and height of the plot for better resolution
plot.rect(x='x', y='y', width=1, height=1, source=source, color='color', line_color=None)
# Output to file
output_file("a_star_pathfinding.html")
show(plot)




