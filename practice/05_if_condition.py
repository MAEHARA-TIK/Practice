from flask import Flask
app = Flask(__name__)

# 年齢で分岐
@app.route("/role/<int:age>")
def role(age):
    # 条件で返す文言を切り替える
    if age < 6:
        msg = "未就学"
    elif age < 12:
        msg = "小学生"
    elif age < 18:
        msg = "中高生"
    elif age < 65:
        msg = "社会人"
    else:
        msg = "シニア"
    return f"あなたは: {msg}"

# クエリっぽい簡易スイッチ（動的ルート＋if）
@app.route("/mode/<mode>")
def mode_switch(mode):
    mode = mode.lower()
    if mode == "dev":
        return "開発モード"
    elif mode == "prod":
        return "本番モード"
    else:
        return "未知のモード"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5006,debug=True)
