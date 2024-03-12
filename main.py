import pandas as pd

#Reading in CSV file 
df = pd.read_csv(r"C:\Users\Iaine\.vscode\Python Projects\ACNH Project\ACNH Items\headwear.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df.head())




#Turning source into a string 
df["Source"] = df["Source"].astype("string")
print(df.dtypes)

#Top 5 highest selling headwear that can only be crafted 
top_selling_headwear_df = df.loc[(df['Sell'] > 500) & (df['Source'] != "Able Sisters")].sort_values(by = "Sell", ascending = False).head(5)
print(top_selling_headwear_df.filter(items = ["Name","Sell","Source"]))




#Turning buy into a string 
df["Buy"] = df["Buy"].astype("string")
print(df.dtypes)

#Turning "Not For Sale" items to price of 0 
df["Buy"] = df["Buy"].replace("NFS","0")

#Top 5 most expensive headwear to buy 
most_expensive_headwear_items = df.sort_values(by = "Buy", ascending = False).head(5)
print(most_expensive_headwear_items.filter(items = ["Name","Buy","Sell"]))




#Grouping on colors that are in the game and their respective counts, then filtering on "rare" or 1 of colors in the game 
group_by_colors_df = df.groupby("Variation").count().filter(items = ["Name"]).rename(columns = {"Name":"Count"}).sort_values(by = "Count")
group_by_colors_df = group_by_colors_df.loc[group_by_colors_df["Count"] == 1]
print(group_by_colors_df)




#Grouping on hats and the number of variations they have 
group_by_hats_df = df.groupby("Name").count().filter(items = ["Variation"]).rename(columns = {"Variation" : "Color Variations"}).sort_values(by = "Color Variations", ascending = False)
print(group_by_hats_df)

print(df.filter(items = ["Name","Buy","Sell"]))