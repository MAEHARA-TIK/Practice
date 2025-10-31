from flack import Flask
app = Flask(__name__)

#ホーム
@app.route("/")
def home():
    return "ここはホーム"

#アバウト
@app.route("/about")
def about():
    return "ここはアバウト"

#お問い合わせ
@app.route("/contact")
def contact():
    return "ここはお問い合わせ"

#同じ処理に複数ルートを割り当てる例
@app.route("/index")
@app.route("/top")
def index():
    return "index と Top は同じページ"

#http://127.0.0.1:5000/xxxx で変わる xxxx=abort/contact/index/top
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)