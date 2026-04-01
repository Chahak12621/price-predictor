
import pandas as pd

# =============================
# LOAD DATA
# =============================
df = pd.read_csv('new_york_listings_2024.csv')

print("Initial Shape:", df.shape)

# =============================
# DROP USELESS COLUMNS
# =============================
df = df.drop(columns=[
    'id',
    'host_id',
    'name',
    'host_name',
    'license',
    'last_review',
    'neighbourhood'
])

# =============================
# CLEAN NUMERIC-LIKE COLUMNS
# =============================

# Clean baths (handles "1 bath", "2 baths", "Not specified")
df['baths'] = df['baths'].astype(str).str.extract('(\d+)')
df['baths'] = pd.to_numeric(df['baths'], errors='coerce')

# Bedrooms
df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce')

# Rating
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# =============================
# HANDLE MISSING VALUES
# =============================
df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())
df['baths'] = df['baths'].fillna(df['baths'].median())
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

# =============================
# ENCODING CATEGORICAL VARIABLES
# =============================
df = pd.get_dummies(df, columns=['room_type', 'neighbourhood_group'], drop_first=True)

# Convert boolean columns to integers (0/1)
bool_cols = df.select_dtypes(include='bool').columns
df[bool_cols] = df[bool_cols].astype(int)

# =============================
# FINAL CHECK
# =============================
print("\nFinal Data Types:\n", df.dtypes)
print("\nFinal Shape:", df.shape)
print("\nAny Null Values:\n", df.isnull().sum())

# =============================
# SAVE CLEANED DATA
# =============================
df.to_csv("cleaned_airbnb_data.csv", index=False)

print("\n Cleaned data saved as 'cleaned_airbnb_data.csv'")
