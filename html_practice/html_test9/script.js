document.getElementById("btn").addEventListener("click", function() {
    document.getElementById("message").textContent = "ボタンが押されました";
});

// おみくじ機能
document.getElementById("fortune-btn").addEventListener("click", function() {
  const results = ["大吉", "中吉", "小吉", "凶"];
  const random = Math.floor(Math.random() * results.length);
  document.getElementById("result").textContent = "あなたの運勢は…「" + results[random] + "」！";
});

// 名前入力に反応する
document.getElementById("hello-btn").addEventListener("click", function() {
  const name = document.getElementById("name").value;
  if (name === "") {
    document.getElementById("hello").textContent = "名前を入れてね！";
  } else {
    document.getElementById("hello").textContent = "こんにちは、" + name + "さん！";
  }
});

// 色をランダムに変更
document.getElementById("color-btn").addEventListener("click", function() {
  const colors = ["red", "blue", "green", "purple", "orange"];
  const random = Math.floor(Math.random() * colors.length);
  document.getElementById("color-text").style.color = colors[random];
});
