import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

# Load the dataset 
housing = pd.read_csv("housing.csv")
# Income_cat for split data

housing["income_cat"] = pd.cut(housing["median_income"],bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels = [1,2,3,4,5])


## Split the data 
split  = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index , test_index in split.split(housing,housing["income_cat"]):
    train_data = housing.loc[train_index]
    test_data = housing.loc[test_index]


# Drop the income_cat column
for sett in train_data,test_data :
    sett.drop(columns = "income_cat",inplace=True)  

# Copy the training data to explore and prepare it

housing = train_data.copy()
# Explore the dataset
housing_label = housing["median_house_value"]   ## Answer of question
housing = housing.drop(columns = "median_house_value",axis=1)   #Question

#Columns 
Categorical = ["ocean_proximity"]
Numerical = housing.drop(columns=Categorical).columns

## Categorical pipeline 

Cat_pipeline = Pipeline([
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ("one_hot_encoder",OneHotEncoder(handle_unknown="ignore")),
])

## Numerical Pipeline

Num_pipeline = Pipeline([
    ("imputer",SimpleImputer(strategy="mean")), 
    ("scaler",MinMaxScaler(feature_range=(-1,1))),
])

## Full pipeline
full_Pipleline = ColumnTransformer([
    ("Num",Num_pipeline,Numerical),   # Takes columns
    ("Cat",Cat_pipeline,Categorical),
])


data_prepared = full_Pipleline.fit_transform(housing)

# Transform in DataFrame    
cat_features = full_Pipleline.named_transformers_["Cat"]["one_hot_encoder"].get_feature_names_out(Categorical)
cat_features = [feature.split("_")[2] for feature in cat_features]
data_prepared = pd.DataFrame(data_prepared,columns=list(Numerical)+list(cat_features),index=housing.index)

# print(data_prepared)
# LinearRegression 

print("Linear Regression Results:")
lin_reg = LinearRegression()
lin_reg.fit(data_prepared,housing_label)  #(x,y)   (data,label)

print("Actual values for first 5 rows:", housing_label.iloc[:5].values)  # Actual values for the first 5 rows
print("Predictions for first 5 rows:", lin_reg.predict(data_prepared.iloc[:5]))  # Predicting the first 5 rows

# DecisionTreeRegressor
print("\nDecision Tree Regression Results:")
Dec_reg = DecisionTreeRegressor(random_state=42)
Dec_reg.fit(data_prepared,housing_label)

print("Actual values for first 5 rows:", housing_label.iloc[:5].values)  # Actual values for the first 5 rows
print("Predictions for first 5 rows:", Dec_reg.predict(data_prepared.iloc[:5]))  # Predicting the first 5 rows

# RandomForestRegressor
print("\nRandom Forest Regression Results:")
Ran_reg = RandomForestRegressor(random_state=42)
Ran_reg.fit(data_prepared,housing_label)    
print("Actual values for first 5 rows:", housing_label.iloc[:5].values)  # Actual values for the first 5 rows  
print("Predictions for first 5 rows:", Ran_reg.predict(data_prepared.iloc[:5]))  # Predicting the first 5 rows

# Mean Squared Error for Linear Regression
lin_predictions = lin_reg.predict(data_prepared)
print("\nMean Squared Error for Linear Regression:",root_mean_squared_error(housing_label,lin_predictions))

# Mean Squared Error for Decision Tree Regression
Dec_predictions = Dec_reg.predict(data_prepared)
print("Mean Squared Error for Decision Tree Regression:",root_mean_squared_error(housing_label,Dec_predictions))   
# Mean Squared Error for Random Forest Regression
Ran_predictions = Ran_reg.predict(data_prepared)
print("Mean Squared Error for Random Forest Regression:",root_mean_squared_error(housing_label,Ran_predictions))

# Cross Validation for Linear Regression
lin_scores = -cross_val_score(lin_reg,data_prepared,housing_label,scoring="neg_root_mean_squared_error",cv=10) #cross_val_score(model,data,label,scoring,cv)  #cross_val_score returns negative values for mean_squared_error, so we negate it to get positive values
print("\nCross Validation Scores for Linear Regression:",lin_scores)

# Cross Validation for Decision Tree Regression
Dec_scores = -cross_val_score(Dec_reg,data_prepared,housing_label,scoring="neg_root_mean_squared_error",cv=10)
print("Cross Validation Scores for Decision Tree Regression:",Dec_scores)
# Cross Validation for Random Forest Regression
Ran_scores =  -cross_val_score(Ran_reg,data_prepared,housing_label,scoring="neg_root_mean_squared_error",cv=10)
print("Cross Validation Scores for Random Forest Regression:",Ran_scores)