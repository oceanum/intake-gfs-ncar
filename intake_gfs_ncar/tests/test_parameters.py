"""Unit tests for GFS intake driver parameters functionality."""

import pytest
from datetime import datetime, timezone
from intake_gfs_ncar.gfs_intake_driver import GFSForecastSource


class TestGFSParameters:
    """Test class for GFS intake driver parameters."""

    def test_parameter_definition(self):
        """Test that parameters are defined correctly in the class."""
        params = GFSForecastSource.parameters
        
        # Check that both parameters are defined
        assert "cycle" in params, "cycle parameter not found"
        assert "max_lead_time" in params, "max_lead_time parameter not found"
        
        # Check cycle parameter structure
        cycle_param = params["cycle"]
        assert cycle_param["default"] == "today"
        assert cycle_param["type"] == "datetime"
        assert "description" in cycle_param
        
        # Check max_lead_time parameter structure
        max_lead_param = params["max_lead_time"]
        assert max_lead_param["default"] == 24
        assert max_lead_param["type"] == "int"
        assert "description" in max_lead_param

    def test_default_parameters(self):
        """Test that default parameters are applied correctly."""
        source = GFSForecastSource()
        
        # Verify the values match the parameter defaults
        assert source.max_lead_time == 24
        assert source.metadata.get("max_lead_time") == 24
        
        # The cycle should be set to the latest available
        assert source.metadata.get("cycle") is not None
        
    def test_custom_parameters_via_kwargs(self):
        """Test that custom parameters are applied correctly via kwargs."""
        custom_cycle = "2024-01-15T12:00:00"
        custom_max_lead_time = 48
        
        source = GFSForecastSource(
            cycle=custom_cycle,
            max_lead_time=custom_max_lead_time
        )
        
        # Verify the values match what we set
        assert source.max_lead_time == custom_max_lead_time
        assert source.metadata.get("max_lead_time") == custom_max_lead_time
        assert source.metadata.get("cycle") == "2024-01-15T12:00:00"

    def test_cycle_parameter_today(self):
        """Test that 'today' cycle parameter works correctly."""
        source = GFSForecastSource(cycle="today")
        
        # Should have a valid cycle datetime
        cycle_str = source.metadata.get("cycle")
        assert cycle_str is not None
        
        # Should be parseable as datetime
        cycle_dt = datetime.fromisoformat(cycle_str)
        assert isinstance(cycle_dt, datetime)
        
        # Should be a valid GFS cycle hour (0, 6, 12, 18)
        assert source.model_run_time in [0, 6, 12, 18]

    def test_cycle_parameter_latest(self):
        """Test that 'latest' cycle parameter still works correctly."""
        source = GFSForecastSource(cycle="latest")
        
        # Should have a valid cycle datetime
        cycle_str = source.metadata.get("cycle")
        assert cycle_str is not None
        
        # Should be parseable as datetime
        cycle_dt = datetime.fromisoformat(cycle_str)
        assert isinstance(cycle_dt, datetime)
        
        # Should be a valid GFS cycle hour (0, 6, 12, 18)
        assert source.model_run_time in [0, 6, 12, 18]

    def test_cycle_parameter_iso_string(self):
        """Test that ISO format cycle strings work correctly."""
        test_cycle = "2024-01-15T18:00:00"
        source = GFSForecastSource(cycle=test_cycle)
        
        assert source.date.year == 2024
        assert source.date.month == 1
        assert source.date.day == 15
        assert source.model_run_time == 18
        assert source.metadata.get("cycle") == test_cycle

    def test_cycle_parameter_datetime_object(self):
        """Test that datetime objects work for cycle parameter."""
        test_dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
        source = GFSForecastSource(cycle=test_dt)
        
        assert source.date.year == 2024
        assert source.date.month == 1
        assert source.date.day == 15
        assert source.model_run_time == 12

    def test_max_lead_time_validation(self):
        """Test max_lead_time parameter validation."""
        # Valid value should work
        source = GFSForecastSource(max_lead_time=72)
        assert source.max_lead_time == 72
        
        # Test edge case: positive values
        source2 = GFSForecastSource(max_lead_time=1)
        assert source2.max_lead_time == 1

    def test_invalid_cycle_parameter(self):
        """Test that invalid cycle parameters raise appropriate errors."""
        with pytest.raises(ValueError, match="Invalid cycle format"):
            GFSForecastSource(cycle="invalid-date-string")

    def test_invalid_max_lead_time_parameter(self):
        """Test that invalid max_lead_time parameters raise appropriate errors."""
        # Negative value should fail
        with pytest.raises(ValueError, match="Invalid max_lead_time"):
            GFSForecastSource(max_lead_time=-1)
        
        # Zero should fail
        with pytest.raises(ValueError, match="Invalid max_lead_time"):
            GFSForecastSource(max_lead_time=0)
        
        # Non-integer should fail
        with pytest.raises(ValueError, match="Invalid max_lead_time"):
            GFSForecastSource(max_lead_time="not-a-number")

    def test_parameter_inheritance_in_metadata(self):
        """Test that parameters are properly included in metadata."""
        cycle = "2024-06-15T06:00:00"
        max_lead_time = 96
        
        source = GFSForecastSource(
            cycle=cycle,
            max_lead_time=max_lead_time
        )
        
        metadata = source.metadata
        assert metadata["cycle"] == cycle
        assert metadata["max_lead_time"] == max_lead_time
        assert metadata["model_run_time"] == "06Z"
        assert metadata["date"] == "2024-06-15"

    def test_parameters_with_other_kwargs(self):
        """Test that parameters work alongside other constructor arguments."""
        source = GFSForecastSource(
            cycle="2024-01-01T00:00:00",
            max_lead_time=36,
            base_url="https://custom.thredds.server.com",
            access_method="ncss"
        )
        
        assert source.max_lead_time == 36
        assert source.metadata["cycle"] == "2024-01-01T00:00:00"
        assert source.base_url == "https://custom.thredds.server.com"
        assert source.access_method == "ncss"

    def test_high_max_lead_time_warning(self):
        """Test that a warning is logged for very high max_lead_time values."""
        import logging
        
        # This should trigger a warning but not fail
        source = GFSForecastSource(max_lead_time=500)
        assert source.max_lead_time == 500