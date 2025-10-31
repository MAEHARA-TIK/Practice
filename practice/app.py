#Flaskクラスをインポート
from flask import Flask

#Flaskアプリ本体を作成
#__name__は現在のファイル名を表す特別な変数
#Flaskがテンプレートなどを探すときの基準となる
app = Flask(__name__)

#ルート("/")にアクセスがきたときに呼び出される関数を定義
@app.route("/")
def home():
    #ブラウザに表示するテキストを返す
    return "Hello Flask!"

#このファイルが直接実行されたときだけ起動する
if __name__ == "__main__":
    #Flaskサーバーを起動(debug=Trueで自動リロード&エラー表示)
    app.run(debug=True)