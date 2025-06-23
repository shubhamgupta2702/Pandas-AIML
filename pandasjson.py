data = '{"employee_name":"Shubham","email":"shubhamg@gmail.com","Job_profile":[{"title1":"Data Scientist","title2":"Software Developer"}]}'

print(type(data))

import pandas as pd

print(pd.read_json(data,orient='index'))
print(pd.read_json(data,orient='records'))
