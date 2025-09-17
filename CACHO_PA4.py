# %% [markdown]
# # PROGRAMMING ASSIGNMENT #4

# %%
import pandas as pd

# %%
df = pd.read_excel("board2.xlsx", sheet_name="board2.csv")



# %% [markdown]
# 1. Create the following data frames based on the format provided:
# Example: Vis = [“Name”, “Gender”, “Track”, “Math<70”]; hometown is constant as Visayas

# %%
#-1a-

instru = df[(df["Track"] == "Instrumentation") & (df["Hometown"] == "Luzon")].copy()
instru["Electronics >70"] = instru["Electronics"] > 70
instru = instru[["Name", "GEAS", "Electronics >70"]]

print("\n1a. Instru DataFrame: ")
print(instru)

# %%
#-1b-
mindy = df[(df["Hometown"] == "Mindanao") & (df["Gender"] == "Female")].copy()
mindy["Average"] = mindy[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)
mindy["Average >=55"] = mindy["Average"] >= 55
mindy = mindy[["Name", "Track", "Electronics", "Average >=55"]]

print("\n1b. Mindy DataFrame:")
print(mindy)


# %% [markdown]
# 2. Create a visualization that shows how the different features contributes to average grade. Does
# chosen track in college, gender, or hometown contributes to a higher average score?

# %%
import matplotlib.pyplot as plt
import seaborn as sns


# %%
df["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)

# %%
# a. Track vs Average

plt.figure(figsize=(8,5))
sns.boxplot(x="Track", y="Average", data=df)
plt.title("Average Grade by Track")
plt.xticks(rotation=30)
plt.show()


# %%
# b. Gender vs Average
plt.figure(figsize=(6,4))
sns.boxplot(x="Gender", y="Average", data=df)
plt.title("Average Grade by Gender")
plt.show()


# %%
# c. Hometown vs average
plt.figure(figsize=(7,5))
sns.boxplot(x="Hometown", y="Average", data=df)
plt.title("Average Grade by Hometown")
plt.show()

# %%
#AVG
df["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)


print("\nAverage Grade by Track:")
print(df.groupby("Track")["Average"].mean())

print("\nAverage Grade by Gender:")
print(df.groupby("Gender")["Average"].mean())

print("\nAverage Grade by Hometown:")
print(df.groupby("Hometown")["Average"].mean())


