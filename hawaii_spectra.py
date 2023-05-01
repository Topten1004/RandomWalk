import csv
import matplotlib.pyplot as plt

filename = 'Data/2023-01-08_4_3C.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    wavelengths = []
    spectra_combined = [[] for _ in range(len(header_row)-1)]

    for row in reader:
        if len(row) > 0:
            wavelength = float(row[0])
            wavelengths.append(wavelength)
            for index, data in enumerate(row[1:]):
                spectra_combined[index].append(float(data))

# Plot the data
plt.style.use('classic')
fig, ax = plt.subplots()
ax.set_xlabel('Wavelength')
ax.set_ylabel('Reflectance')

for spectrum in spectra_combined:
    ax.plot(wavelengths, spectrum)

plt.show()