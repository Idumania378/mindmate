from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_jwt_extended import create_access_token
import uuid
from db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    hashed_password = generate_password_hash(password)
    user_id = str(uuid.uuid4())

    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cur.fetchone():
        return jsonify({'error': 'Email already exists'}), 400

    cur.execute("INSERT INTO users (id, email, password_hash, name) VALUES (%s, %s, %s, %s)",
                (user_id, email, hashed_password, name))
    current_app.mysql.connection.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if not user or not check_password_hash(user[1], password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity=user[0])
    return jsonify({'token': token})
