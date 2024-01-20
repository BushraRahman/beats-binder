document.cookie = "mode=light; expires=Fri, 31 Dec 9999 23:59:59 GMT"
let mode = document.cookie

function changeMode() {
    if (mode.includes("light")) {
        document.body.classList.add("dark_mode")
        document.cookie = "mode=dark; expires=Fri, 31 Dec 9999 23:59:59 GMT"
    } else {
        document.body.classList.remove("dark_mode")
        document.cookie = "mode=light; expires=Fri, 31 Dec 9999 23:59:59 GMT"
    }
}

function updateCookie(cValue) {
    date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = cName + "=" + cValue + "; " + expires ;
}