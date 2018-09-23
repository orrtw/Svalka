# Svalka

```
import numpy as np 
from scipy.io.netcdf import netcdf_file
import matplotlib.pyplot as plt
import json
with netcdf_file(r'C:\Users\Наталия .LAPTOP-61AJMTC8\MSR-2.nc', mmap=False) as f:
    variables = f.variables
print(variables['longitude'].units)
print(variables['latitude'].units)
latitude_index = np.searchsorted(variables['latitude'].data,-33.27)
longitude_index = np.searchsorted(variables['longitude'].data,-70.40) 
print('longitude_index:',longitude_index)
print('latitude_index:',latitude_index)
data = variables['Average_O3_column'][:, latitude_index, longitude_index][:]
jan_data = data[::12]
july_data = data[6::12]
time = variables['time'][:]
jan_time=time[::12]
july_time=time[6::12]
plt.plot(variables['time'].data, data,label = 'Все время') 
plt.plot(jan_time, jan_data, label = 'Январь')
plt.plot(july_time, july_data, label = 'Июль')
plt.legend()
plt.grid()
plt.savefig('ozon.png')
d = {
  "city": "Santiago de Chile",
  "coordinates": [-33.27, 70.40],
  "jan": {
    "min": float(np.min(jan_data)),
    "max": float(np.max(jan_data)),
    "mean": float(np.mean(jan_data))
  },
  "jul": {
    "min": float(np.min(july_data)),
    "max": float(np.max(july_data)),
    "mean": float(np.mean(july_data))
  },
  "all": {
    "min": float(np.min(data)),
    "max": float(np.max(data)),
    "mean": float(np.mean(data))
  }
}
with open('ozon.json', 'w') as f:
    json.dump(d, f)
with open('ozon.json', 'r') as f:
    print(f.read())
    f.seek(0)



```
