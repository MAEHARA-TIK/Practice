from flask import Flask, render_template
app = Flask(__name__,template_folder="template")

# ホームページ
@app.route("/")
def home():
    return render_template("index.html")

# リンクページ
@app.route("/links")
def links():
    return render_template("links.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006, debug=True)
