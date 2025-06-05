.. _release_notes:

Release Notes
=============

This document summarizes the changes in each release of ``intake-gfs-ncar``.

.. _unreleased:

Unreleased
----------

**Added:**
- Initial release of the package
- Support for accessing GFS forecast data from NCAR NOMADS
- Basic filtering by variable, level, and forecast time
- Integration with xarray and Dask for data analysis

**Changed:**
- N/A

**Fixed:**
- N/A

**Deprecated:**
- N/A

**Removed:**
- N/A

**Security:**
- N/A

Versioning
---------

This project follows `Semantic Versioning <https://semver.org/>`_ (SemVer).

Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

Changelog
--------

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

### Added
- Initial project setup with basic GFS data access functionality
- Documentation and examples
- Test suite

### Changed
- N/A

### Fixed
- N/A

### Security
- N/A

Maintainer Notes
----------------

### Creating a New Release

1. Update the version number in ``intake_gfs_ncar/__init__.py``
2. Update this changelog with the new version and changes
3. Commit the changes with a message like "Bump version to X.Y.Z"
4. Create a git tag: ``git tag vX.Y.Z``
5. Push the tag: ``git push origin vX.Y.Z``
6. The GitHub Actions workflow will automatically publish to PyPI

### Backward Compatibility

- Always maintain backward compatibility within the same MAJOR version
- Use deprecation warnings when removing or changing functionality
- Document any breaking changes in the release notes

### Deprecation Policy

- Deprecated features will be marked with a ``DeprecationWarning``
- Features will be removed after being deprecated for at least one MINOR version
- The deprecation notice will include the version in which the feature will be removed
