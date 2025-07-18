from flask import Blueprint, request, jsonify

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.get_json().get('message')
    # Dummy response (simulate AI response)
    response = f"You said: {user_message}"
    return jsonify({'reply': response})
