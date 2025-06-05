.. intake-gfs-ncar documentation master file, created by
   sphinx-quickstart on Wed May 28 14:55:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _intake-gfs-ncar:

intake-gfs-ncar
===============

.. image:: https://img.shields.io/pypi/v/intake-gfs-ncar.svg
   :target: https://pypi.python.org/pypi/intake-gfs-ncar
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/l/intake-gfs-ncar.svg
   :target: https://github.com/oceanum/intake-gfs-ncar/blob/main/LICENSE
   :alt: License

.. image:: https://github.com/oceanum/intake-gfs-ncar/actions/workflows/tests.yaml/badge.svg
   :target: https://github.com/oceanum/intake-gfs-ncar/actions/workflows/tests.yaml
   :alt: Tests

.. image:: https://readthedocs.org/projects/intake-gfs-ncar/badge/?version=latest
   :target: https://intake-gfs-ncar.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

``intake-gfs-ncar`` is an `Intake <https://intake.readthedocs.io/>`_ driver for accessing Global Forecast System (GFS) data from the NCAR NOMADS server. It provides a convenient way to load GFS forecast data into xarray Datasets for analysis and visualization.

Features
--------

- Simple, Pythonic API for accessing GFS forecast data
- Built on top of the Intake data catalog system
- Uses xarray for labeled, multi-dimensional data structures
- Supports Dask for out-of-core and parallel computation
- Caching of downloaded data to minimize network usage
- Supports filtering by variable, level, and forecast time

Getting Started
--------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   
   getting_started/installation
   getting_started/quickstart
   getting_started/examples

User Guide
----------

.. toctree::
   :maxdepth: 2
   :caption: User Guide
   
   user_guide/configuration
   user_guide/usage
   user_guide/faq

API Reference
------------

.. toctree::
   :maxdepth: 2
   :caption: API Reference
   
   api/generated/intake_gfs_ncar
   api/generated/intake_gfs_ncar.gfs_intake_driver

Development
-----------

.. toctree::
   :maxdepth: 2
   :caption: Development
   
   development/contributing
   development/release_notes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

License
-------
This project is licensed under the MIT License - see the :ref:`LICENSE <license>` file for details.

Acknowledgements
----------------
This project was developed by `Oceanum <https://oceanum.io>`_ and is part of the `intake <https://intake.readthedocs.io/>`_ ecosystem.

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.
