.. _faq:

Frequently Asked Questions
=========================

This page answers common questions about using the ``intake-gfs-ncar`` package.

General Questions
----------------

What is intake-gfs-ncar?
~~~~~~~~~~~~~~~~~~~~~~~
``intake-gfs-ncar`` is an `Intake <https://intake.readthedocs.io/>`_ driver for accessing Global Forecast System (GFS) data from the NCAR NOMADS server. It provides a convenient way to load GFS forecast data into xarray Datasets for analysis and visualization.

What Python versions are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The package supports Python 3.8 and later.

How do I cite this package?
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you use this package in your research, please cite it as:

.. code-block:: bibtex

   @software{intake_gfs_ncar,
     author = {Oceanum Developers},
     title = {intake-gfs-ncar: An Intake driver for GFS forecast data},
     year = {2023},
     publisher = {GitHub},
     journal = {GitHub repository},
     howpublished = {\url{https://github.com/oceanum/intake-gfs-ncar}}
   }

Installation Issues
------------------

I'm getting an error about missing ECCODES. How do I fix this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``cfgrib`` package requires the ECCODES library. Install it using your system package manager:

- **Ubuntu/Debian**:
  .. code-block:: bash

     sudo apt-get install libeccodes-dev

- **macOS (Homebrew)**:
  .. code-block:: bash

     brew install eccodes

- **Conda**:
  .. code-block:: bash

     conda install -c conda-forge eccodes

I'm getting SSL certificate errors. What should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you encounter SSL certificate verification errors, you can try:

1. Updating your system's CA certificates:
   - On Ubuntu/Debian: ``sudo apt-get update && sudo apt-get install ca-certificates``
   - On macOS: Update your system through System Preferences

2. If that doesn't work, you can disable SSL verification (not recommended for security reasons):
   .. code-block:: python

      import os
      os.environ['CURL_CA_BUNDLE'] = ''
      os.environ['REQUESTS_CA_BUNDLE'] = ''

Usage Questions
--------------

How do I know what variables are available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can explore available variables using the following approaches:

1. Check the GRIB parameter table from NCEP: `NCEP GRIB2 Table <https://www.nco.ncep.noaa.gov/sib/params/grib2_table4-2-0-0.html>`_

2. Use the ``cfgrib`` tools to inspect a GRIB file:
   .. code-block:: bash

      cfgrib dump file.grib2

3. In Python, you can list available variables after loading a dataset:
   .. code-block:: python

      print(list(ds.data_vars))

How can I access data at specific coordinates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use xarray's selection methods to access data at specific coordinates:

.. code-block:: python

   # Select by coordinate values (nearest neighbor)
   point = ds.sel(
       latitude=40.71,  # New York City latitude
       longitude=-74.01,  # New York City longitude
       method='nearest'
   )
   
   # Select by index
   point = ds.isel(latitude=100, longitude=200)

How do I convert units?
~~~~~~~~~~~~~~~~~~~~~~
You can use the ``pint-xarray`` package to handle unit conversions:

.. code-block:: python

   import xarray as xr
   import pint_xarray  # noqa: F401
   
   # Convert temperature from Kelvin to Celsius
   temp_c = ds['t2m'].pint.quantify().pint.to('degC')

Performance Issues
----------------

The data loading is slow. How can I improve performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Try these optimizations:

1. **Use chunking**: Load data in smaller chunks
   .. code-block:: python

      source = cat.gfs_forecast(
          # ... other parameters ...
          chunks={'time': 1, 'latitude': 100, 'longitude': 100}
      )

2. **Use Dask for parallel processing**:
   .. code-block:: python

      import dask.array as da
      from dask.distributed import Client
      
      client = Client()  # Start a local Dask cluster
      
      # Your existing code here
      ds = source.to_dask()
      
      # Process data in parallel
      result = ds.mean().compute()

3. **Cache results**: Enable caching to avoid re-downloading the same data

I'm running out of memory. What should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For large datasets:

1. Use chunking to process data in smaller pieces
2. Use Dask for out-of-core computation
3. Consider using a machine with more RAM
4. Process one time step or variable at a time

Data Questions
-------------

What is the spatial resolution of the data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The default configuration uses the 0.25-degree GFS data, which has a spatial resolution of approximately 25 km.

How often is the data updated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GFS data is typically updated every 6 hours (00Z, 06Z, 12Z, 18Z), with a delay of about 3-4 hours after the model run time.

What is the temporal resolution?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The temporal resolution varies by forecast lead time:
- Hourly for the first 120 hours
- 3-hourly from 120 to 240 hours

Troubleshooting
--------------

I'm getting "No data found" errors. What's wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This can happen if:

1. The requested data is not yet available (check the server status)
2. The GRIB filter keys don't match any available fields
3. The server is temporarily unavailable

Try these steps:
1. Verify the server status
2. Check the filter keys against the GRIB parameter table
3. Try a different forecast time or date

How do I enable debug logging?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To enable debug logging, add this to your code:

.. code-block:: python

   import logging
   logging.basicConfig(level=logging.DEBUG)

This will print detailed information about the data loading process.

Where can I get help?
~~~~~~~~~~~~~~~~~~~~
For additional help:

1. Check the `GitHub Issues <https://github.com/oceanum/intake-gfs-ncar/issues>`_
2. Open a new issue if you've found a bug
3. Check the `Intake documentation <https://intake.readthedocs.io/>`_ for general usage help
