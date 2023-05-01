import numpy as np
import matplotlib.pyplot as plt

# Define the boundaries of your region of interest
min_lat, max_lat = 33, 37
min_lon, max_lon = 119, 123

# Set the central latitude and longitude as the starting point for your random walk
lat, lon = (min_lat + max_lat) / 2, (min_lon + max_lon) / 2

# Generate a random walk
n_steps = 10000
step_size = 0.5 # Change this value to adjust the spatial resolution of the random walk
lats, lons = [lat], [lon]
for i in range(n_steps):
    lat += np.random.uniform(-step_size, step_size)
    lon += np.random.uniform(-step_size, step_size)
    if lat < min_lat or lat > max_lat:
        lat -= np.sign(lat - (min_lat + max_lat) / 2) * (lat - (min_lat + max_lat) / 2) * 2
    if lon < min_lon or lon > max_lon:
        lon -= np.sign(lon - (min_lon + max_lon) / 2) * (lon - (min_lon + max_lon) / 2) * 2
    lats.append(lat)
    lons.append(lon)

# Plot the random walk on a map
fig, ax = plt.subplots()
ax.scatter(lons, lats, s=10, c=lats, cmap='viridis')
ax.set_xlim(min_lon, max_lon)
ax.set_ylim(min_lat, max_lat)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Random Walk')
plt.show()
