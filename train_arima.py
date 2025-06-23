
---

### `train_arima.py`
```python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

data = pd.Series([100 + i*5 + (i%5)*2 for i in range(50)])
model = ARIMA(data, order=(2,1,2))
model_fit = model.fit()
forecast = model_fit.forecast(steps=10)
print("Forecast:", forecast.tolist())
