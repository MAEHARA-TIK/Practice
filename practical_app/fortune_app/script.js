// 要素を取得
const btn = document.getElementById("fortune-btn");
const result = document.getElementById("result");
const sound = document.getElementById("sound");

// ボタンを押したら実行
btn.addEventListener("click", () => {
  const fortunes = [
    { text: "大吉", color: "red", emoji: "🌸", bg: "#ffe5e5" },
    { text: "中吉", color: "orange", emoji: "😊", bg: "#fff3cd" },
    { text: "小吉", color: "green", emoji: "🍀", bg: "#e5ffe5" },
    { text: "凶", color: "gray", emoji: "💀", bg: "#e0e0e0" }
  ];

  // いったんメッセージをリセット
  result.textContent = "運勢を占っています...";
  result.style.color = "black";
  result.style.fontSize = "24px";
  result.classList.remove("show");
  document.body.style.backgroundColor = "#f8f9fa";

  // 音をリセット
  sound.pause();
  sound.currentTime = 0;

  // 1秒後に結果を表示
  setTimeout(() => {
    const random = Math.floor(Math.random() * fortunes.length);
    const fortune = fortunes[random];

    result.textContent = `あなたの運勢は…「${fortune.text}」！ ${fortune.emoji}`;
    result.style.color = fortune.color;
    result.classList.add("show");

    // 背景を変更
    document.body.style.backgroundColor = fortune.bg;

    // 音を再生
    sound.play();
  }, 1000);
});
