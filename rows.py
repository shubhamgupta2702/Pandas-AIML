#head() tail()
#head(n) - displays first n rows.
#tail(n) - displays last n rows.

import pandas as pd

df = pd.read_csv("student_depression_dataset.csv")

print("Display 10 rows from first")
print(df.head(10)) 

print("Displays 10 rows from last")
print(df.tail(10))