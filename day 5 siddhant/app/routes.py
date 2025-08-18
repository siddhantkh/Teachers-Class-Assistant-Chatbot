from flask import Blueprint, render_template, request, jsonify
from .chatbot import generate_response

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message received'}), 400
    response = generate_response(user_input)
    return jsonify({'response': response})
