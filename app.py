from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks.append({"task": data['task'], "done": False})
    return jsonify({"message": "added"})

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
    return jsonify({"message": "deleted"})

@app.route('/complete/<int:index>', methods=['PUT'])
def complete_task(index):
    if index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
    return jsonify({"message": "toggled"})

@app.route('/edit/<int:index>', methods=['PUT'])
def edit_task(index):
    data = request.get_json()
    if index < len(tasks):
        tasks[index]['task'] = data['task']
    return jsonify({"message": "edited"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)