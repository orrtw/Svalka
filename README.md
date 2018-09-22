# Svalka

```
import numpy as np 
from scipy.io.netcdf import netcdf_file
import matplotlib.pyplot as plt
import json
with netcdf_file(r'C:\Users\Наталия .LAPTOP-61AJMTC8\MSR-2.nc', mmap=False) as f:
    variables = f.variables
latitude_index = np.searchsorted(variables['latitude'].data,-33.27)
longitude_index = np.searchsorted(variables['longitude'].data,-70.40) 
data = variables['Average_O3_column'][:, latitude_index, longitude_index][:]
january_data = data[::12]
july_data = data[6::12]
time = variables['time'][:]
january_time=time[::12]
july_time=time[6::12]
plt.plot(variables['time'].data, data,label = 'Все время') 
plt.plot(january_time, january_data, label = 'Январь')
plt.plot(july_time, july_data, label = 'Июль')
plt.legend()
plt.grid()
plt.savefig('ozon.png')
print('min(Январь) =', np.min(january_data), 'max(Январь) =', np.max(january_data),'mean(Январь) =', np.mean(january_data))
print('min(Июль) =', np.min(july_data), 'max(Июль) =', np.max(july_data),'mean(Июль) =', np.mean(july_data))
print('min(Все) =', np.min(data), 'max(Все) =', np.max(data),'mean(Все) =', np.mean(data))
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
