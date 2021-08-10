from flask import Flask, jsonify, request
import csv

all_movies = []
liked_movies = []
not_liked_movies = []
not_watched_movies = []


with open('Movies.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)

    data = list(csv_reader)

all_movies = data[1:]


app = Flask(__name__)



# all-movies
@app.route('/get-movies')
def get_movie():
    return jsonify({
        'data': all_movies[0],
        'status': 'success'
    })


# liked-movies
@app.route('/liked-movies', methods=['POST'])
def like_movie():
    global all_movies

    movie = all_movies[0]
    all_movies = all_movies[1:]

    liked_movies.append(movie)

    return jsonify({
        'status': 'success'
    })


# not-liked-movies
@app.route('/not-liked-movies', methods=['POST'])
def like_movie():
    global all_movies

    movie = all_movies[0]
    all_movies = all_movies[1:]

    not_liked_movies.append(movie)

    return jsonify({
        'status': 'success'
    })


# did-not-watch-movies
@app.route('/did-not-watch-movies', methods=['POST'])
def like_movie():
    global all_movies

    movie = all_movies[0]
    all_movies = all_movies[1:]

    not_watched_movies.append(movie)

    return jsonify({
        'status': 'success'
    })




if __name__ == '__main__':
    app.run()
