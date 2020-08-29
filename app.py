from flask import Flask, render_template, request, redirect, flash, url_for
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import pickle

app = Flask(__name__)

df = pd.read_csv("data.csv")
df['overview'] = df['overview'].fillna('')

def get_cosine_similarities(df):

    vectorizer = TfidfVectorizer(stop_words="english")

    tf_idf_mat = vectorizer.fit_transform(df['overview'])

    cosine_sim = linear_kernel(tf_idf_mat, tf_idf_mat)

    return cosine_sim

titles = pd.Series(df.index, index=df['lower_name']).drop_duplicates()

cosine_sim = get_cosine_similarities(df)

def get_recommendations(movie_title, cosine_similarity = cosine_sim):
    index_movie = titles[movie_title]

    name_of_movie = df.iloc[index_movie]['title']
    
    similarities = cosine_similarity[index_movie]
    
    similarity_scores = list(enumerate(similarities))
    
    similarity_scores = sorted(similarity_scores , key=lambda x: x[1], reverse = True)
    
    similarity_scores = similarity_scores[1:11]
    
    similar_indexes = [x[0] for x in similarity_scores]
    
    return df.iloc[similar_indexes], name_of_movie


@app.route('/', methods=['GET', 'POST'])
def hello():
    length = 0
    movie_name=""
    context = {'movies': [],
                'urls' : [],
                'release_dates': [],
                'runtimes':[],
                'overviews': []}
    
    if request.method=="POST":
        text = request.form['fname'].lower()
        try:
            recommended_df, movie_name = get_recommendations(text)
            context['movies'] = recommended_df.title.values
            context['urls'] = recommended_df.homepage.values
            context['release_dates'] = recommended_df.release_date.values
            context['runtimes'] = recommended_df.runtime.values
            context['overviews'] = recommended_df.overview.values

            length = len(context['movies'])
            print(text)
        except:
            return render_template('index.html', error=True)
    
    return render_template('index.html', length=length, context=context, movie_name=movie_name, error=False)

if __name__ == '__main__':
    app.run()