import pandas as pd
import matplotlib.pyplot as plt


dataSet = pd.read_csv("dataset.csv")

print(dataSet)

print(dataSet.isna().sum())
print(dataSet.duplicated())

x = dataSet["Student_Average"]
y = dataSet["Higest_Average"]

plt.scatter(x,y)
plt.show()  