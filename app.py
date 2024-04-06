from flask import Flask, render_template, request, redirect, url_for
from matrix_generator import generate_matrix, generate_answer_options, check_answer

app = Flask(__name__)

score = 0

def update_score(is_correct):
    global score
    if is_correct:
        score += 1

@app.route('/')
def index():
    matrix = generate_matrix()
    answer_options = generate_answer_options(matrix)
    return render_template('index.html', matrix=matrix, answer_options=answer_options, score=score, is_correct=False)

@app.route('/submit', methods=['POST'])
def submit():
    matrix = generate_matrix()
    selected_answer = request.form['answer']
    is_correct = check_answer(matrix, selected_answer)
    update_score(is_correct)
    return render_template('index.html', matrix=matrix, answer_options=generate_answer_options(matrix), score=score, is_correct=is_correct)

if __name__ == '__main__':
    app.run(debug=True)