.. _installation:

Installation
============

This guide will help you install the ``intake-gfs-ncar`` package and its dependencies.

Prerequisites
------------

- Python 3.8 or higher
- pip (Python package installer)

Installation Methods
-------------------

From PyPI (recommended)
~~~~~~~~~~~~~~~~~~~~~~

To install the latest stable release from PyPI:

.. code-block:: bash

   pip install intake-gfs-ncar

From Source
~~~~~~~~~~~

If you want to install the latest development version or modify the source code:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/oceanum/intake-gfs-ncar.git
      cd intake-gfs-ncar

2. Install in development mode with all dependencies:

   .. code-block:: bash

      pip install -e ".[dev]"

Dependencies
-----------

The core dependencies are automatically installed with the package:

- `intake <https://intake.readthedocs.io/>`_
- `xarray <https://xarray.pydata.org/>`_
- `dask <https://dask.org/>`_
- `cfgrib <https://github.com/ecmwf/cfgrib>`_
- `fsspec <https://filesystem-spec.readthedocs.io/>`_
- `aiohttp <https://docs.aiohttp.org/>`_
- `requests <https://docs.python-requests.org/>`_
- `beautifulsoup4 <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

Optional dependencies:

- For running tests: `pytest`, `pytest-cov`
- For code formatting: `black`, `isort`
- For static type checking: `mypy`
- For linting: `pylint`

Verifying the Installation
-------------------------

To verify that the package is installed correctly, you can run:

.. code-block:: python

   import intake
   import intake_gfs_ncar
   
   print(f"Intake version: {intake.__version__}")
   print(f"intake-gfs-ncar version: {intake_gfs_ncar.__version__}")

If you don't see any errors, the installation was successful.

Troubleshooting
--------------

Common issues and their solutions:

1. **Error installing cfgrib**:
   - Ensure you have the ECCODES library installed
   - On Ubuntu/Debian: ``sudo apt-get install libeccodes-dev``
   - On macOS: ``brew install eccodes``

2. **Import errors**:
   - Make sure you've activated the correct Python environment
   - Try reinstalling the package: ``pip install --force-reinstall intake-gfs-ncar``

3. **SSL certificate errors**:
   - If you encounter SSL certificate errors, you may need to update your certificates
   - On Linux: Update your system's CA certificates
   - Or set the environment variable: ``export CURL_CA_BUNDLE=/path/to/cert.pem``

For additional help, please open an issue on the `GitHub repository <https://github.com/oceanum/intake-gfs-ncar/issues>`_.
