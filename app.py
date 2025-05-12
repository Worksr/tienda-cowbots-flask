from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configura la conexión a la base de datos RDS
def get_db_connection():
    return psycopg2.connect(
        host="retodb.ck6s4f2n4l9t.us-east-1.rds.amazonaws.com",
        database="retodb",
        user="retouser",
        password="Admin1234!",
        port="5432"
    )

# Ruta para obtener todos los productos
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()

    results = []
    for item in items:
        results.append({
            "id": item[0],
            "name": item[1],
            "price": float(item[2])
        })

    return jsonify(results)

# Ruta para agregar nuevos productos
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item agregado con éxito"}), 201

# Ejecutar el servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

