import os

def create_project_structure():
    # Define folder structure
    folders = [
        "eisenhower_matrix_app/static/css",
        "eisenhower_matrix_app/static/js",
        "eisenhower_matrix_app/templates",
        "eisenhower_matrix_app/utils",
        "eisenhower_matrix_app/instance",
    ]

    # Define files to create
    files = {
        "eisenhower_matrix_app/app.py": "# Main Flask application file\n\nfrom flask import Flask, render_template, request\n\napp = Flask(__name__)\n\n@app.route('/', methods=['GET', 'POST'])\ndef home():\n    if request.method == 'POST':\n        tasks = request.form.getlist('task')\n        categories = request.form.getlist('category')\n        matrix = {'urgent_important': [], 'important_not_urgent': [], 'urgent_not_important': [], 'not_urgent_not_important': []}\n\n        for task, category in zip(tasks, categories):\n            if category == 'urgent_important':\n                matrix['urgent_important'].append(task)\n            elif category == 'important_not_urgent':\n                matrix['important_not_urgent'].append(task)\n            elif category == 'urgent_not_important':\n                matrix['urgent_not_important'].append(task)\n            else:\n                matrix['not_urgent_not_important'].append(task)\n\n        return render_template('matrix.html', matrix=matrix)\n\n    return render_template('home.html')\n\nif __name__ == '__main__':\n    app.run(debug=True)",
        "eisenhower_matrix_app/static/css/styles.css": "/* Custom CSS styles for the app */\nbody {\n    font-family: Arial, sans-serif;\n    background-color: #f9f9f9;\n}\nheader {\n    background-color: #007bff;\n    color: white;\n    padding: 10px;\n    text-align: center;\n}\n.content {\n    margin: 20px;\n}\n",
        "eisenhower_matrix_app/static/js/script.js": "// Optional JavaScript for interactive features\n",
        "eisenhower_matrix_app/templates/base.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/styles.css') }}\">\n    <title>Eisenhower Matrix App</title>\n</head>\n<body>\n    <header>\n        <h1>Prioritize Ruthlessly</h1>\n    </header>\n    <div class=\"content\">\n        {% block content %}{% endblock %}\n    </div>\n</body>\n</html>",
        "eisenhower_matrix_app/templates/home.html": "{% extends 'base.html' %}\n{% block content %}\n<form method=\"post\">\n    <label for=\"task\">Task Name:</label>\n    <input type=\"text\" name=\"task\" required>\n    <label for=\"category\">Task Category:</label>\n    <select name=\"category\">\n        <option value=\"urgent_important\">Urgent & Important</option>\n        <option value=\"important_not_urgent\">Important but Not Urgent</option>\n        <option value=\"urgent_not_important\">Urgent but Not Important</option>\n        <option value=\"not_urgent_not_important\">Neither Urgent nor Important</option>\n    </select>\n    <button type=\"submit\">Add Task</button>\n</form>\n{% endblock %}",
        "eisenhower_matrix_app/templates/matrix.html": "{% extends 'base.html' %}\n{% block content %}\n<h2>Your Eisenhower Matrix</h2>\n<div>\n    <h3>Urgent & Important</h3>\n    <ul>\n    {% for task in matrix['urgent_important'] %}\n        <li>{{ task }}</li>\n    {% endfor %}\n    </ul>\n</div>\n<div>\n    <h3>Important but Not Urgent</h3>\n    <ul>\n    {% for task in matrix['important_not_urgent'] %}\n        <li>{{ task }}</li>\n    {% endfor %}\n    </ul>\n</div>\n<div>\n    <h3>Urgent but Not Important</h3>\n    <ul>\n    {% for task in matrix['urgent_not_important'] %}\n        <li>{{ task }}</li>\n    {% endfor %}\n    </ul>\n</div>\n<div>\n    <h3>Neither Urgent nor Important</h3>\n    <ul>\n    {% for task in matrix['not_urgent_not_important'] %}\n        <li>{{ task }}</li>\n    {% endfor %}\n    </ul>\n</div>\n{% endblock %}",
        "eisenhower_matrix_app/utils/categorizer.py": "# Utility functions for categorizing tasks\n",
        "eisenhower_matrix_app/instance/config.py": "# Configuration settings for the Flask app\nDEBUG = True\n"
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files with initial content
    for filepath, content in files.items():
        # Skip creating README.md if it already exists
        if filepath == "eisenhower_matrix_app/README.md":
            continue
        with open(filepath, 'w') as file:
            file.write(content)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")