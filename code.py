import pandas as pd 
import os 

#Create a sample DataFrame with column names
data={'Name': ['Alice','Bob','Charlie'],
      'Age':[25,20,30],
      'City': ['New York','Los Angeles','Chicago']
    }

df=pd.DataFrame(data)

## Adding a new row to df for V2
new_row_loc ={'Name': 'Emily','Age':35,'City':'Texas'}
df.loc[len(df.index)]=new_row_loc 

## Adding a new row to df for V3
# new_row_loc2 ={'Name': 'V3','Age':40,'City':'Vegas'}
# df.loc[len(df.index)]=new_row_loc2

#Ensure the "data" directory exists at root level 
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path 
file_path=os.path.join(data_dir,"sample_data.csv")

#Save the DataFrame to a CSV file, including column names
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")




