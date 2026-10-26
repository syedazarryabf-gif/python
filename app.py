
from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

ENDPOINT = os.environ["EBAY_ENDPOINT"]
TOKEN = os.environ["EBAY_VERIFICATION_TOKEN"]


@app.route("/endpoint", methods=["GET", "POST"])
def ebay_notification():
    if request.method == "GET":
        challenge = request.args.get("challenge_code")

        if not challenge:
            return jsonify({"error": "Missing challenge code"}), 400

        raw = challenge + TOKEN + ENDPOINT
        result = hashlib.sha256(raw.encode("utf-8")).hexdigest()

        return jsonify({"challengeResponse": result})

    return "", 200
