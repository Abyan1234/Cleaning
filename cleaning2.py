import pandas as pd
import csv

df=pd.read_csv("new_total_stars.csv")

del df["Unnamed: 0"]
del df["Unnamed: 6"]


df.to_csv('final_total_stars.csv')

