from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

PEDIDOS_URL = os.getenv("PEDIDOS_SERVICE_URL", "http://localhost:8081")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    data = request.json
    response = requests.post(f"{PEDIDOS_URL}/pedidos", json=data)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
