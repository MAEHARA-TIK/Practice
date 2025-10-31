from flask import Flask
app = Flask(__name__)

#<name>部分を変数として受け取る
@app.route("/hello/<name>")
def hello_name(name):
    #f文字列で埋め込み。
    return f"こんにちは、{name}!"

#型指定の例：<int:age>は整数として受け取る
@app.route("/age/<int:age>")
def show_age(age):
    #受け取った値は関数の引数になる
    return f"あなたの年齢は{age}歳"

#複数パラメータの例
@app.route("/calc/<int:a>/<int:b>")
def calc(a,b):
    #足し算だけ返す
    result = a + b
    return f"{a}+{b}={result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5001,debug = True)