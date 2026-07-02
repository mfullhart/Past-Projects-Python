"""
Course Project

mfullhart20@georgefox.edu
"""

# Import
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets
import sklearn.model_selection
import sklearn.svm

# Load the dataset
data = pd.read_csv("banana_quality.csv")

# Separate features (X) and target (y)
X = data.drop(columns=['Quality'])
y = data['Quality']

# Dictionary to convert target labels to colors
class_colors = {'Good': 'green', 'Bad': 'red'}
colors = [class_colors[label] for label in y]

# Scatter plot of Size vs Sweetness
plt.scatter(X['Size'], X['Weight'], c=colors)
plt.xlabel('Size')
plt.ylabel('Weight')
plt.title('Size vs Weight')
plt.show()

# Scatter plot of Weight vs Softness
plt.scatter(X['Sweetness'], X['Softness'], c=colors)
plt.xlabel('Sweetness')
plt.ylabel('Softness')
plt.title('Sweetness vs Softness')
plt.show()

# Scatter plot of Harvest Time vs Ripeness
plt.scatter(X['HarvestTime'], X['Ripeness'], c=colors)
plt.xlabel('Harvest Time')
plt.ylabel('Ripeness')
plt.title('Harvest Time vs Ripeness')
plt.show()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = (
    sklearn.model_selection.train_test_split(X, y, test_size=0.1, random_state=42, stratify=y))

# Initialize SVM classifier
model = sklearn.svm.SVC()

# Train the model
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy: .3f}')

# Classification report
report = sklearn.metrics.classification_report(y_test, y_pred)
print(f'Classification Report: \n{report}')

# Confusion matrix
cm = sklearn.metrics.confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix: \n{cm}')

# Plot a confusion matrix
sklearn.metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred, cmap='Blues')
plt.show()
