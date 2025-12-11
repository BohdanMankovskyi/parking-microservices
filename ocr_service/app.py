from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ocr/recognize", methods=["POST"])
def recognize():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    return jsonify({
        "message": "ok",
        "plate": "XWE591"
    }), 200


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
