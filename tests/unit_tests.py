import json
from middleware.forecast_to_tf import generate_tf_from_forecast
from tempfile import TemporaryDirectory
import os

def test_generate_tf():
    forecast = {"2025-07-01T00:00": 2, "2025-07-01T01:00": 3}
    with TemporaryDirectory() as tmpdir:
        forecast_path = os.path.join(tmpdir, "forecast.json")
        with open(forecast_path, "w") as f:
            json.dump(forecast, f)
        generate_tf_from_forecast(forecast_path, tmpdir)
        assert os.path.exists(os.path.join(tmpdir, "autoscaling.tf"))
