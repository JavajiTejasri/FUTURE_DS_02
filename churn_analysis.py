import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("churn_data.csv")

# Show first rows
print(df.head())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove missing values
df = df.dropna()

# =========================
# 1. Churn Distribution
# =========================
df['Churn'].value_counts().plot(kind='bar', title='Churn Distribution')
plt.savefig("churn_distribution.png")
plt.show()

# =========================
# 2. Churn by Gender
# =========================
pd.crosstab(df['gender'], df['Churn']).plot(kind='bar', title='Churn by Gender')
plt.savefig("churn_by_gender.png")
plt.show()

# =========================
# 3. Monthly Charges vs Churn
# =========================
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges vs Churn")
plt.savefig("monthly_charges_vs_churn.png")
plt.show()