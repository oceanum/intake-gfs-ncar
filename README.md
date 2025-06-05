# Intake GFS NCAR

An [Intake](https://intake.readthedocs.io/) driver for accessing Global Forecast System (GFS) data from the NCAR NOMADS server.

## Features

- Access GFS forecast data through a simple Python interface
- Supports filtering by variable, level, and forecast lead time
- Built on xarray and cfgrib for efficient handling of GRIB2 data
- Supports both single files and time series of forecast files
- Compatible with Dask for out-of-core computations

## Installation

```bash
pip install intake-gfs-ncar
```

## Usage

### Basic Usage

```python
import intake

# Open the catalog
cat = intake.open_catalog("gfs_catalog.yaml")

# Get a data source for surface variables
source = cat.gfs_forecast(
    cycle="2023-01-01T00:00:00",  # Forecast cycle in ISO format
    max_lead_time=24,  # Maximum forecast lead time in hours
    cfgrib_filter_by_keys={
        'typeOfLevel': 'surface',  # Get surface variables
        'step': 3  # 3-hour forecast step
    }
)

# Load the data as an xarray Dataset
ds = source.read()
print(ds)
```

### Available Parameters

- `cycle`: Forecast cycle in ISO format (e.g., '2023-01-01T00:00:00') or 'latest'
- `max_lead_time`: Maximum forecast lead time in hours (e.g., 24)
- `cfgrib_filter_by_keys`: Dictionary of GRIB filter parameters (see below)
- `base_url`: Base URL for the NOMADS server (defaults to NCAR's server)

### GRIB Filter Keys

You can filter the GRIB data using any of the following keys in the `cfgrib_filter_by_keys` parameter:

- `typeOfLevel`: Type of level (e.g., 'surface', 'isobaricInhPa')
- `level`: Pressure level in hPa (for isobaric levels)
- `shortName`: Variable short name (e.g., 't' for temperature, 'u' for u-wind)
- `step`: Forecast step in hours

## Examples

### Get 500 hPa geopotential height

```python
source = cat.gfs_forecast(
    cycle="2023-01-01T00:00:00",
    max_lead_time=24,
    cfgrib_filter_by_keys={
        'typeOfLevel': 'isobaricInhPa',
        'level': 500,
        'shortName': 'gh'
    }
)
```

### Get surface temperature

```python
source = cat.gfs_forecast(
    cycle="2023-01-01T00:00:00",
    max_lead_time=24,
    cfgrib_filter_by_keys={
        'typeOfLevel': 'surface',
        'shortName': '2t'  # 2m temperature
    }
)
```

### Predefined Datasets

The catalog also includes predefined datasets with common filter configurations:

#### Surface Winds

```python
# Get 10m wind components (u10, v10)
source = cat.gfs_surface_winds(
    cycle="2023-01-01T00:00:00",
    max_lead_time=24
)
```

#### Sea Ice Concentration

```python
# Get sea ice concentration data
source = cat.gfs_ice_concentration(
    cycle="2023-01-01T00:00:00",
    max_lead_time=24
)
```

## Development

### Installation from source

```bash
git clone https://github.com/oceanum/intake-gfs-ncar.git
cd intake-gfs-ncar
pip install -e '.[dev]'
```

### Running tests

```bash
pytest
```

### Code formatting

```bash
black .
isort .
```

## License

MIT

## Acknowledgements

This package was developed by [Oceanum](https://oceanum.science) with support from the wider scientific Python community.
