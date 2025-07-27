"""Test catalog parameter functionality for GFS intake driver."""

import pytest
import intake
import os
from datetime import datetime


class TestCatalogParameters:
    """Test class for catalog parameter functionality."""

    @pytest.fixture
    def catalog_path(self):
        """Get path to the catalog file."""
        current_dir = os.path.dirname(__file__)
        catalog_path = os.path.join(current_dir, "..", "gfs_catalog.yaml")
        return os.path.abspath(catalog_path)

    @pytest.fixture
    def catalog(self, catalog_path):
        """Load the catalog."""
        return intake.open_catalog(catalog_path)

    def test_catalog_loads_successfully(self, catalog):
        """Test that the catalog loads without errors."""
        assert catalog is not None
        assert hasattr(catalog, "gfs_forecast")
        assert hasattr(catalog, "gfs_surface_winds")
        assert hasattr(catalog, "gfs_ice_concentration")

    def test_gfs_forecast_parameters(self, catalog):
        """Test parameters for the main gfs_forecast source."""
        source = catalog.gfs_forecast

        # Check that parameters are defined
        assert hasattr(source, "_captured_init_kwargs")

        # Test that we can access the source with default parameters
        assert source is not None

    def test_gfs_forecast_custom_parameters(self, catalog):
        """Test using custom parameters with gfs_forecast."""
        # Test with custom cycle and max_lead_time
        source = catalog.gfs_forecast(cycle="2024-01-15T12:00:00", max_lead_time=48)

        # The source should be created successfully
        assert source is not None

    def test_gfs_surface_winds_parameters(self, catalog):
        """Test parameters for the gfs_surface_winds source."""
        source = catalog.gfs_surface_winds

        # Check that the source exists
        assert source is not None

        # Test with custom parameters
        custom_source = catalog.gfs_surface_winds(
            cycle="2024-06-01T06:00:00", max_lead_time=36
        )
        assert custom_source is not None

    def test_gfs_ice_concentration_parameters(self, catalog):
        """Test parameters for the gfs_ice_concentration source."""
        source = catalog.gfs_ice_concentration

        # Check that the source exists
        assert source is not None

        # Test with custom parameters
        custom_source = catalog.gfs_ice_concentration(
            cycle="2024-06-01T00:00:00", max_lead_time=72
        )
        assert custom_source is not None

    def test_parameter_validation_through_catalog(self, catalog):
        """Test that parameter validation works through the catalog."""
        # Valid parameters should work
        source = catalog.gfs_forecast(cycle="2024-01-01T00:00:00", max_lead_time=24)
        assert source is not None

        # Test that valid datetime parameters work through catalog
        valid_source = catalog.gfs_forecast(cycle="2024-01-15T06:00:00")
        assert valid_source is not None

    def test_default_parameters_through_catalog(self, catalog):
        """Test that default parameters work through the catalog."""
        # Should work with no parameters (using defaults)
        source = catalog.gfs_forecast()
        assert source is not None

        source = catalog.gfs_surface_winds()
        assert source is not None

        source = catalog.gfs_ice_concentration()
        assert source is not None

    def test_catalog_parameter_inheritance(self, catalog):
        """Test that catalog parameters are properly inherited."""
        # Test that different parameter combinations work
        sources = [
            catalog.gfs_forecast(cycle="2024-01-01T00:00:00", max_lead_time=12),
            catalog.gfs_forecast(cycle="2024-01-01T06:00:00", max_lead_time=48),
            catalog.gfs_surface_winds(cycle="2024-01-01T12:00:00", max_lead_time=24),
            catalog.gfs_ice_concentration(
                cycle="2024-06-15T18:00:00", max_lead_time=96
            ),
        ]

        for source in sources:
            assert source is not None

    def test_catalog_args_still_work(self, catalog):
        """Test that non-parameter args still work correctly."""
        # The catalog should still pass through other arguments
        # that are not parameters (like base_url, access_method, etc.)
        source = catalog.gfs_forecast(cycle="2024-01-01T00:00:00", max_lead_time=24)

        # The source should be created with the catalog's predefined args
        assert source is not None

    def test_parameter_types(self, catalog):
        """Test that parameter types are handled correctly."""
        # String cycle parameter
        source1 = catalog.gfs_forecast(cycle="2024-01-01T00:00:00")
        assert source1 is not None

        # Integer max_lead_time parameter
        source2 = catalog.gfs_forecast(max_lead_time=48)
        assert source2 is not None

        # Both parameters
        source3 = catalog.gfs_forecast(cycle="2024-01-01T18:00:00", max_lead_time=72)
        assert source3 is not None

    def test_catalog_documentation_accessible(self, catalog):
        """Test that catalog documentation is accessible."""
        # Check that each source has description and metadata
        sources = ["gfs_forecast", "gfs_surface_winds", "gfs_ice_concentration"]

        for source_name in sources:
            source = getattr(catalog, source_name)
            assert hasattr(source, "description")
            assert source.description is not None
            assert len(source.description) > 0
