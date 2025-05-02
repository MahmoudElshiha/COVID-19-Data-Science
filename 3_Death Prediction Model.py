import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv('./Datasets/cleaned_covid_dataset.csv')

# Feature selection - using all relevant medical features
features = [
    'Treatment_Level', 'Medical_Unit_Type', 'Sex', 'Patient_Care_Type',
    'Pneumonia', 'Age', 'Diabetes', 'COPD', 'Asthma', 'Immunosuppressed',
    'Hypertension', 'Other_Disease', 'Cardiovascular_Disease', 'Obesity',
    'Chronic_Renal_Disease', 'Tobacco_Use', 'is_infected'
]

# Target variable
target = 'is_dead'

# Split data into features and target
X = data[features]
y = data[target]

# Convert Medical_Unit_Type to categorical (one-hot encoding)
X = pd.get_dummies(X, columns=['Medical_Unit_Type'], prefix='unit')

# Split into train and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Handle class imbalance (using class weights)
class_counts = y_train.value_counts()
total = class_counts.sum()
weight_for_0 = (1 / class_counts[0]) * (total / 2.0)
weight_for_1 = (1 / class_counts[1]) * (total / 2.0)
class_weight = {0: weight_for_0, 1: weight_for_1}

# Build the neural network model
def create_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=[
            'accuracy',
            tf.keras.metrics.Precision(name='precision'),
            tf.keras.metrics.Recall(name='recall'),
            tf.keras.metrics.AUC(name='auc')
        ]
    )
    return model

# Create and train model
input_shape = X_train.shape[1]
model = create_model(input_shape)

# Early stopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_auc',
    patience=5,
    restore_best_weights=True
)

# Train the model
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=30,
    batch_size=256,
    class_weight=class_weight,
    callbacks=[early_stopping],
    verbose=1
)

# Evaluate on test set
results = model.evaluate(X_test, y_test, verbose=0)
print("\nTest Evaluation:")
print(f"Loss: {results[0]:.4f}")
print(f"Accuracy: {results[1]:.4f}")
print(f"Precision: {results[2]:.4f}")
print(f"Recall: {results[3]:.4f}")
print(f"AUC: {results[4]:.4f}")

# Generate predictions
y_pred = model.predict(X_test)
y_pred_class = (y_pred > 0.5).astype(int)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_class))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_class)
print("\nConfusion Matrix:")
print(cm)

# Plot training history
def plot_history(history):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Accuracy over Epochs')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['auc'], label='Train AUC')
    plt.plot(history.history['val_auc'], label='Validation AUC')
    plt.title('AUC over Epochs')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

plot_history(history)

# Save the model
model.save('./Model/covid_mortality_predictor.h5')
print("\nModel saved at './Model/covid_mortality_predictor.h5'")