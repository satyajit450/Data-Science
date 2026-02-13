import os
import joblib # type: ignore
import numpy as np # type: ignore
import pandas as pd# type: ignore
import matplotlib.pyplot as plt# type: ignore
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder# type: ignore
from sklearn.model_selection import StratifiedShuffleSplit# type: ignore
from sklearn.impute import SimpleImputer# type: ignore
from sklearn.pipeline import Pipeline # type: ignore
from sklearn.compose import ColumnTransformer# type: ignore
from sklearn.ensemble import RandomForestRegressor# type: ignore


MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

def build_pipeline(num_attributes , cat_attributes) :


    num_pipeline = Pipeline([
        ("Imputer" , SimpleImputer(strategy="most_frequent")),
        ("MinMax",MinMaxScaler(feature_range=(-1,1))),
    ])
    Cat_pipeline = Pipeline([
    ("one_hot_encoder",OneHotEncoder(handle_unknown="ignore")),
    ])

    full_pipeline = ColumnTransformer ([
        ("Num",num_pipeline),num_attributes,
        ("Cat",Cat_pipeline,cat_attributes)
    ])
    return full_pipeline


if not os.path.exists(MODEL_FILE) :
    #Read CSv

    housing = pd.read_csv("housing.csv")

    housing["income_cat"] = pd.cut(housing["median_income"],bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])

    ##StratifiedShuffleSplit

    split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

    for train_index,test_index in split.split(housing,housing["income_cat"]) :
        train_data = housing.loc[train_index]
        test_data = housing.loc[test_index]


    for sett in (train_data, test_data):
        sett.drop(columns="income_cat", axis=1, inplace=True)

    housing = train_data.copy()
    # print(train_data)


    Categorical = ["ocean_proximity"]
    Numerical = housing.drop(columns="ocean_proximity").columns

    # print(train_data)

    housing_features = housing.drop("median_house_value",axis=1)
    housing_labels = housing["median_house_value"]
    print(housing_labels)