.. _examples:

Examples
========

This page contains practical examples demonstrating how to use ``intake-gfs-ncar`` for various common tasks.

Basic Example: Surface Temperature
---------------------------------

Load and plot surface temperature data:

.. code-block:: python

   import intake
   import matplotlib.pyplot as plt
   import cartopy.crs as ccrs
   import cartopy.feature as cfeature
   import numpy as np

   # Open the catalog
   cat = intake.open_catalog("intake_gfs_ncar/gfs_catalog.yaml")
   
   # Get surface temperature data
   source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cfgrib_filter_by_keys={
           'typeOfLevel': 'surface',
           'shortName': '2t'  # 2m temperature
       }
   )
   ds = source.read()
   
   # Plot the data
   plt.figure(figsize=(12, 8))
   ax = plt.axes(projection=ccrs.PlateCarree())
   ds['t2m'].isel(time=0).plot(ax=ax, transform=ccrs.PlateCarree())
   ax.coastlines()
   ax.add_feature(cfeature.BORDERS, linestyle=':')
   plt.title("Surface Temperature (K)")
   plt.show()

Wind Vectors
-----------

Plot wind vectors at 10m height:

.. code-block:: python

   import xarray as xr
   
   # Get wind components
   wind_source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cfgrib_filter_by_keys={
           'typeOfLevel': 'surface',
           'shortName': ['10u', '10v']
       }
   )
   wind_ds = wind_source.read()
   
   # Plot wind vectors (subsampled for clarity)
   plt.figure(figsize=(12, 8))
   ax = plt.axes(projection=ccrs.PlateCarree())
   
   # Subset the data (every 4th point)
   subset = wind_ds.isel(longitude=slice(None, None, 4), latitude=slice(None, None, 4))
   
   # Plot wind vectors
   q = ax.quiver(
       subset.longitude, subset.latitude,
       subset['u10'], subset['v10'],
       transform=ccrs.PlateCarree(),
       scale=300, width=0.002
   )
   
   ax.coastlines()
   ax.add_feature(cfeature.BORDERS, linestyle=':')
   plt.title("10m Wind Vectors")
   plt.show()

Vertical Profile
---------------

Extract and plot a vertical profile of temperature:

.. code-block:: python

   # Get temperature at multiple pressure levels
   temp_levels = [1000, 925, 850, 700, 500, 300, 200, 100]
   
   # Get data for all levels
   temp_profiles = []
   for level in temp_levels:
       source = cat.gfs_forecast(
           date_str="2023-01-01",
           max_lead_time_fXXX="f000",  # Analysis time
           cfgrib_filter_by_keys={
               'typeOfLevel': 'isobaricInhPa',
               'level': level,
               'shortName': 't'
           }
       )
       temp_profiles.append(source.read())
   
   # Combine into a single dataset
   temp_profile = xr.concat(temp_profiles, dim='isobaricInhPa')
   
   # Plot the vertical profile at a specific location
   plt.figure(figsize=(8, 10))
   temp_profile['t'].isel(longitude=100, latitude=100, time=0).plot(y='isobaricInhPa', yincrease=False)
   plt.title('Temperature Profile')
   plt.ylabel('Pressure (hPa)')
   plt.grid(True)
   plt.show()

Time Series Analysis
-------------------

Analyze temperature trends at a specific location over time:

.. code-block:: python

   import pandas as pd
   
   # Get temperature time series at a specific point
   times = [f"f{hour:03d}" for hour in range(0, 73, 6)]  # 0h to 72h in 6h steps
   
   temps = []
   for time in times:
       source = cat.gfs_forecast(
           date_str="2023-01-01",
           max_lead_time_fXXX=time,
           cfgrib_filter_by_keys={
               'typeOfLevel': 'surface',
               'shortName': '2t'
           }
       )
       ds = source.read()
       # Select a specific location (e.g., New York)
       ny_temp = ds['t2m'].sel(
           longitude=285,  # Approx. -75°E
           latitude=40,    # 40°N
           method='nearest'
       )
       temps.append(float(ny_temp.values))
   
   # Create a time series
   time_index = pd.date_range("2023-01-01", periods=len(times), freq="6H")
   ts = pd.Series(temps, index=time_index)
   
   # Plot the time series
   plt.figure(figsize=(12, 5))
   ts.plot()
   plt.title("Surface Temperature Time Series (New York)")
   plt.ylabel("Temperature (K)")
   plt.grid(True)
   plt.show()

Saving and Loading Data
----------------------

Save processed data for later use:

.. code-block:: python

   # Save to NetCDF
   ds.to_netcdf('gfs_data.nc')
   
   # Save to Zarr (better for large datasets)
   ds.to_zarr('gfs_data.zarr', mode='w')
   
   # Load saved data
   ds_loaded = xr.open_dataset('gfs_data.nc')
   # or
   # ds_loaded = xr.open_zarr('gfs_data.zarr')

Advanced: Using Dask for Large Datasets
-------------------------------------

For large datasets, use Dask for lazy loading and parallel computation:

.. code-block:: python

   import dask.array as da
   
   # Enable Dask's distributed scheduler (optional)
   # from dask.distributed import Client
   # client = Client()
   
   # Get data with chunks
   source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       chunks={'time': 1, 'latitude': 100, 'longitude': 100},
       cfgrib_filter_by_keys={
           'typeOfLevel': 'surface',
           'shortName': '2t'
       }
   )
   
   # This doesn't load the data yet
   ds = source.to_dask()
   
   # Compute mean temperature (triggers computation)
   mean_temp = ds['t2m'].mean().compute()
   print(f"Global mean temperature: {mean_temp.values} K")
