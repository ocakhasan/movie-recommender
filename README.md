# movie-recommender

## Dataset
This simple recommendation uses the dataset from the [TMDB 500 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata). 

## How it works

You need to run these commands
```
set FLASK_APP=app (Windows)
export FLASK_APP=app (Linux, MacOS)
```

After that,
```
flask run
```
It will run the website in http://127.0.0.1:5000/.

It recommends movie by based on their overviews.
It looks for text similarity and shows the most similar 10 results for the given input.

## Screenshots

![First Scrrenshot](https://github.com/ocakhasan/movie-recommender/blob/master/screenshots/first.png)

I am planning to deploy in soon after doing some modifications.
