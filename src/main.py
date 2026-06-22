from flask import Flask, request, jsonify
import supabase
import os

app = Flask(__name__)

client = supabase.create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate email address
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return jsonify({'error': 'Invalid email address'}), 400

    # Validate password length
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    try:
        client.from_('users').insert({
            'username': username,
            'email': email,
            'password': password
        }).execute()
        return jsonify({'message': 'User created successfully!'})
    except supabase.client.exceptions.ClientError as e:
        return jsonify({'error': str(e.message)}), 500


