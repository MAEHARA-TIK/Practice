// 色選択のプレビューをリアルタイムで反映するスクリプト
const colorPicker = document.querySelector('input[name="favcolor"]');
const previewText = document.getElementById("preview");

colorPicker.addEventListener("input", () => {
  previewText.style.color = colorPicker.value;
  previewText.textContent = `選んだ色: ${colorPicker.value}`;
});
