import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Generate random walk data
num_steps = 10000
step_size = 0.1
lon = np.cumsum(np.random.uniform(low=-step_size, high=step_size, size=num_steps))
lat = np.cumsum(np.random.uniform(low=-step_size, high=step_size, size=num_steps))

# Set up basemap
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', lat_0=50, lon_0=-100)

# Plot random walk
x, y = m(lon, lat)
m.plot(x, y, color='blue', linewidth=1, alpha=0.5)

# Draw map features
m.drawcoastlines()
m.fillcontinents(color='lightgray', lake_color='white')
m.drawmapboundary(fill_color='white')

# Show plot
plt.show()
