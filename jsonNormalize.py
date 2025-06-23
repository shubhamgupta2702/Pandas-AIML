res = {"employee_name":"Shubham","email":"shubhamg@gmail.com","Job_profile":{"title1":"Data Scientist","title2":"Software Developer"}}

import pandas as pd

print(type(res))

print(pd.json_normalize(res ))