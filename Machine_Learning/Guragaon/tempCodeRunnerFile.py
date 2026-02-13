

# Load the dataset 
housing = pd.read_csv("housing.csv")
# Explore the dataset
housing_label = housing["median_house_value"]
housing = housing.drop(columns = "median_house_value",axis=1)

# Income_cat for split data

housing["income_cat"] = pd.cut(housing["median_income"],bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels = [1,2,3,4,5])
print(housing)