import numpy as np
import pandas as pd
import xarray as xr

ds = xr.open_dataset('/home/misdan/Documents/Data/Angin/wind_1992.nc')
da = ds['u10'].sel(time='1992-02',latitude=6.0, longitude=95.20,method='nearest').data
print('--------------------------')
print('hasilnya adalah : ')
print(da)