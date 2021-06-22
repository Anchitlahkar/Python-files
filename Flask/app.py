from flask import Flask, jsonify, request

app = Flask(__name__)


# creating an array of tasks with each task as a different object in it

tasks = [
    {
        'id': 1,
        'title': "Buy Groceries",
        'description': "Milk, Cheese,Pizza ,Fruit",
        'done': False
    },

    {
        'id': 2,
        'title': "Watch Movies",
        'description': "Flash, The Green Arrow, Loki",
        'done': False
    },


]


@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            'status': "error",
            'message': "Please provide the data"
        },400)

    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks,
    })


if(__name__ == '__main__'):
    app.run(debug=True)
