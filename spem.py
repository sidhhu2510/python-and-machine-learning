import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# Assuming df is your DataFrame
df = pd.read_csv("D:\\python_task__\\files\\upi_2.csv")  # Replace "your_dataset.csv" with the actual file path

# Drop unnecessary columns
df = df.drop(['Name', 'UPI_number', 'IsFraud Report'], axis=1)

# Convert 'Pin Number' to numeric
df['Pin Number'] = pd.to_numeric(df['Pin Number'], errors='coerce')

# Prepare features (X) and target variable (y)
X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features (optional but often beneficial)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define classifiers
classifiers = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

# Train and evaluate each classifier
for name, classifier in classifiers.items():
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {accuracy}")

    # If you want to use cross-validation for a more robust evaluation
    # scores = cross_val_score(classifier, X, y, cv=5)
    # print(f"{name} Cross-Validation Accuracy: {scores.mean()}")

# Note: This is a basic example. You may need to tune hyperparameters and handle class imbalance for better results.
