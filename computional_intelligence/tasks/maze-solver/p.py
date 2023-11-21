# # import matplotlib.pyplot as plt
# # import matplotlib.animation as animation

# # # Function to update the animation
# # def update(frame):
# #     # Update the positions of the two points
# #     point1.set_data(frame, 5)  # Horizontal movement at the top
# #     point2.set_data(frame, frame)  # Diagonal movement towards the top

# # # Set up the figure and axes
# # fig, ax = plt.subplots()
# # ax.set_xlim(0, 10)
# # ax.set_ylim(0, 10)

# # # Initialize the points
# # point1, = ax.plot([], [], 'ro')  # Point moving horizontally
# # point2, = ax.plot([], [], 'bo')  # Point moving diagonally

# # # Create the animation
# # ani = animation.FuncAnimation(fig, update, frames=range(48), interval=250, repeat=True)

# # plt.show()



import matplotlib.pyplot as plt

# Define the maze as a 2D list where 0 represents an open path and 1 represents a wall
maze_data = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

def plot_maze(maze):
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == 1:
                plt.fill_between([col_index, col_index + 1], row_index, row_index + 1, color='black')  # Wall
            else:
                plt.fill_between([col_index, col_index + 1], row_index, row_index + 1, color='white')  # Open path

# Plot the maze
plot_maze(maze_data)

# Set start and goal points
start_point = (1, 1)
goal_point = (3, 5)

# Mark the start and goal points
plt.scatter(*start_point, color='green', marker='o', s=100, label='Start')
plt.scatter(*goal_point, color='red', marker='x', s=100, label='Goal')

# Configure plot settings
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()
