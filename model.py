
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# =============================
# LOAD DATA
# =============================
df = pd.read_csv("cleaned_airbnb_data.csv")

# =============================
# REMOVE OUTLIERS (VERY IMPORTANT)
# =============================
df = df[df['price'] < 1000]

# =============================
# SPLIT FEATURES & TARGET
# =============================
X = df.drop('price', axis=1)

# LOG TRANSFORM TARGET
y = np.log1p(df['price'])

# =============================
# TRAIN TEST SPLIT
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =============================
# TRAIN XGBOOST MODEL
# =============================
model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.03,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

# =============================
# PREDICTIONS
# =============================
y_pred_log = model.predict(X_test)

# CONVERT BACK TO ORIGINAL SCALE
y_pred = np.expm1(y_pred_log)
y_test_actual = np.expm1(y_test)

# =============================
# EVALUATION
# =============================
mae = mean_absolute_error(y_test_actual, y_pred)
rmse = np.sqrt(mean_squared_error(y_test_actual, y_pred))
r2 = r2_score(y_test_actual, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# =============================
# FEATURE IMPORTANCE
# =============================
importance = model.feature_importances_
features = X.columns

indices = importance.argsort()[::-1]

plt.figure(figsize=(10,6))
plt.bar(range(len(features)), importance[indices])
plt.xticks(range(len(features)), features[indices], rotation=90)
plt.title("Feature Importance")
plt.tight_layout()
plt.show()

import joblib

joblib.dump(model, "price_model.pkl")
print("Model saved successfully!")
