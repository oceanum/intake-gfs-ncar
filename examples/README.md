# GFS Intake Examples

This directory contains example scripts demonstrating how to use the Intake GFS NCAR driver for accessing Global Forecast System (GFS) data.

## Example Scripts

### Basic Examples

- `example_surface_winds.py` - Shows how to download and process GFS surface wind data (10m U and V components), calculate wind speed and direction, and save to NetCDF.

### Dataset-Specific Examples

The `dataset_examples` directory contains examples for working with the predefined datasets in the GFS catalog:

- `use_surface_winds.py` - Uses the predefined `gfs_surface_winds` dataset to access 10m wind components, calculate derived fields, visualize the data, and save to NetCDF.
- `use_ice_concentration.py` - Uses the predefined `gfs_ice_concentration` dataset to access sea ice concentration data, create polar visualizations, and save to NetCDF.

## Running the Examples

The examples can be run directly with Python:

```bash
# From the project root directory
python examples/example_surface_winds.py

# Or for dataset-specific examples
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
1. Download the requested GFS data from the NCAR NOMADS server
2. Process the data (calculating derived fields, etc.)
3. Save the processed data as NetCDF files in a `gfs_output` directory
4. Generate visualizations (where applicable)

The examples use data from 3 days ago by default to ensure availability.