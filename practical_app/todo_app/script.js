// 要素を取得
const input = document.getElementById("task-input");
const addBtn = document.getElementById("add-btn");
const taskList = document.getElementById("task-list");

// 追加ボタンを押したら実行
addBtn.addEventListener("click", () => {
  const task = input.value.trim(); // ← .valueを忘れずに

  // 入力が空白なら無視
  if (task === "") return;

  // liタグ生成
  const li = document.createElement("li");
  li.textContent = task;

  // 削除ボタン生成
  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "削除";
  deleteBtn.classList.add("delete");

  // 削除ボタン押下で削除
  deleteBtn.addEventListener("click", () => {
    li.remove();
  });

  // liに削除ボタンを追加
  li.appendChild(deleteBtn);

  // タスクリストにliを追加
  taskList.appendChild(li);

  // 入力欄を空にする
  input.value = "";
});
