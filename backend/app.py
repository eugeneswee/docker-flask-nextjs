from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

def create_tables():
    db.create_all()

@app.route('/create', methods=['POST'])
def create_item():
    data = request.json
    item = Item(name=data['name'], description=data.get('description'))
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 201

@app.route('/read', methods=['GET'])
def read_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items]), 200

@app.route('/update/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get(id)
    if item:
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200
    return jsonify({'error': 'Not Found'}), 404

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return '', 204
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
