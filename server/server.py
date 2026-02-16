from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database (replace with MongoDB later)
users = {}

@app.route("/get_user", methods=["POST"])
def get_user():
    user_id = request.json["user_id"]

    if user_id not in users:
        users[user_id] = {"coins": 0}

    return jsonify(users[user_id])


@app.route("/watch_ad", methods=["POST"])
def watch_ad():
    user_id = request.json["user_id"]

    users[user_id]["coins"] += 10  # reward per ad
    return jsonify({"coins": users[user_id]["coins"]})


@app.route("/withdraw", methods=["POST"])
def withdraw():
    user_id = request.json["user_id"]

    if users[user_id]["coins"] < 100:
        return jsonify({"error": "Minimum 100 coins required"})

    users[user_id]["coins"] = 0
    return jsonify({"status": "Withdraw request sent"})


if __name__ == "__main__":
    app.run(port=5000)
