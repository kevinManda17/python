import pandas as pd 

data_file="celsius_farinette_dataset.csv"
data= pd.read_csv(data_file, header=None)
data.columns = ["temp_c", "temp_f"]

print(f"File contains: {data.shape}")
data.describe()

data.plot(kind="scatter", x="temp_c", y="temp_f")

