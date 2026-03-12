from flask import Flask, jsonify, request
from database import get_db

app = Flask(__name__)

@app.route('/api/items', methods=['GET', 'POST'])
def handle_items():
    db = get_db()
    if request.method == 'POST':
        item = request.json
        db.execute('INSERT INTO items (name, packed) VALUES (?, ?)', (item['name'], item['packed']))
        db.commit()
        return jsonify(item), 201
    else:
        items = db.execute('SELECT * FROM items').fetchall()
        return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)