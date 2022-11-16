let closeBtn = document.getElementById("close-sidebar");
let sidebar = document.querySelector(".sidebar");
let showBtn = document.getElementById("show-sidebar");


closeBtn.addEventListener("click", function () {
    sidebar.classList.toggle("hide");
    showBtn.classList.add("toggle");
})

showBtn.addEventListener("click", function () {
    sidebar.classList.toggle("hide");
    showBtn.classList.remove("toggle");
})