import pandas as pd

df = pd.DataFrame([['a', 'b'],['c','d']],
                  index=['row1', 'row2'],
                  columns=['col1', 'col2'])

print(df.to_json())

print(df.to_json(orient='index'))

print(df.to_json(orient='columns'))

print(df.to_json(orient='split'))

print(df.to_json(orient='table'))

schema = '{"schema":{"fields":[{"name":"index","type":"string"},{"name":"col1","type":"string"},{"name":"col2","type":"string"}],"primaryKey":["index"],"pandas_version":"1.4.0"},"data":[{"index":"row1","col1":"a","col2":"b"},{"index":"row2","col1":"c","col2":"d"}]}'

response = pd.read_json(schema,orient='table')

print(response)