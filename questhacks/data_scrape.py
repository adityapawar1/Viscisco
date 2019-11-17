import pandas as pd
x = pd.DataFrame(pd.read_csv('Database.csv')) 
x=x.drop(0)
print(x)