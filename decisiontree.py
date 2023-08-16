from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import pandas as pd

class DecisionTree:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def preprocess_data(self, X):
        # Preprocess the features (e.g., encoding categorical variables)
        # Remove columns with all NaN values
        X = X.dropna(axis=1, how='all')
        X = pd.get_dummies(X, drop_first=True)
        return X

    def train_model(self, X, y):

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Decision Tree model
        self.model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = self.model.predict(X_test)

        # Calculate accuracy, precision, recall, and confusion matrix
        return accuracy_score(y_test, y_pred), precision_score(y_test, y_pred), recall_score(y_test, y_pred), confusion_matrix(y_test, y_pred)

    def predict(self, new_data):
        # Preprocess the new data in the same way as the training data
        new_data = self.preprocess_data(new_data)

        # Predict the likelihood for new data
        return self.model.predict_proba(new_data)
