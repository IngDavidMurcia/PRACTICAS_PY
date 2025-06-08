from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=10000)
# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
# Evaluate the model
print("presicion:",accuracy_score(y_test, y_pred))
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
# Save the model using joblib
import joblib
joblib.dump(model, 'logistic_regression_model.pkl')
# Load the model
loaded_model = joblib.load('logistic_regression_model.pkl')
# Make predictions with the loaded model
loaded_y_pred = loaded_model.predict(X_test)
# Evaluate the loaded model
print("Precisión del modelo cargado:", accuracy_score(y_test, loaded_y_pred))
# Ensure the loaded model gives the same predictions
assert (y_pred == loaded_y_pred).all(), "Predictions do not match after loading the model"
# Print a message indicating successful completion
print("Modelo de regresión logística entrenado y guardado exitosamente.")
# Ensure the model is trained and saved correctly
# Print the model coefficients
print("Coeficientes del modelo:", model.coef_)
# Print the intercept of the model
print("Intercepto del modelo:", model.intercept_)
# Print the shape of the training and testing sets
print("Forma de los datos de entrenamiento:", X_train.shape)
print("Forma de los datos de prueba:", X_test.shape)
# Print the number of features
print("Número de características:", X.shape[1])
# Print the number of samples
print("Número de muestras:", X.shape[0])
# Print the class labels
print("Etiquetas de clase:", data.target_names)
# Print the feature names
print("Nombres de características:", data.feature_names)
# Print the first 5 predictions
print("Primeras 5 predicciones:", y_pred[:5])
# Print the first 5 true labels
print("Primeras 5 etiquetas verdaderas:", y_test[:5])
# Print the model's score on the test set
print("Puntuación del modelo en el conjunto de prueba:", model.score(X_test, y_test))
# Print the confusion matrix
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:\n", conf_matrix)
# Print the ROC AUC score
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
print("ROC AUC score:", roc_auc)
# Print the ROC curve
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], 'k--', label='Random guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
# Print the precision-recall curve
from sklearn.metrics import precision_recall_curve
precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(X_test)[:, 1])
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower left')
plt.show()
# Print the learning curve
from sklearn.model_selection import learning_curve
train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, n_jobs=-1)
train_scores_mean = train_scores.mean(axis=1)
test_scores_mean = test_scores.mean(axis=1)
plt.figure(figsize=(8, 6))
plt.plot(train_sizes, train_scores_mean, label='Training score')
plt.plot(train_sizes, test_scores_mean, label='Cross-validation score')
plt.xlabel('Training Size')
plt.ylabel('Score')
plt.title('Learning Curve')
plt.legend(loc='best')
plt.show()
# Print the feature importance
import numpy as np
feature_importance = np.abs(model.coef_[0])
feature_names = data.feature_names
sorted_indices = np.argsort(feature_importance)[::-1]
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_names)), feature_importance[sorted_indices], align='center')
plt.xticks(range(len(feature_names)), feature_names[sorted_indices], rotation=90)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
# Print the model's coefficients
print("Coeficientes del modelo:", model.coef_)
# Print the model's intercept
print("Intercepto del modelo:", model.intercept_)
# Print the model's score on the training set
print("Puntuación del modelo en el conjunto de entrenamiento:", model.score(X_train, y_train))
# Print the model's score on the test set
print("Puntuación del modelo en el conjunto de prueba:", model.score(X_test, y_test))
# Print the number of iterations taken to converge  
print("Número de iteraciones para converger:", model.n_iter_)
# Print the model's parameters
print("Parámetros del modelo:", model.get_params())
# Print the model's class weights
print("Pesos de las clases:", model.class_weight)
# Print the model's regularization strength
print("Fuerza de regularización:", model.C)
# Print the model's solver
print("Solver del modelo:", model.solver)
# Print the model's duality gap
print("Dualidad del modelo:", model.dual_gap_)
# Print the model's tolerance
print("Tolerancia del modelo:", model.tol)
# Print the model's number of classes
print("Número de clases:", model.n_classes_)
# Print the model's number of features
