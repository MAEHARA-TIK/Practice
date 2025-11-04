//ボタンを押したとき文字を変える
document.getElementById("btn").addEventListener("click", function() {
    document.getElementById("message").textContent = "ボタンが押されました";
});