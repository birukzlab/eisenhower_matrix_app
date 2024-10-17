# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from utils.categorizer import categorize_tasks
import os

app = Flask(__name__)

# Load configurations
app.config.from_pyfile('instance/config.py')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve tasks from the form
        tasks = []
        num_tasks = int(request.form['num_tasks'])
        for i in range(num_tasks):
            task = {
                'title': request.form.get(f'title_{i}'),
                'objective': request.form.get(f'objective_{i}'),
                'importance': request.form.get(f'importance_{i}') == 'on',
                'urgency': request.form.get(f'urgency_{i}') == 'on'
            }
            tasks.append(task)
        # Store tasks in session
        session['tasks'] = tasks
        return redirect(url_for('matrix'))
    return render_template('home.html')

@app.route('/matrix')
def matrix():
    tasks = session.get('tasks', [])
    # Categorize tasks into the Eisenhower Matrix
    matrix = categorize_tasks(tasks)
    return render_template('matrix.html', matrix=matrix)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
