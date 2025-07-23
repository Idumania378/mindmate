from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import os
from .db import get_db

bp = Blueprint('chat', __name__, url_prefix='/api/chat')

# Sample mental health responses
MENTAL_HEALTH_RESPONSES = {
    'stress': "Stress is common. Try deep breathing: Inhale for 4s, hold for 4s, exhale for 6s. Repeat. Would you like to talk more about what's stressing you?",
    'anxiety': "Anxiety can feel overwhelming. Try grounding techniques: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you can taste.",
    'sad': "I'm sorry you're feeling this way. Small steps like a short walk or talking to someone you trust can help. Would you like some resources?",
    'happy': "I'm glad you're feeling good! Celebrating positive moments helps mental wellbeing. Consider journaling about this feeling.",
    'sleep': "Sleep affects mental health. Try keeping a consistent schedule and reducing screen time before bed. Are you having trouble falling or staying asleep?"
}

@bp.route('/send', methods=['POST'])
def send_message():
    """
    Handle incoming chat messages and generate responses
    """
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message', '').strip().lower()
    
    if not message:
        return jsonify({'error': 'Empty message'}), 400
    
    # Save message to database
    db = get_db()
    try:
        db.execute(
            "INSERT INTO messages (user_id, message, is_bot, created_at) VALUES (?, ?, ?, ?)",
            (user_id, message, False, datetime.now())
        )
        db.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Generate response (in production, this would call Qwen AI)
    response = generate_response(message)
    
    # Save bot response to database
    try:
        db.execute(
            "INSERT INTO messages (user_id, message, is_bot, created_at) VALUES (?, ?, ?, ?)",
            (user_id, response, True, datetime.now())
        )
        db.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'response': response,
        'timestamp': datetime.now().isoformat()
    })

def generate_response(message):
    """
    Generate appropriate response based on message content
    """
    # Check for specific keywords
    for keyword, response in MENTAL_HEALTH_RESPONSES.items():
        if keyword in message:
            return response
    
    # Default responses
    default_responses = [
        "I hear you. Would you like to share more?",
        "Thank you for sharing. How has this been affecting you?",
        "I understand. What would be most helpful right now?",
        "That sounds challenging. Would you like to explore coping strategies?",
        "I'm here to listen. Would you like to continue sharing?"
    ]
    
    return default_responses[len(message) % len(default_responses)]

@bp.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    """
    Retrieve chat history for a user
    """
    db = get_db()
    messages = db.execute(
        "SELECT message, is_bot, created_at FROM messages WHERE user_id = ? ORDER BY created_at ASC",
        (user_id,)
    ).fetchall()
    
    return jsonify({
        'history': [
            {
                'message': msg['message'],
                'is_bot': bool(msg['is_bot']),
                'timestamp': msg['created_at']
            }
            for msg in messages
        ]
    })