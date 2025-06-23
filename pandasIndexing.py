import pandas as pd
import numpy as np

given = np.arange(0,20).reshape(5,4)

df = pd.DataFrame(data=given, index=["Row1", "Row2", "Row3", 'Row4', 'Row5'], columns=['column1', 'column2', 'column3', 'column4'])

#indexing
# columnname, rowindex[loc], rowindex columnindex number[.iloc]

print(df['column4'])
print(df["column2"])

print(type(df['column2']))  #<class 'pandas.core.series.Series'>