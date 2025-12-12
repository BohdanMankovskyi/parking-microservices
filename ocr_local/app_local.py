from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/recognize", methods=["POST"])
def recognize():
    # Simple echo response to confirm service is reachable
    if "image" not in request.files:
        return jsonify({"error": "no image"}), 400
    return jsonify({"plate": "DUMMY"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
