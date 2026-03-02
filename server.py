from flask import Flask, render_template

app = Flask(__name__)

# --- Core Routing ---
@app.route('/')
def home():
    # Redirect root to theory by default
    return render_template('theory.html', active_page='theory')

@app.route('/theory')
def theory():
    return render_template('theory.html', active_page='theory')

@app.route('/visualizer')
def visualizer():
    return render_template('visualizer.html', active_page='visualizer')

@app.route('/codelab')
def codelab():
    return render_template('codelab.html', active_page='codelab')

@app.route('/programs')
def programs():
    # The detailed programmatic data (Level, Task, Skill, Execution, Explanation) 
    # will be injected or handled dynamically via JS to keep the template clean.
    return render_template('programs.html', active_page='programs')

if __name__ == '__main__':
    # Run fully local on port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
