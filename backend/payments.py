from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import uuid

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/pay', methods=['POST'])
@jwt_required()
def process_payment():
    user_id = get_jwt_identity()
    data = request.get_json()
    payment_id = str(uuid.uuid4())
    plan = data.get('plan_id')
    amount = data.get('amount')
    method = data.get('payment_method')

    cur = current_app.mysql.connection.cursor()
    cur.execute("""
        INSERT INTO payments (id, user_id, plan_id, amount, payment_method, status)
        VALUES (%s, %s, %s, %s, %s, 'completed')
    """, (payment_id, user_id, plan, amount, method))
    current_app.mysql.connection.commit()
    return jsonify({'message': 'Payment recorded'})
