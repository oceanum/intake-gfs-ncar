.. _quickstart:

Quickstart
==========

This guide will help you get started with ``intake-gfs-ncar`` by walking you through basic usage examples.

Basic Usage
----------

1. **Import the package and open the catalog**:

   .. code-block:: python

      import intake
      
      # Open the default catalog
      cat = intake.open_catalog("intake_gfs_ncar/gfs_catalog.yaml")
      
      # List available data sources
      print(list(cat))

2. **Create a data source for surface temperature**:

   .. code-block:: python

      # Get surface temperature data
      source = cat.gfs_forecast(
          date_str="2023-01-01",  # Forecast initialization date
          max_lead_time_fXXX="f024",  # Maximum lead time (24 hours)
          cfgrib_filter_by_keys={
              'typeOfLevel': 'surface',
              'shortName': '2t'  # 2m temperature
          }
      )
      
      # Display source metadata
      print(source.metadata)

3. **Read the data into an xarray Dataset**:

   .. code-block:: python

      # Read the data
      ds = source.read()
      print(ds)
      
      # Access the temperature data
      temperature = ds['t2m']
      print(temperature)

Working with Different Variables
------------------------------

You can access different variables by changing the ``shortName`` in the filter. Here are some common ones:

- ``'2t'``: 2m temperature (K)
- ``'10u'``: 10m U-component of wind (m/s)
- ``'10v'``: 10m V-component of wind (m/s)
- ``'msl'``: Mean sea level pressure (Pa)
- ``'tcc'``: Total cloud cover (0-1)

Example with wind data:

.. code-block:: python

   # Get wind data at 10m
   wind_source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cfgrib_filter_by_keys={
           'typeOfLevel': 'surface',
           'shortName': ['10u', '10v']  # Both U and V components
       }
   )
   
   wind_data = wind_source.read()
   print(wind_data)

Accessing Different Vertical Levels
--------------------------------

To access data at different vertical levels, change the ``typeOfLevel`` and ``level`` parameters:

.. code-block:: python

   # Get temperature at 500hPa
   temp_500_source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cfgrib_filter_by_keys={
           'typeOfLevel': 'isobaricInhPa',
           'level': 500,
           'shortName': 't'  # Temperature
       }
   )
   
   temp_500 = temp_500_source.read()
   print(temp_500)

Working with Time Series
-----------------------

To work with multiple forecast times, you can loop through lead times:

.. code-block:: python

   import xarray as xr
   
   # Initialize an empty list to store datasets
   datasets = []
   
   # Loop through lead times
   for lead_time in [f"f{hour:03d}" for hour in range(0, 25, 6)]:  # 0h to 24h in 6h steps
       source = cat.gfs_forecast(
           date_str="2023-01-01",
           max_lead_time_fXXX=lead_time,
           cfgrib_filter_by_keys={
               'typeOfLevel': 'surface',
               'shortName': '2t'
           }
       )
       ds = source.read()
       datasets.append(ds)
   
   # Combine datasets along the time dimension
   combined = xr.concat(datasets, dim='time')
   print(combined)

Saving Data
----------

You can save the data to various formats using xarray's I/O methods:

.. code-block:: python

   # Save to NetCDF
   ds.to_netcdf('gfs_data.nc')
   
   # Save to Zarr (better for large datasets)
   ds.to_zarr('gfs_data.zarr', mode='w')

Next Steps
----------

- Learn more about :ref:`configuration options <configuration>`
- Explore :ref:`advanced usage examples <examples>`
- Check the :ref:`FAQ <faq>` for common issues
