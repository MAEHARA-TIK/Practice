// 要素取得
const inputField   = document.getElementById("input-value");
const presentField = document.getElementById("present-value");
const maxField     = document.getElementById("max-value");
const minField     = document.getElementById("min-value");
const okBtn        = document.getElementById("ok");
const cancelBtn    = document.getElementById("cancel");
const decBtn       = document.getElementById("dec");
const hexBtn       = document.getElementById("hex");
const keypadRoot   = document.querySelector(".input-screen__keypad") || document.querySelector(".keypad");

let currentMode = "DEC"; // モード: DEC or HEX

const DEC_CHARS = "0123456789";
const HEX_CHARS = "0123456789ABCDEF";

// -------------------------
// 入力制御
// -------------------------
function appendValue(v) {
  const allowed = currentMode === "HEX" ? HEX_CHARS : DEC_CHARS;
  if (v === ".") {
    if (inputField.value.includes(".")) return;
    inputField.value += ".";
    return;
  }
  const up = v.toUpperCase();
  if (!allowed.includes(up)) return;
  inputField.value += up;
}

// 符号反転
function toggleSign() {
  if (!inputField.value) {
    inputField.value = "-";
  } else if (inputField.value.startsWith("-")) {
    inputField.value = inputField.value.slice(1);
  } else {
    inputField.value = "-" + inputField.value;
  }
}

// -------------------------
// 範囲チェック（Max/Minを超えない）
// -------------------------
function clampValue() {
  const max = parseInt(maxField.value, 10);
  const min = parseInt(minField.value, 10);

  let num = parseInt(inputField.value || "0", currentMode === "DEC" ? 10 : 16);
  if (isNaN(num)) num = 0;

  if (num > max) num = max;
  if (num < min) num = min;

  // 表示モードに合わせて戻す
  inputField.value =
    currentMode === "DEC" ? String(num) : num.toString(16).toUpperCase();
}

// -------------------------
// モード切り替え
// -------------------------
function switchMode(mode) {
  if (mode === currentMode) return;
  let num = parseInt(inputField.value || "0", currentMode === "DEC" ? 10 : 16);
  if (isNaN(num)) num = 0;

  if (mode === "DEC") {
    inputField.value = num.toString(10);
    currentMode = "DEC";
  } else {
    inputField.value = num.toString(16).toUpperCase();
    currentMode = "HEX";
  }
  updateModeStyle();
  updateHexAlphaEnabled();
  clampValue();
}

// -------------------------
// 見た目制御
// -------------------------
function updateModeStyle() {
  if (currentMode === "DEC") {
    decBtn.classList.add("active");
    decBtn.disabled = true;
    hexBtn.classList.remove("active");
    hexBtn.disabled = false;
  } else {
    hexBtn.classList.add("active");
    hexBtn.disabled = true;
    decBtn.classList.remove("active");
    decBtn.disabled = false;
  }
}

function updateHexAlphaEnabled() {
  const alphaBtns = document.querySelectorAll(
    '[data-value="A"],[data-value="B"],[data-value="C"],[data-value="D"],[data-value="E"],[data-value="F"]'
  );
  alphaBtns.forEach((btn) => {
    btn.disabled = currentMode === "DEC";
    btn.style.opacity = currentMode === "DEC" ? 0.5 : 1;
    btn.style.cursor = currentMode === "DEC" ? "not-allowed" : "pointer";
  });
}

// -------------------------
// イベント処理
// -------------------------
if (keypadRoot) {
  keypadRoot.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;

    const action = btn.dataset.action;
    const value = btn.dataset.value;

    if (action) {
      switch (action) {
        case "back":
          inputField.value = inputField.value.slice(0, -1);
          break;
        case "clear":
          inputField.value = "";
          break;
        case "sign":
          toggleSign();
          break;
        case "dec":
          switchMode("DEC");
          break;
        case "hex":
          switchMode("HEX");
          break;
      }
      clampValue();
      return;
    }

    if (value !== undefined) {
      appendValue(value);
      clampValue();
    }
  });
}

// -------------------------
// OK / Cancel
// -------------------------
okBtn.addEventListener("click", () => {
  clampValue();
  presentField.value = inputField.value;
});

cancelBtn.addEventListener("click", () => {
  inputField.value = "";
});

// -------------------------
// 初期化
// -------------------------
updateModeStyle();
updateHexAlphaEnabled();
clampValue();
