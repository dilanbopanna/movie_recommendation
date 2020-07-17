# Movie-Recommendation-System-Using-Python
 In this project where using Pandas library to find correlation and created basic Movie Recommender System with Python.
 
The Dataset used is a subset of MovieLens Dataset.

### Extension
Have created a text input bar to add your movie whose recommendation you want. Output will give you top 4 matches that are recommended movies.

### Approach Followed

# Step 1 - Scrapping
The ml-latest dataset from MovieLens was used to get user ratings. Movie Name, DIrector, Year , Run Time, Stars, Rating, Plot were collected and the collection is in the movie/data folder.

# Step 2 - Recommending Algos
For recommendation, from the ml-latest only those users were used who had rated atleast 75 movies from IMDB Top 250. Then the codes for collaborative filtering(item-item, user-user) was written.

Matrix Factorization was done in a similar way.

# Step 3 - Prediction
The final movie reccomandation prediction is done based on a text input bar to add your movie whose recommendation you want. Output will give you top 4 matches that are recommended movies.

