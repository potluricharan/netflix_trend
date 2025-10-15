#importing the all required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("netflix_titles.csv")

#Understanding the data
df.head()
print(df.describe())
print(df.info())
print(df.isnull().sum())

#cleaning the data
df.drop_duplicates(inplace=True)
df['country']=df['country'].fillna('unknown')
df['rating']=df['rating'].fillna('not rated')
df.dropna(subset=['date_added', 'duration'], inplace=True)
columns=['type','title','director','cast','country','listed_in','description']
for col in columns:
    df[col]=df[col].astype(str).str.strip()

#transforming the data 
df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
df['year_added']=df['date_added'].dt.year
df['month_added']=df['date_added'].dt.month_name()
df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0] if pd.notnull(x) else 'Unknown')
recent_title=df[df['release_year']>2015].sort_values(by="year_added",ascending=False)
country_counts=df.groupby('country')['show_id'].count().sort_values(ascending=False)
print(country_counts.head())

#data vizulization
# Set style
sns.set(style="whitegrid", palette="muted")

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title("Distribution of Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()


top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries with Most Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()


titles_by_year = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.lineplot(x=titles_by_year.index, y=titles_by_year.values)
plt.title("Trend of Content Added Over the Years")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.show()


top_genres = df['main_genre'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Main Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()


plt.tight_layout()
plt.show()
 # type: ignore