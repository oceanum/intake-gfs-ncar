.. _configuration:

Configuration
=============

This guide explains how to configure the ``intake-gfs-ncar`` package to suit your needs.

Catalog Configuration
--------------------

The package includes a default catalog file (``intake_gfs_ncar/gfs_catalog.yaml``) with the following structure:

.. code-block:: yaml

   sources:
     gfs_forecast:
       driver: gfs_forecast
       description: GFS forecast data from NCAR NOMADS
       metadata:
         tags: ['weather', 'forecast', 'gfs', 'nomads', 'ncep', 'atmospheric']
         source: NCEP NOMADS GFS 0.25 degree forecast
         license: Public Domain
         intake_esm_varname: gfs_forecast
       parameters:
         date_str:
           description: Forecast initialization date in YYYY-MM-DD format or 'latest'
           type: str
           default: latest
         max_lead_time_fXXX:
           description: Maximum forecast lead time (e.g., 'f024' for 24 hours)
           type: str
           default: f024
         base_url:
           description: Base URL for the NOMADS server
           type: str
           default: https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod
         model_run_time:
           description: Model run time in 'HH' format (e.g., '00' for 00Z run)
           type: str
           default: '00'

Customizing the Catalog
----------------------

You can create a custom catalog file to modify the default settings. Here's how to use a custom catalog:

1. Create a new YAML file (e.g., ``my_gfs_catalog.yaml``)
2. Copy and modify the default catalog structure as needed
3. Load your custom catalog:

   .. code-block:: python

      import intake
      cat = intake.open_catalog('path/to/my_gfs_catalog.yaml')

Available Parameters
-------------------

The following parameters can be specified when creating a data source:

- ``date_str``: Forecast initialization date in 'YYYY-MM-DD' format or 'latest'
- ``max_lead_time_fXXX``: Maximum forecast lead time (e.g., 'f024' for 24 hours)
- ``base_url``: Base URL for the NOMADS server
- ``model_run_time``: Model run time in 'HH' format (e.g., '00', '06', '12', '18')
- ``chunks``: Dictionary specifying chunk sizes for Dask arrays (e.g., {'time': 1, 'latitude': 100, 'longitude': 100})
- ``cfgrib_filter_by_keys``: Dictionary of GRIB filter keys (see below)

GRIB Filter Keys
---------------

The ``cfgrib_filter_by_keys`` parameter allows you to filter the GRIB data. Common filter keys include:

- ``typeOfLevel``: Type of vertical level (e.g., 'surface', 'isobaricInhPa', 'heightAboveGround')
- ``level``: Specific level value (e.g., 500 for 500hPa, 2 for 2m above ground)
- ``shortName``: Parameter short name (e.g., '2t' for 2m temperature, '10u' for 10m U-wind)
- ``step``: Forecast step in hours

Example of using filter keys:

.. code-block:: python

   # Get 500hPa geopotential height
   source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cfgrib_filter_by_keys={
           'typeOfLevel': 'isobaricInhPa',
           'level': 500,
           'shortName': 'z'  # Geopotential height
       }
   )

Environment Variables
-------------------

You can configure the package using the following environment variables:

- ``INTAKE_GFS_NCAR_CACHE_DIR``: Directory to cache downloaded GRIB files (default: ``~/.intake/gfs_ncar``)
- ``INTAKE_GFS_NCAR_CACHE_TTL``: Time-to-live for cached files in seconds (default: 86400 = 1 day)
- ``INTAKE_GFS_NCAR_MAX_RETRIES``: Maximum number of retry attempts for failed downloads (default: 3)
- ``INTAKE_GFS_NCAR_TIMEOUT``: Request timeout in seconds (default: 30)

Example of setting environment variables:

.. code-block:: bash

   # In your shell
   export INTAKE_GFS_NCAR_CACHE_DIR="$HOME/.my_gfs_cache"
   export INTAKE_GFS_NCAR_CACHE_TTL=3600  # 1 hour

Or in Python:

.. code-block:: python

   import os
   os.environ['INTAKE_GFS_NCAR_CACHE_DIR'] = '/path/to/cache'
   os.environ['INTAKE_GFS_NCAR_CACHE_TTL'] = '3600'

Caching Behavior
---------------

The package caches downloaded GRIB files to avoid redundant downloads. The cache behavior can be controlled with:

- ``cache=True/False``: Enable/disable caching (default: True)
- ``cache_dir``: Override the cache directory
- ``cache_ttl``: Override the cache time-to-live in seconds

Example:

.. code-block:: python

   # Disable caching
   source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cache=False,
       cfgrib_filter_by_keys={'typeOfLevel': 'surface', 'shortName': '2t'}
   )
   
   # Use a custom cache directory
   source = cat.gfs_forecast(
       date_str="2023-01-01",
       max_lead_time_fXXX="f024",
       cache_dir="/tmp/my_gfs_cache",
       cache_ttl=3600,  # 1 hour
       cfgrib_filter_by_keys={'typeOfLevel': 'surface', 'shortName': '2t'}
   )

Troubleshooting Configuration
---------------------------

1. **Connection Issues**:
   - Check your internet connection
   - Verify the server URL is accessible
   - Try increasing the timeout value

2. **GRIB Decoding Errors**:
   - Ensure you have the latest version of cfgrib and eccodes
   - Check that the GRIB filter keys match the available fields

3. **Memory Issues**:
   - Use chunking for large datasets
   - Consider using Dask for out-of-core computation
   - Increase system memory if needed

For additional help, refer to the :ref:`FAQ <faq>` or open an issue on the `GitHub repository <https://github.com/oceanum/intake-gfs-ncar/issues>`_.
