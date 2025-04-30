import pandas as pd
data = pd.read_csv('new_textile.csv')

print(data.head())

#DATA PREPROCESSING
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# Load your data
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Check for null or NaN values
null_counts = data.isnull().sum()

# Display columns with null values
print("Columns with null values:")
print(null_counts[null_counts > 0])

# Check if any NaN values are present
nan_exists = data.isna().any().any()
if nan_exists:
    print("The dataset contains NaN values.")
else:
    print("The dataset does not contain any NaN values.")

# Optionally, display the percentage of null values in each column
null_percentage = data.isnull().mean() * 100
print("Percentage of null values in each column:")
print(null_percentage[null_percentage > 0])


data = pd.read_csv('new_textile.csv')
print(data.shape)
data.info()
data.isna().sum()
clean_data=data.fillna(data.mean())
clean_data.head()
import pandas as pd

# Load your data
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Check for null values and create a boolean DataFrame
null_bool_df = data.isnull()

# Display the boolean DataFrame indicating null values
print(null_bool_df)

# Count the null values for each column
null_counts = null_bool_df.sum()
print("\nColumns with null values:")
print(null_counts[null_counts > 0])

# Check if any NaN values are present
nan_exists = data.isna().any().any()
if nan_exists:
    print("The dataset contains NaN values.")
else:
    print("The dataset does not contain any NaN values.")

# Optionally, display the percentage of null values in each column
null_percentage = data.isnull().mean() * 100
print("Percentage of null values in each column:")
print(null_percentage[null_percentage > 0])

#Data Visualization with null values
def plot_hist_box(data, column):
    plt.figure(figsize=(14, 6))

    # Histogram
    plt.subplot(1, 2, 1)
    sns.histplot(data[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)

    plt.show()

# Function to create scatter plots for each column against 'QUALITYRATE'
def plot_scatter(data, column):
    if 'QUALITYRATE' in data.columns:
        plt.figure(figsize=(7, 6))
        sns.scatterplot(x=data[column], y=data['QUALITYRATE'])
        plt.title(f'Scatter plot of {column} vs QUALITYRATE')
        plt.xlabel(column)
        plt.ylabel('QUALITYRATE')
        plt.show()

# List of columns to analyze
columns = [
    'TOTAL_LENGTH', 'THEORY_LENGTH', 'WARPTOTAL', 'YA_RN_SPEC_DEN_IM', 'YARN_SPEC_FIBERBASE',
    'DEN_IM', 'FIBERBASE', 'UNITWEIGHT', 'GRANULARITY', 'WARPLENGTH', 'WARPSTRIP', 'SIZINGLENGTH',
    'WARPSPEED', 'WARPPRES', 'SSTENSION', 'WARPTENSION', 'HYDRATENSION', 'SIZINGSPEED', 'SIZINGBPRES',
    'SIZINGATENSION', 'SIZINGBTENSION', 'CONSISTENCY', 'DENSITY', 'BEAMSPEED', 'BEAMATENSION', 'BEAMBTENSION',
    'BEAMTENSION', 'WEAVEBTENSION', 'QUALITYRATE'
]

# Create plots for each column
for column in columns:
    if column in data.columns:
        print(f"Analyzing column: {column}")
        plot_hist_box(data, column)
        plot_scatter(data, column)
    else:
        print(f"Column {column} not found in the dataset.")


import pandas as pd

# Load your data
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Display initial null values count
null_counts = data.isnull().sum()
print("Columns with null values before filling:")
print(null_counts[null_counts > 0])

# Fill missing values with the mean of each column
data.fillna(data.mean(), inplace=True)

# Check if any NaN values are present after filling
null_counts_after = data.isnull().sum()
print("\nColumns with null values after filling:")
print(null_counts_after[null_counts_after > 0])

# Check if any NaN values are present
nan_exists = data.isna().any().any()
if nan_exists:
    print("The dataset still contains NaN values.")
else:
    print("The dataset does not contain any NaN values after filling.")

# Optional: Display the first few rows of the modified dataset
print("\nSample of the modified dataset:")
print(data.head())

#Data Visualization without null values
def plot_hist_box(data, column):
    plt.figure(figsize=(14, 6))

    # Histogram
    plt.subplot(1, 2, 1)
    sns.histplot(data[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)

    plt.show()

# Function to create scatter plots for each column against 'QUALITYRATE'
def plot_scatter(data, column):
    if 'QUALITYRATE' in clean_data.columns:
        plt.figure(figsize=(7, 6))
        sns.scatterplot(x=data[column], y=data['QUALITYRATE'])
        plt.title(f'Scatter plot of {column} vs QUALITYRATE')
        plt.xlabel(column)
        plt.ylabel('QUALITYRATE')
        plt.show()

# List of columns to analyze
columns = [
    'TOTAL_LENGTH', 'THEORY_LENGTH', 'WARPTOTAL', 'YA_RN_SPEC_DEN_IM', 'YARN_SPEC_FIBERBASE',
    'DEN_IM', 'FIBERBASE', 'UNITWEIGHT', 'GRANULARITY', 'WARPLENGTH', 'WARPSTRIP', 'SIZINGLENGTH',
    'WARPSPEED', 'WARPPRES', 'SSTENSION', 'WARPTENSION', 'HYDRATENSION', 'SIZINGSPEED', 'SIZINGBPRES',
    'SIZINGATENSION', 'SIZINGBTENSION', 'CONSISTENCY', 'DENSITY', 'BEAMSPEED', 'BEAMATENSION', 'BEAMBTENSION',
    'BEAMTENSION', 'WEAVEBTENSION', 'QUALITYRATE'
]

# Create plots for each column
for column in columns:
    if column in clean_data.columns:
        print(f"Analyzing column: {column}")
        plot_hist_box(clean_data, column)
        plot_scatter(clean_data, column)
    else:
        print(f"Column {column} not found in the dataset.")

#*Spliting the Data *
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load your dataset


# Prepare X and y
# (replace 'target_column' with your actual target column name)


# Train the model
model = GradientBoostingClassifier()


# Save the model
#joblib.dump(model, 'ML/gradient_boosting_model.pkl')

#print("✅ Model trained and saved successfully!")

# Assuming 'QUALITYRATE' is the name of the target variable column in your dataset
X = clean_data.drop('QUALITYRATE', axis=1)  # Features
y = clean_data['QUALITYRATE']               # Target variable
#model.fit(X, y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
print("\nShapes of the resulting datasets:")
print(f"X_train: {X_train.shape}")
print(f"X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test: {y_test.shape}")

# Optionally, you can print the first few rows of X_train and y_train to inspect the data
print("\nFirst few rows of X_train:")
print(X_train.head())

print("\nFirst few values of y_train:")
print(y_train.head())

#Train the Model with XGBoost and Random Forest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import matplotlib.pyplot as plt
import numpy as np
import joblib

# Load your trained model from the file
#model = joblib.load('ML/gradient_boosting_model.pkl')

# Feature names (based on your input data)
feature_names = [
    'TOTAL_LENGTH', 'THEORY_LENGTH', 'WARPTOTAL', 'YA_RN_SPEC_DEN_IM',
    'YARN_SPEC_FIBERBASE', 'DEN_IM', 'FIBERBASE', 'UNITWEIGHT', 'GRANULARITY',
    'WARPLENGTH', 'WARPSTRIP', 'SIZINGLENGTH', 'WARPSPEED', 'WARPPRES',
    'SSTENSION', 'WARPTENSION', 'HYDRATENSION', 'SIZINGSPEED', 'SIZINGBPRES',
    'SIZINGATENSION', 'SIZINGBTENSION', 'CONSISTENCY', 'DENSITY', 'BEAMSPEED',
    'BEAMATENSION', 'BEAMBTENSION', 'BEAMTENSION', 'WEAVEBTENSION'
]

# Get feature importances from the model
#importances = model.feature_importances_

# Plot feature importances
"""indices = np.argsort(importances)[::-1]
plt.figure(figsize=(12, 6))
plt.title('Feature Importance')
plt.bar(range(len(importances)), importances[indices], align='center')
plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
plt.tight_layout()
plt.show()"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset into a pandas DataFrame
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Discretize the target variable 'QUALITYRATE' into categories
data['QUALITYRATE_CAT'] = pd.qcut(data['QUALITYRATE'], q=3, labels=False)  # Example with 3 bins

# Encode the target variable if not already integer labels
le = LabelEncoder()
y = le.fit_transform(data['QUALITYRATE_CAT'])

# Separate features (X) and encoded target (y)
X = data.drop(columns=['QUALITYRATE', 'QUALITYRATE_CAT'])

# Impute missing values in X
imputer = SimpleImputer(strategy='mean')  # You can use 'median'/'most_frequent' if preferred
X_imputed = imputer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3, random_state=42)

# Initialize and train the GradientBoostingClassifier model
print("Training GradientBoostingClassifier...")
gb_model = GradientBoostingClassifier()
gb_model.fit(X_train, y_train)

# Predictions and evaluation on test set
y_pred = gb_model.predict(X_test)

# Compute accuracy and other metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
rocauc = roc_auc_score(y_test, gb_model.predict_proba(X_test), multi_class='ovr')

print(f"GradientBoostingClassifier Performance:")
print(f"- Accuracy: {accuracy:.4f}")
print(f"- F1 score: {f1:.4f}")
print(f"- Precision: {precision:.4f}")
print(f"- Recall: {recall:.4f}")
print(f"- ROC AUC score: {rocauc:.4f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the dataset into a pandas DataFrame
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Discretize the target variable 'QUALITYRATE' into categories
data['QUALITYRATE_CAT'] = pd.qcut(data['QUALITYRATE'], q=3, labels=False)  # Example with 3 bins

# Encode the target variable if not already integer labels
le = LabelEncoder()
y = le.fit_transform(data['QUALITYRATE_CAT'])

# Separate features (X) and encoded target (y)
X = data.drop(columns=['QUALITYRATE', 'QUALITYRATE_CAT'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the XGBoost model
xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
xgb_model.fit(X_train, y_train)

# Make predictions
y_pred = xgb_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load your data


# Convert the target column to categorical if it's not already
data['QUALITYRATE_CAT'] = pd.qcut(data['QUALITYRATE'], q=3, labels=False)

# Separate features and target
X = data.drop('QUALITYRATE', axis=1)
y = data['QUALITYRATE']

# Encode the target variable if it's not already integers
if y.dtype == 'float' or y.dtype == 'object':
    le = LabelEncoder()
    y = le.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset into a pandas DataFrame
data_path = 'new_textile.csv'  # Replace with your file path
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Discretize the target variable 'QUALITYRATE' into categories
data['QUALITYRATE_CAT'] = pd.qcut(data['QUALITYRATE'], q=3, labels=False)  # Example with 3 bins

# Encode the target variable if not already integer labels
le = LabelEncoder()
y = le.fit_transform(data['QUALITYRATE_CAT'])

# Separate features (X) and encoded target (y)
X = data.drop(columns=['QUALITYRATE', 'QUALITYRATE_CAT'])

# Impute missing values in X
imputer = SimpleImputer(strategy='mean')  # You can use 'median'/'most_frequent' if preferred
X_imputed = imputer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3, random_state=42)

# Initialize and train the GradientBoostingClassifier model
print("Training GradientBoostingClassifier...")
gb_model = GradientBoostingClassifier()
gb_model.fit(X_train, y_train)

# Predictions and evaluation on test set
y_pred = gb_model.predict(X_test)

# Compute accuracy and other metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
rocauc = roc_auc_score(y_test, gb_model.predict_proba(X_test), multi_class='ovr')

print(f"GradientBoostingClassifier Performance:")
print(f"- Accuracy: {accuracy:.4f}")
print(f"- F1 score: {f1:.4f}")
print(f"- Precision: {precision:.4f}")
print(f"- Recall: {recall:.4f}")
print(f"- ROC AUC score: {rocauc:.4f}")

# Save the GradientBoostingClassifier model
joblib.dump(gb_model, 'gradient_boosting_model.pkl')
print("GradientBoostingClassifier model saved successfully.")


import pickle
from sklearn.ensemble import GradientBoostingClassifier
# Train your model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save the model
with open('gradient_boosting_model.pkl', 'wb') as f:
    pickle.dump(model, f)