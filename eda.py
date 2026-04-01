## EDA
import pandas as pd
df = pd.read_csv('new_york_listings_2024.csv')
import matplotlib.pyplot as plt

#plt.scatter(df['number_of_reviews'], df['price'])
#plt.xlabel("Number of Reviews")
#plt.ylabel("Price")
#plt.title("Reviews vs Price")
#plt.show()
## Scatter plot of reviews per month vs price
#plt.scatter(df['reviews_per_month'], df['price'])
#plt.xlabel("Reviews per Month")
#plt.ylabel("Price")
#plt.show()

#df.boxplot(column='price', by='room_type')
#plt.xticks(rotation=45)
#plt.show()


## Correlation matrix
print(df.corr(numeric_only=True)['price'].sort_values(ascending=False))

df['demand'] = df['number_of_reviews'] * df['reviews_per_month']

print(df.groupby(pd.qcut(df['demand'], 4))['price'].mean())
print(df.groupby(pd.qcut(df['availability_365'], 4))['price'].mean())