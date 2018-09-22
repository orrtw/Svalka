# Svalka

```
import numpy as np 
from scipy.io.netcdf import netcdf_file
import matplotlib.pyplot as plt
import json
with netcdf_file(r'C:\Users\Наталия .LAPTOP-61AJMTC8\MSR-2.nc', mmap=False) as f:
    variables = f.variables
print(variables['lon'].units)
print(variables['lat'].units)
lat_index = np.searchsorted(variables['lat'].data,-33.27)
lon_index = np.searchsorted(variables['lon'].data,-70.40) 
print('lon_index:',lon_index)
print('lat_index:',lat_index)
data = variables['Average_O3_column'][:, lat_index, lon_index][:]
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
print('min(jan) =', np.min(jan_data), 'max(jan) =', np.max(jan_data),'mean(jan) =', np.mean(jan_data))
print('min(jul) =', np.min(july_data), 'max(jul) =', np.max(july_data),'mean(jul) =', np.mean(july_data))
print('min(all) =', np.min(data), 'max(all) =', np.max(data),'mean(all) =', np.mean(data))
d = {
  "city": "Moscow",
  "coordinates": [-33.27, 70.40],
  "jan": {
    "min": 252.0,
    "max": 275.0,
    "mean": 263.05
  },
  "jul": {
    "min": 260.0,
    "max": 312.0,
    "mean": 291.48
  },
  "all": {
    "min": 246.0,
    "max": 334.0,
    "mean": 279.50
  }
}
with open('ozon.json', 'w') as f:
    json.dump(d, f)
with open('ozon.json', 'r') as f:
    print(f.read())
```
