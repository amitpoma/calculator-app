from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/calc")
def calculate():
    data = request.get_json(force=True)

    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
        op = data.get("op")
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

    if op == "add":
        res = a + b
    elif op == "sub":
        res = a - b
    elif op == "mul":
        res = a * b
    elif op == "div":
        if b == 0:
            return jsonify({"error": "division by zero"}), 400
        res = a / b
    else:
        return jsonify({"error": "Invalid operation. Use add/sub/mul/div"}), 400

    return jsonify({"result": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
