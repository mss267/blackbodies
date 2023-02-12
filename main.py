import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Select one of the files
filename = input('Filename: ')

# Given wavelength x in metres, returns temperature at that wavelength in percent relative to a 3000K black body
def func(x, temp):
    h = 6.63E-34
    light = 3E8
    k = 1.38E-23

    # Black body function
    y = (2 * h * light * light) / (x**5 * (np.exp(h * light / (x * k * temp)) - 1))

    # Scale factor for relative intensity
    a = (2 * h * light * light) / ((961E-9)**5 * (np.exp(h * light / ((961*1E-9) * k * 3000)) - 1)) 

    # Convert to relative intensity in %
    return(y / a * 100.0)

csvname = filename + '.csv'

# Read data from csvs
wavelength_nm = np.genfromtxt(csvname, delimiter = ',', skip_header = 1, dtype = float, usecols = [0])
data = np.genfromtxt(csvname, delimiter = ',', skip_header = 1, dtype = float, usecols = [1])

# Plot data
plt.plot(wavelength_nm, data)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Relative Intensity %')
plt.title(filename)

plotname = filename + '.pdf'
plt.savefig(plotname)

# Initial temperature guess in K for fitting function
init_t = [1000]

# Perform fit
popt, pcov = curve_fit(func, wavelength_nm/1E9, data, p0=init_t)

# Print temerature
print("Temperature", popt[0], "K")
