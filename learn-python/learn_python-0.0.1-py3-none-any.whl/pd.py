import pandas as pd


# read from csv
path = "E:/Tutos/data_samples/question_tags_10K.csv"

df = pd.read_csv(path)
print(df)
#print(df.columns)
print(df.shape)
print(df.shape[1])

