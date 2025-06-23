import pandas as pd
from io import StringIO

df = pd.read_csv('student_depression_dataset.csv',dtype='object')
print(df.info())

print(df.isnull().sum())

df.to_csv('test.csv',index=False)

print(df.head())
print(type(df))

print(df.dtypes)

data = ('col1,col2,col3 \n'
        'x,y,z\n'
        'a,b,3.4\n'
        'ab,bc,5.5')

print(type(data))

# in memory file format object
print(StringIO(data))


res = pd.read_csv(StringIO(data))
print(res)