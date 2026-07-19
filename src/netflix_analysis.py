# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic overview
print(df.head())
print(df.info())
print(df.describe())

# -----------------------
# DATA CLEANING
# -----------------------

# Convert date
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Fill missing values
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

# -----------------------
# ANALYSIS
# -----------------------

import matplotlib.pyplot as plt

# 1. Movies vs TV Shows
df['type'].value_counts().plot(kind='bar', title="Movies vs TV Shows")
plt.show()

# 2. Top countries
df['country'].value_counts().head(10).plot(kind='bar', title="Top 10 Countries")
plt.xticks(rotation=45)
plt.show()

# 3. Content over time
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(title="Content Over Years")
plt.show()

# 4. Ratings
df['rating'].value_counts().plot(kind='bar', title="Ratings Distribution")
plt.xticks(rotation=45)
plt.show()

# -----------------------
# INSIGHTS (PRINT)
# -----------------------

print("Most content type:", df['type'].mode()[0])
print("Top country:", df['country'].mode()[0])
print("Most common rating:", df['rating'].mode()[0])
