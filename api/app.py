from pymongo import MongoClient
from flask import Flask, request, jsonify
import json

mongo_uri = "mongodb://admin:admin@mongodb:27017/"
client = MongoClient(mongo_uri)

db = client.db

collection = db.users

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    user_list = []
    for user in users:
        user_list.append({'name': user['name']})
    return json.dumps(user_list, ensure_ascii=False, indent=4)



@app.route('/user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    print(name)
    new_user = {'name': name}
    result = collection.insert_one(new_user)
    return jsonify({'message': 'User added successfully', 'inserted_id': str(result.inserted_id)})


@app.route('/user', methods=['PUT'])
def update_user():
    old_name = request.form.get('old_name')
    new_name = request.form.get('new_name')
    query = {'name': old_name}
    update = {"$set": {'name': new_name}}
    result = collection.update_one(query, update)
    if result.matched_count == 0:
        return jsonify({'message': 'User not found'})
    return jsonify({'message': 'User updated successfully'})

