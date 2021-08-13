import csv

all_movies = []
with open('CSV/Movies.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)

    data = list(csv_reader)
    all_movies = data[1:]
    headers = data[0]

headers.append('Poster_link')

with open('final.csv', 'a+', encoding='utf-8') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(headers)


with open('CSV/movie_links.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)

    data=list(csv_reader)
    all_movies_links = data[1:]


for movie_item in all_movies:
    poster_found = any(movie_item[9] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_items in all_movies_links:
            if movie_item[9] == movie_link_items[0]:
                movie_item.append(movie_link_items[1])
                if len(movie_item) == 29:
                    with open('final.csv', 'a+', encoding='utf-8') as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movie_item)
                        print(f'movie append {movie_item[0]}: {movie_item[9]}')

input('\n\n\nexit...')