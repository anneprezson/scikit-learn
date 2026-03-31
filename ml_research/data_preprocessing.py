from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
scaler = StandardScaler()
print(scaler.fit(data).transform(data))

# ML research on data scaling and normalization