from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IllvdXJVc2VybmFtZSIsImV4cCI6MTcyMTE0MzQxMSwiaWF0IjoxNzIwNTM4NjExfQ.0T5_NSEKD2LY1euZLE1acYjH9tCWOXXHndJT5XGKw5Y'

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'password123':
        token = jwt.encode({'role': 'Admin', 'issuer': 'Issuer', 'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/blockchain', methods=['GET'])
def get_blockchain():
    token = request.headers.get('Authorization').split(' ')[1]
    try:
        jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        # Dummy blockchain data
        blockchain_data = {
            'blocks': [
                {'index': 1, 'data': 'Genesis Block'}
            ]
        }
        return jsonify(blockchain_data)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)
