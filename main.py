import pandas as pd
pancakes = pd.read_csv("candy.csv")

import matplotlib.pyplot as plt
import numpy as np

print(pancakes.idxmax())
print(pancakes)

x = np.asarray(pancakes.head(5)["competitorname"])
y = np.asarray(pancakes.head(5)["winpercent"])
plt.bar(x,y)
plt.savefig("candyy.png")