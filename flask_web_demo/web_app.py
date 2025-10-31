from flask import Flask, render_template, request

app = Flask(__name__)

# ホーム（フォームページ）
@app.route("/")
def home():
    return render_template("index.html")

# 入力を受け取って結果ページへ
@app.route("/result", methods=["POST"])
def result():
    name = request.form["username"]
    color = request.form["favcolor"]
    return render_template("result.html", name=name, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=5006)
