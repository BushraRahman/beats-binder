// On page load set the theme.
(function() {
    let onpageLoad = localStorage.getItem("theme") || "";
    let element = document.body;
    element.classList.add(onpageLoad);
  })();
  
  function themeToggle() {
    let element = document.body;
    element.classList.toggle("dark_mode");
  
    let theme = localStorage.getItem("theme");
    if (theme && theme === "dark_mode") {
      localStorage.setItem("theme", "");
    } else {
        document.body.classList.remove("dark_mode")
        current_mode = "light"
        console.log("change to light")
    }
}