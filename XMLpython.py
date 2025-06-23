import pandas as pd



df = pd.read_xml("basic-structure.xml")

print(df)
print(type(df))