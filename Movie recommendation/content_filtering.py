from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

df = df[df['soup'].notna()]

count = CountVectorizer(stop_words='english')
count_metrix = count.fit_transform(df['soup'])
cosine_sim = cosine_similarity(count_metrix, count_metrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['original_title'])


def get_recommendation(title):
    index = indices[title]
    sim_scores = list(enumerate(cosine_sim[index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1: 11]

    movie_indices = [i[0] for i in sim_scores]

    return df[['original_title', 'Poster_link', 'vote_average', 'vote_count']].iloc[movie_indices].values.tolist()
