import numpy as np
import matplotlib.pyplot as plt
import random

# Define the size of the galaxy
width = 800
height = 800

# Create a numpy array to hold the fractal galaxy
galaxy = np.zeros((height, width))

# Define the properties of the fractal galaxy
galaxy_density = random.uniform(0.5, 1)
galaxy_size = random.uniform(0.1, 0.5)
galaxy_aspect_ratio = random.uniform(0.5, 2)

# Generate the fractal galaxy
for y in range(height):
    for x in range(width):
        galaxy[y][x] = galaxy_density * (np.exp(-((x / width - 0.5) ** 2 / (galaxy_size * galaxy_aspect_ratio) ** 2 + (y / height - 0.5) ** 2 / galaxy_size ** 2)))

# Normalize the fractal galaxy
galaxy = (galaxy - galaxy.min()) / (galaxy.max() - galaxy.min())

# Generate a random color map
color_map = np.zeros((256, 3))
for i in range(256):
    color_map[i] = [random.random(), random.random(), random.random()]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the fractal galaxy
ax.imshow(galaxy, cmap='gray')

# Add the colorbar
fig.colorbar(ax.imshow(galaxy, cmap='gray'))

# Show the plot
plt.show()
