import pandas as pd

df1 = pd.read_csv("student_depression_dataset.csv")
df = pd.DataFrame({ 
  "Name":['Ram','Shubham','Vashu'],
  "Age":[18,19,17],
  "City":["Mau", 'Varanasi', "Goakhpur"]
})

print("Displaying the infor of dataset: ")
print(df.info())
print(df1.info())