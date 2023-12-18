import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("D:\\python_task__\\files\\upi_2.csv")


def UPI_Fraud_Detection(UPI_number):
    UPI_number_str = str(UPI_number)  # Convert UPI_number to string
    if UPI_number_str in data['UPI_number'].astype(str).values:
        # Convert 'Name' column to a binary indicator (1 if present, 0 otherwise)
        data["Name"] = data["Name"].apply(lambda x: 1 if UPI_number_str in str(x) else 0)

        # Map 'isFraud' column to binary labels
        data["isFraud"] = data["isFraud"].map({0: "NO Fraud", 1: "Fraud UPI Number"})

        # Prepare features (X) and target variable (y)
        x = np.array(data[["UPI_number"]])
        y = np.array(data["isFraud"])

        # Train-test split
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        # Create and fit the Decision Tree model
        # Define classifiers
        classifiers = {
            'Logistic Regression': LogisticRegression(),
            'Decision Tree': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier()
        }

        # Train and evaluate each classifier
        for name, classifier in classifiers.items():
            model=classifier.fit(x_train, y_train)
            # y_pred = classifier.predict(x_test)
            #
            # accuracy = accuracy_score(y_test, y_pred)
            # print(f"{name} Accuracy: {accuracy}")
            # # Evaluate accuracy on the test set (optional)
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"{name} Accuracy: {accuracy}")

        # Predict on new data
        features = np.array([[UPI_number]])
        prediction = model.predict(features)[0]

        print(f"Fraud Prediction for UPI Number {UPI_number}: {prediction}\n")



    else:
        print(f"{UPI_number} the UPI Number is invalid ")


# # Example usage
# UPI_number = 5662371908
# UPI_Fraud_Detection(UPI_number)
