import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform forward feature selection
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set()

for i in range(n_features):
    best_score = 0
    best_feature = None
    
    for feature in X.columns:
        if feature not in selected_features:
            selected_features.add(feature)
            X_selected = X[list(selected_features)]
            scores, _ = f_regression(X_selected, y)
            score = scores.mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
                
            selected_features.remove(feature)
            
    selected_features.add(best_feature)

print('Selected features 1st Tech :', list(selected_features))

############################################################################
'''
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation matrix
corr = housing.corr()

# Plot the correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Perform feature selection based on correlation
threshold = 0.5
corr_features = set()
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            corr_features.add(corr.columns[i])

print('Selected features:', list(corr_features))

# Create a new dataframe with the selected features
selected_features_df = housing[list(corr_features)]

# Display the new dataframe
print('\nNew dataframe with selected features:')
print(selected_features_df.head())
'''
############################################################################

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Apply ANOVA feature selection
k = 5  # number of top features to select
selector = SelectKBest(f_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features 2nd Tech:', list(selected_features))

###########################################################################

import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# Load the dataset into a Pandas dataframe
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
df = pd.read_csv(url, delim_whitespace=True, header=None)

# Extract the features (columns 0-12) and the target variable (column 13)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Perform feature selection using RFE
estimator = LinearRegression()
selector = RFE(estimator, n_features_to_select=5, step=1)
selector = selector.fit(X, y)

# Print the ranking of features and their names
print('Ranking of features:')
for i in range(len(selector.ranking_)):
    if selector.ranking_[i] == 1:
        print(df.columns[i], '(rank:', selector.ranking_[i], ')')

# Train a linear regression model on the selected features
X_selected = selector.transform(X)
regressor = LinearRegression()
regressor.fit(X_selected, y)

# Print the coefficients of the model
print('Coefficients:', regressor.coef_)
