
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = 'data.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS damaged_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            description TEXT,
            hours REAL,
            status TEXT DEFAULT 'Unresolved'
        )''')

@app.route("/add", methods=["POST"])
def add_item():
    data = request.json
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO damaged_items (item, description, hours) VALUES (?, ?, ?)",
                     (data['item'], data['description'], data['hours']))
    return "", 204

@app.route("/items", methods=["GET"])
def get_items():
    with sqlite3.connect(DB) as conn:
        rows = conn.execute("SELECT * FROM damaged_items").fetchall()
        return jsonify([{"id": r[0], "item": r[1], "description": r[2], "hours": r[3], "status": r[4]} for r in rows])

@app.route("/resolve/<int:item_id>", methods=["POST"])
def resolve_item(item_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("UPDATE damaged_items SET status='Resolved' WHERE id=?", (item_id,))
    return "", 204

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
