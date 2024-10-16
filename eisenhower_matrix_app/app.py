# Main Flask application file

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tasks = request.form.getlist('task')
        categories = request.form.getlist('category')
        matrix = {'urgent_important': [], 'important_not_urgent': [], 'urgent_not_important': [], 'not_urgent_not_important': []}

        for task, category in zip(tasks, categories):
            if category == 'urgent_important':
                matrix['urgent_important'].append(task)
            elif category == 'important_not_urgent':
                matrix['important_not_urgent'].append(task)
            elif category == 'urgent_not_important':
                matrix['urgent_not_important'].append(task)
            else:
                matrix['not_urgent_not_important'].append(task)

        return render_template('matrix.html', matrix=matrix)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)