from flask import Flask, request, jsonify
from chatbot_core import ask_college_bot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    answer = ask_college_bot(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )
