from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import uuid

goals_bp = Blueprint('goals', __name__)

@goals_bp.route('/goals', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()
    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM goals WHERE user_id = %s", (user_id,))
    goals = cur.fetchall()
    return jsonify([{'id': row[0], 'title': row[2], 'progress': row[3]} for row in goals])

@goals_bp.route('/goals', methods=['POST'])
@jwt_required()
def create_goal():
    user_id = get_jwt_identity()
    data = request.get_json()
    goal_id = str(uuid.uuid4())
    title = data.get('title')
    progress = 0
    cur = current_app.mysql.connection.cursor()
    cur.execute("INSERT INTO goals (id, user_id, title, progress) VALUES (%s, %s, %s, %s)",
                (goal_id, user_id, title, progress))
    current_app.mysql.connection.commit()
    return jsonify({'message': 'Goal added'})
