import pandas as pd

html = pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")

# print(type(df))

print(html[1]) 