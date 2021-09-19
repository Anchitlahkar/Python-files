from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendation
import csv


all_movies = []
liked_movies = []
not_liked_movies = []
not_watched_movies = []


with open('final.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)

    data = list(csv_reader)

all_movies = data[1:]


app = Flask(__name__)


# all-movies
@app.route('/get-movies')
def get_movie():
    movie_data = {
        'title': all_movies[0][9],
        'poster_link': all_movies[0][28],
        'release_date': all_movies[0][14] or 'n/a',
        'duration': all_movies[0][16],
        'rating': all_movies[0][21],
        'overview': all_movies[0][10]
    }

    return jsonify({
        'data': movie_data,
        'status': 'success'
    })


# liked-movies
@app.route('/liked-movies', methods=['POST'])
def like_movie():
    global all_movies

    movie = all_movies[0]
    liked_movies.append(movie)

    all_movies.pop(0)

    return jsonify({
        'status': 'success'
    })


# not-liked-movies
@app.route('/not-liked-movies', methods=['POST'])
def not_like_movie():
    global all_movies

    movie = all_movies[0]
    not_liked_movies.append(movie)
    all_movies.pop(0)

    return jsonify({
        'status': 'success'
    })


# did-not-watch-movies
@app.route('/did-not-watch-movies', methods=['POST'])
def did_not_watch_movie():
    global all_movies

    movie = all_movies[0]
    not_watched_movies.append(movie)
    all_movies.pop(0)

    return jsonify({
        'status': 'success'
    })


@app.route('/popular-movies')
def popular_movies():
    return jsonify({
        'data': output ,
        'status': 'success'
    })


@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recommendation(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200


if __name__ == '__main__':
    app.run()
