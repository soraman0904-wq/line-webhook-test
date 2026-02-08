from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # JSON を強制的に取得
    body = request.get_json(force=True)
    print("=== WEBHOOK BODY ===")
    print(body)
    return "OK", 200

# 開発用サーバーで直接実行したい場合はコメントアウト
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)
