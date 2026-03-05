import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("prix_maisons.csv")

print(data.head())
print(data.dtypes)
print(len(data))


# A2

x = data["surface"].values
y = data["prix"].values

mean_x = np.mean(x)
std_x = np.std(x)

mean_y = np.mean(y)
std_y = np.std(y)

x = (x - mean_x) / std_x
y = (y - mean_y) / std_y


plt.scatter(x, y)
plt.xlabel("surface")
plt.ylabel("prix")
plt.title("Surface vs Prix")
plt.show()