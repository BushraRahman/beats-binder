current_mode = "light"

function changeMode() {
    if (current_mode == "light") {
        document.body.classList.add("dark_mode")
        current_mode = "dark"
        console.log("change to dark")
    } else {
        document.body.classList.remove("dark_mode")
        current_mode = "light"
        console.log("change to light")
    }
}