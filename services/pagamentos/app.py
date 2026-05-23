from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/pagamentos", methods=["POST"])
def pagar():
    return jsonify({"status": "pago"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
