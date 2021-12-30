import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv("iphone_price.csv")
model = LinearRegression()
model.fit(data[['version']],data[['price']])


plt.scatter(data['version'],data['price'])

plt.show()