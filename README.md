# Svalka

```
import numpy as np \\
from scipy.io.netcdf import netcdf_file\\
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
with netcdf_file(r'C:\Users\Наталия .LAPTOP-61AJMTC8\MSR-2.nc', mmap=False) as f:
    variables = f.variables
latitude_index = np.searchsorted(variables['latitude'].data,-33.27)
longitude_index = np.searchsorted(variables['longitude'].data,-70.40) 
data = variables['Average_O3_column'][:, latitude_index, longitude_index][:]
january_data = data[::12]
july_data = data[6::12]
print(january_data)
print(july_data)
print(july_data.size)
time = variables['time'][:]
january_time=time[::12]
july_time=time[6::12]
plt.plot(variables['time'].data, data,label = 'За все время') 
plt.plot(january_time, january_data, label = 'Январь')
plt.plot(july_time, july_data, label = 'Июль')
```
