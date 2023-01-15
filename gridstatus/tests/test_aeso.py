import pytest

from gridstatus import NotSupported
from gridstatus.aeso import AESO
from gridstatus.tests.base_test_iso import BaseTestISO


class TestAESO(BaseTestISO):
    iso = AESO()

    """get_fuel_mix"""

    def test_get_fuel_mix_date_or_start(self):
        with pytest.raises(NotSupported):
            super().test_get_fuel_mix_date_or_start()

    def test_get_fuel_mix_historical(self):
        with pytest.raises(NotSupported):
            super().test_get_fuel_mix_historical()

    def test_get_fuel_mix_historical_with_date_range(self):
        with pytest.raises(NotSupported):
            super().test_get_fuel_mix_historical_with_date_range()

    def test_get_fuel_mix_today(self):
        with pytest.raises(NotSupported):
            super().test_get_fuel_mix_today()

    def test_get_interconnection_queue(self):
        with pytest.raises(NotSupported):
            super().test_get_interconnection_queue()