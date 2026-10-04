from flask import Flask, request, jsonify

app = Flask(__name__)

registrations = [
    {
        "name": "Sania",
        "event": "Tech Fest"
    }
]

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(registrations), 200

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data or "name" not in data or "event" not in data:
        return jsonify({"error": "Invalid input. Both 'name' and 'event' are required."}), 400

    registrations.append(data)

    return jsonify({
        "message": "Registration added successfully",
        "registration": data
    }), 201

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)