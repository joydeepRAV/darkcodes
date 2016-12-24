#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
	{
		'name': 'joydeep',
		'roll': 1,
		'done': False
	},
        {
                'name': 'Atrayee',
                'roll': 2,
                'done': False
        },
        {
                'name': 'Raj',
                'roll': 3,
                'done': False
        },
        {
                'name': 'jisu',
                'roll': 4,
                'done': False
        }
	]

@app.route('/', methods = ['GET'])
def gett():
	return jsonify({'Students': tasks})


@app.route('/<na>', methods = ['GET'])
def get_task(na):
	task=[task for task in tasks if task['name'] == na] 
	if len(task)==0:
		abort(404)
   	return jsonify({'student': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
