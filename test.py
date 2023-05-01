import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

# Set up the basemap
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_global()

# Add map features
ax.coastlines(resolution='110m', linewidth=0.5)
ax.gridlines(draw_labels=True, xlocs=[-180,-120,-60,0,60,120,180], ylocs=[-90,-60,-30,0,30,60,90])

# Generate random walk data
nsteps = 10000
stepsize = 10000
lat, lon = 51.5074, -0.1278
lons = np.ones(nsteps) * lon
lats = np.ones(nsteps) * lat

for i in range(1, nsteps):
    # Generate a random direction and distance
    direction = 2 * np.pi * np.random.random()
    distance = stepsize * np.random.random()
    
    # Calculate the new latitude and longitude
    lats[i] = lats[i-1] + distance / 111000.0 * np.cos(direction)
    lons[i] = lons[i-1] + distance / 111000.0 * np.sin(direction) / np.cos(np.radians(lat))

# Convert latitudes and longitudes to basemap coordinates
x, y = ax.projection.transform_points(ccrs.PlateCarree(), lons, lats)[:, :2].T

# Plot the random walk
ax.scatter(x, y, s=1, color='red')

# Show the plot
plt.show()
