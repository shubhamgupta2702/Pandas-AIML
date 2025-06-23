#basic operations

import numpy as np
import pandas as pd

# given = np.arange(0,20).reshape(5,4)

df = pd.DataFrame(data=[[1,5,np.nan],[45,65,np.nan]], index=["Row1", "Row2"], columns=['column1', 'column2' ,'column3'])


print(df.isnull())

print(df.isnull().sum())

print(df['column1'].value_counts())

print(df > 10)