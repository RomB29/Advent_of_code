grid = []
file_path = "input_8.py"

for line in open(file_path):
    for l in line.strip().split("\n"):
        grid.append([int(c) for c in l])

# Get the number of rows and columns in the grid
num_rows = len(grid)
num_cols = len(grid[0])

# Initialize a counter for the number of visible trees
num_visible_trees = 0

# Iterate through each tree in the grid
for i in range(num_rows):
    for j in range(num_cols):
        # Check if the tree is on the edge of the grid
        if i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1:
            num_visible_trees += 1
            continue
        
        # Check if the tree is visible from the left
        visible_from_left = True
        for k in range(j):
            if grid[i][k] >= grid[i][j]:
                visible_from_left = False
                break
        
        # Check if the tree is visible from the right
        visible_from_right = True
        for k in range(j + 1, num_cols):
            if grid[i][k] >= grid[i][j]:
                visible_from_right = False
                break
        
        # Check if the tree is visible from the top
        visible_from_top = True
        for k in range(i):
            if grid[k][j] >= grid[i][j]:
                visible_from_top = False
                break
        
        # Check if the tree is visible from the bottom
        visible_from_bottom = True
        for k in range(i + 1, num_rows):
            if grid[k][j] >= grid[i][j]:
                visible_from_bottom = False
                break
        
        # If the tree is visible from any direction, increment the counter
        if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
            num_visible_trees += 1

# Print the number of visible trees
print(num_visible_trees)


# Get the number of rows and columns in the grid
num_rows = len(grid)
num_cols = len(grid[0])

# Initialize a variable to keep track of the highest scenic score seen so far
# Set the initial maximum scenic score to 0
max_scenic_score = 0

# Iterate over the rows in the grid
for i in range(len(grid)):
    # Iterate over the columns in the row
    for j in range(len(grid[i])):
        # Compute the viewing distance in each direction
        view_up = 0
        view_down = 0
        view_left = 0
        view_right = 0

        # Compute the viewing distance in the up direction
        for k in range(i - 1, -1, -1):
            # If we encounter a tree that is taller than the current tree, stop
            if grid[k][j] >= grid[i][j]:
                view_up += 1
                break
            # Otherwise, increment the viewing distance by 1
            view_up += 1

        # Compute the viewing distance in the down direction
        for k in range(i + 1, len(grid)):
            if grid[k][j] >= grid[i][j]:
                view_down += 1
                break
            view_down += 1

        # Compute the viewing distance in the left direction
        for k in range(j - 1, -1, -1):
            if grid[i][k] >= grid[i][j]:
                view_left += 1
                break
            view_left += 1

        # Compute the viewing distance in the right direction
        for k in range(j + 1, len(grid[i])):
            if grid[i][k] >= grid[i][j]:
                view_right += 1
                break
            view_right += 1

        # Compute the scenic score for the current tree
        scenic_score = view_up * view_down * view_left * view_right

        # Update the maximum scenic score if necessary
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

# Print the maximum scenic score
print(max_scenic_score)