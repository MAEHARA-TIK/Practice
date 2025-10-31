#Flaskクラスを読み込む
from flask import Flask

#アプリ本体を生成
app = Flask(__name__)

#"/"にアクセスがきたらhome()を実行
@app.route("/")
def home():
    #ブラウザへ返すテキスト
    return "Hello Flask!"

#直接実行されたときだけ起動
if __name__ == "__main__":
    #開発サーバーを起動（Default：host="127.0.0.1", port=5000）
    app.run(debug=True)