from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database="pedidos",
        user="postgres",
        password=os.getenv("DB_PASSWORD", "postgres123")
    )

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO pedidos (cliente_id, itens, total, status) VALUES (%s, %s, %s, %s) RETURNING id",
        (data['cliente_id'], str(data['itens']), data['total'], 'CRIADO')
    )
    pedido_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({"id": pedido_id, "status": "CRIADO"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
