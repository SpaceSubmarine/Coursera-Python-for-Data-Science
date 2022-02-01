#Example of Pandas
import pandas as pd

dict = {"a" : [11, 21, 31],
        "b" :[12, 22, 32]}
df = pd.DataFrame(dict)

print(df.head())

