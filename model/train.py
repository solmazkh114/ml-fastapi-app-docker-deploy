import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# 1. Load dataset
df = pd.read_csv("../data/data.csv")

# 2. Features and target
X = df[["size", "zone"]]
y = df["price"]

# 3. Preprocessing (one-hot encode categorical 'zone')
preprocessor = ColumnTransformer(
    transformers=[
        ("zone", OneHotEncoder(handle_unknown="ignore"), ["zone"])
    ],
    remainder="passthrough"  # keep "size"
)

# 4. Model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Fit model
model.fit(X_train, y_train)

# 7. Save trained model
joblib.dump(model, "./model.joblib")

print("✅ Model trained and saved to model/model.joblib")
print("Test R^2 score:", model.score(X_test, y_test))
