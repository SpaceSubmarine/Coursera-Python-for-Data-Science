import pandas as pd

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url,header=None)

print(df)

#Adding column name
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']


#To select a single column
#print(df["First Name"])

#To select multiple columns
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)



#loc() : loc() is label based data selecting method which 
# means that we have to pass the name of the row or column
#  which we want to select.

# To select the first row
#df.loc[0]
print(df.loc[0])

# To select the 0th,1st and 2nd row of "First Name" column only
print("\n", df.loc[[0,1,2], "First Name" ])


#iloc() : iloc() is a indexed based selecting method which means
#  that we have to pass integer index in the method to select 
# 
# specific row/column.
# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]