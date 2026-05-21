import pandas as pd
pancakes = pd.read_csv("candy.csv")
import matplotlib.pyplot as plt
import numpy as np
#print(pancakes['winpercent'].idxmin())

cleats = pancakes.nlargest(5, 'winpercent')
print(pancakes.nlargest(5, 'winpercent'))

x = np.asarray(cleats["competitorname"])
y = np.asarray(cleats["winpercent"])
plt.figure(figsize = (10, 7))
plt.bar(x,y, color = ['#4AE8CB', '#FAC8A5', '#F7E9A3', '#FAA17A', '#A9F5D9'])
plt.title('top 5 most popular candies!')
plt.xlabel('names of candy')
plt.ylabel('percentage')
plt.tight_layout()
plt.legend(#maybe put stuff in here for the key)
plt.savefig("candyy.png")