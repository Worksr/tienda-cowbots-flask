from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configura la conexión a tu RDS
def get_connection():
    return psycopg2.connect(
        host="retodb.ck6s4f2n4l9t.us-east-1.rds.amazonaws.com",
        dbname="retodb",
        user="retouser",
        password="Admin1234!",
        port=5432
    )

@app.route('/items', methods=['GET'])
def get_items():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM items;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        items = [{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows]
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        name = data['name']
        price = data['price']

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO items (name, price) VALUES (%s, %s);", (name, price))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Item agregado con éxito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

