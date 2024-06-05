// const text = document.querySelector(".anime").addEventListener("click", () => {
//   console.log(alert("yahoooo"));
// });

const text = document.querySelector(".anime");
// console.log(text);
const textStr = text.textContent;
// console.log(textStr);
const splitStr = textStr.split("");
// console.log(splitStr);
text.textContent = "";
for (let i = 0; i < splitStr.length; i++) {
  text.innerHTML += "<span>" + splitStr[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick() {
  const span = text.querySelectorAll("span")[char];
  span.classList.add("fade");
  char++;
  if (char === splitStr.length) {
    complete();
    return;
  }
}

function complete() {
  clearInterval(timer);
  timer = null;
}
