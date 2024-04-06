document.querySelector("#btn").addEventListener("click", function () {
    let html = document.querySelector("html")
    let theme = html.getAttribute("data-bs-theme")
    if (theme === "dark") {
        html.setAttribute("data-bs-theme", "light")
    } else {
        html.setAttribute("data-bs-theme", "dark")
    }
})
