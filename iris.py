import pandas as pd
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Shuffle all 150 rows
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(len(df_shuffled))   # MUST print 150
print(df_shuffled)


df = pd.DataFrame(df_shuffled)

df.to_csv("suffle_iris.csv")
print("Successfull !!!")