import pandas as pd

data = {
  "Name":['Ram','Shubham','Vashu'],
  "Age":[18,19,17],
  "City":["Mau", 'Varanasi', "Goakhpur"]
}

df = pd.DataFrame(data)
print(df)


# df.to_csv("saveHoja.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)