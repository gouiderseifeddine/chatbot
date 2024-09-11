from flask import Flask, request, jsonify, render_template, Response
import json

app = Flask(__name__)

# Read the questions from the JSON file with explicit UTF-8 encoding
with open('questions_answers.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

@app.route('/')
def home():
    response = Response(render_template('chat.html', questions=questions))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/get', methods=['GET'])
def get_bot_response():
    question = request.form['question']
    # Find the answer based on the question
    for category in questions:
        for qa in category['questions']:
            if qa['question'] == question:
                return jsonify(answer=qa['answer'])
    return jsonify(answer="Sorry, I don't understand that question.")

if __name__ == '__main__':
    app.run(debug=True)
