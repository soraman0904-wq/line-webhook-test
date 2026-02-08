from flask import Flask, request

print("🔥🔥🔥 THIS IS APP.PY 🔥🔥🔥")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    print("=== WEBHOOK BODY ===")
    print(body)   # ← これが超重要
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
