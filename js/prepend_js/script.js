let div = document.querySelector(".wrapper")
let list = document.querySelectorAll(".element")


function swap() {
	let list = document.querySelectorAll(".element")
	div.prepend(list[list.length - 1])
}
