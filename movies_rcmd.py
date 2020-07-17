
#Import all necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.html.widgets import *
sns.set_style('white')
%matplotlib inline

#Get the data into Pandas Dataframe object
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('dataset.csv', sep = '\t', names = column_names)
df.head()

#Get the Movie Titles
movie_titles = pd.read_csv('movieIdTitles.csv')
movie_titles.head()

#Merge the dataset with movie titles
df = pd.merge(df, movie_titles, on = 'item_id')
df.head()

#Exploratory Data Analysis
df.groupby('title')['rating'].mean().sort_values(ascending = False).head()

df.groupby('title')['rating'].count().sort_values(ascending = False).head()

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()

ratings['numOfRatings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

plt.figure(figsize = (10,4))
ratings['numOfRatings'].hist(bins = 70)

plt.figure(figsize = (10,4))
ratings['rating'].hist(bins = 70)

sns.jointplot(x='rating', y='numOfRatings', data = ratings, alpha = 0.5)

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

#Most Rated Movies with their Average Ratings
ratings.sort_values('numOfRatings', ascending = False).head(10)

for i in ratings.index:
    movieUserRatings = moviemat[i]
    similarToThatMovie = moviemat.corrwith(movieUserRatings)
    corr_toMovie = pd.DataFrame(similarToThatMovie, columns = ['Correlation'])
    corr_toMovie.dropna(inplace = True)
    corr_toMovie = corr_toMovie.join(ratings['numOfRatings'])
    result = corr_toMovie[corr_toMovie['numOfRatings'] > 100].sort_values('Correlation', ascending = False).head()
    if result['numOfRatings'].count() >= 5:
        print(i)
        ratings.loc[i, 'FirstMovieRecommendation'] = result.iloc[1:2].index.values[0]
        ratings.loc[i, 'SecondMovieRecommendation'] = result.iloc[2:3].index.values[0]
        ratings.loc[i, 'ThirdMovieRecommendation'] = result.iloc[3:4].index.values[0]
        ratings.loc[i, 'FourthMovieRecommendation'] = result.iloc[4:5].index.values[0]
#Checking the result 
ratings.head()        
ratings = ratings.fillna('-')

#Save the ratings data for later use
ratings.to_csv('MovieRecommendations.csv', encoding='utf-8')

#Load the dataset saved for reusability from this code block onwards
df_result = pd.read_csv('MovieRecommendations.csv')
df_result.head()

#Load all the movie names
for i in df_result['title']:
    print(i)
    
inputMovieName = widgets.Text()

def getRecommendations(sender):
    searchMovie = inputMovieName.value
    list_result = df_result[df_result['title'] == searchMovie]
    fm = list_result['FirstMovieRecommendation'].values[0]
    sm = list_result['SecondMovieRecommendation'].values[0]
    tm = list_result['ThirdMovieRecommendation'].values[0]
    fourthm = list_result['FourthMovieRecommendation'].values[0]
    finalRecommendationText = '1:' + fm + ' \n2:' + sm + ' \n3:' + tm + ' \n4:' + fourthm
    print('Your Recommendations for the Movie ' + searchMovie + ' are:\n')
    print(finalRecommendationText)
    
#To get movie recommandatons
#Select any movie from the list of Movie Names in the dataset
# You will have your Movie Recommendation for that Particular movie
    
#Movie prediction on a given value
inputMovieName.on_submit(getRecommendations)
inputMovieName





















