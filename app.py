from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return "User Management API is running!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if index < len(users):
        users[index] = request.get_json()
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < len(users):
        users.pop(index)
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)