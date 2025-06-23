import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

data = np.array([i + np.sin(i/5)*5 for i in range(100)]).reshape(-1, 1)
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

X, y = [], []
for i in range(len(data_scaled)-10):
    X.append(data_scaled[i:i+10])
    y.append(data_scaled[i+10])
X, y = np.array(X), np.array(y)

model = Sequential([
    LSTM(50, activation='relu', input_shape=(10,1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=20)
model.save("models/lstm_model.h5")
