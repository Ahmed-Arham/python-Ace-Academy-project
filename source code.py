import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a synthetic dataset similar to the sample
data = {
    "ORDERNUM": range(10100, 10150),
    "QUANTITY": [30, 41, 45, 36, 29, 48, 22, 14, 21, 31] * 5,
    "PRICEEACH": [95.7, 81.35, 83.26, 96.66, 86.13, 98.57, 92.83, 100, 94.74, 76.36] * 5,
    "SALES": [2871, 2976.95, 3746.7, 3479.76, 2497.77, 2168.54, 4708.44, 3188.64, 3676.76, 2434.56] * 5,
    "ORDERDATE": pd.date_range(start="1/1/2003", periods=50, freq='M').strftime("%m/%d/%Y"),
    "STATUS": ["Shipped"] * 50,
    "PRODUCTLINE": ["Motorcycle"] * 50,
    "COUNTRY": ["USA", "France", "USA", "Canada", "Germany"] * 10
}

df = pd.DataFrame(data)

# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Perform summary statistics
summary = df.describe()

# Sales trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(x="ORDERDATE", y="SALES", data=df, marker="o")
plt.title("Sales Trends Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Top-Selling Products
plt.figure(figsize=(8, 4))
sns.barplot(x="PRODUCTLINE", y="SALES", data=df, estimator=sum)
plt.title("Top-Selling Product Lines")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.show()

# Sales by Country
plt.figure(figsize=(10, 5))
sns.boxplot(x="COUNTRY", y="SALES", data=df)
plt.title("Sales Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.show()

# Print summary statistics
print(summary)
