import pandas as pd 
   
df = pd.DataFrame() 
print(df)

lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
df = pd.DataFrame(lst) 
print(df)
# write to csv

df.to_csv('output.csv', index=False)