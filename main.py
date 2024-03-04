from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://{{your-user-data}}@userdata.xdavpql.mongodb.net/")
db = client["UserData"]
collection = db["Users"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if data:
        user = {
            "_id": data["_id"],
            "user_name": data["user_name"]
        }
        collection.insert_one(user)
        return jsonify({"message": "User added successfully"}), 201
    else:
        return jsonify({"error": "Invalid data format"}), 400

@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    if data and "_id" in data:
        user_id = data["_id"]
        result = collection.delete_one({"_id": user_id})
        if result.deleted_count == 1:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Invalid data format or user ID is missing"}), 400
    
@app.route('/users', methods=['PUT'])
def update_user():
    data = request.get_json()
    if data and "_id" in data:
        user_id = data["_id"]
        updated_user_name = data.get("user_name")
        if updated_user_name is not None:
            result = collection.find_one_and_update({"_id": user_id}, {"$set": {"user_name": updated_user_name}}, upsert=False)
            if result:
                return jsonify({"message": "User updated successfully"}), 200
            else:
                return jsonify({"error": "User not found"}), 404
        else:
            return jsonify({"error": "User name is required for update"}), 400
    else:
        return jsonify({"error": "Invalid data format or user ID is missing"}), 400

if __name__ == '__main__':
    app.run(debug=True)
