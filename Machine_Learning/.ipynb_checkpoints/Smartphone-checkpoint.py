import numpy as np
import pandas as pd


row_size = 1000,
names = ["Samsung", "Redmi", "Realme", "Apple", "OnePlus", 
         "Vivo", "Oppo", "Nokia", "Motorola", "Pixel"]

dict_data  = {
    "Name":np.random.choice(names,size=row_size),
    "Age" :np.random.choice([1,2,3,4,5],size=row_size),
    "Ram": np.random.choice([2,4,6,8,16],size=row_size),
    "Storage":np.random.choice([128,256,512,1],size=row_size),
    "Price" : np.random.randint(10000, 100000, size=row_size),
    "sd_card" :np.random.choice([1,2],size=row_size),
    "Rating" : np.random.choice([1,5],size=row_size)
}

df = pd.DataFrame(dict_data)

df.to_csv("smartphone.csv")