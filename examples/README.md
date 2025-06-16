# GFS Intake Examples

This directory contains example scripts demonstrating how to use the Intake GFS NCAR driver for accessing Global Forecast System (GFS) data.

## Example Scripts

### Basic Examples

- `example_surface_winds.py` - Shows how to download and process GFS surface wind data (10m U and V components), calculate wind speed and direction, and save to NetCDF.

### Catalog-Based Examples

- `example_surface_winds_catalog.py` - Uses the dedicated `gfs_surface_winds` catalog dataset to access 10m wind components with pre-configured filters
- `example_ice_concentration_catalog.py` - Uses the dedicated `gfs_ice_concentration` catalog dataset to access sea ice concentration data with pre-configured filters

### Dataset-Specific Examples

The `dataset_examples` directory contains examples for working with the predefined datasets in the GFS catalog:

- `use_surface_winds.py` - Uses the predefined `gfs_surface_winds` dataset to access 10m wind components, calculate derived fields, visualize the data, and save to NetCDF.
- `use_ice_concentration.py` - Uses the predefined `gfs_ice_concentration` dataset to access sea ice concentration data, create polar visualizations, and save to NetCDF.

## Running the Examples

The examples can be run directly with Python:

```bash
# From the project root directory
python examples/example_surface_winds.py

# Catalog-based examples (recommended)
python examples/example_surface_winds_catalog.py
python examples/example_ice_concentration_catalog.py

# Or for dataset-specific examples (if available)
python examples/dataset_examples/use_surface_winds.py
python examples/dataset_examples/use_ice_concentration.py
```

## Dependencies

In addition to the base dependencies of `intake-gfs-ncar`, some examples require:

- `matplotlib` - For visualization
- `cartopy` - For map projections in visualization examples

You can install these with:

```bash
pip install matplotlib cartopy
```

## Output

Most examples will:
1. Download the requested GFS data from the NCAR THREDDS server
2. Process the data (calculating derived fields, etc.)
3. Save the processed data as NetCDF files in a `gfs_output` directory
4. Generate visualizations (where applicable)

The examples use data from recent days by default to ensure availability. The catalog-based examples (`*_catalog.py`) are recommended as they use pre-configured datasets that are simpler to use and more reliable.

## Catalog Datasets

The catalog includes the following pre-configured datasets:

- `gfs_surface_winds` - 10-meter wind components (U and V) with automatic variable mapping
- `gfs_ice_concentration` - Sea ice concentration data optimized for polar region analysis
- `gfs_forecast` - General-purpose dataset for custom variable selection

These datasets use NetCDF Subset Service (NCSS) for efficient data access and include pre-configured filters for common use cases.