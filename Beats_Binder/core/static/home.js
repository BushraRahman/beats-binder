document.getElementById("search_click").onclick = function () {
    if (document.getElementById("search_box").value == null) {
        alert("Search box cannot be empty.")
    } else {
        search_value = String(document.getElementById("search_box").value)
        console.log("success")
    }
}

const callAPI = async function (value) {
    const url = 'https://deezerdevs-deezer.p.rapidapi.com/search?q=' + value;
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'de8f6f2a3fmsh850207b34ede80bp17e3d8jsnd9883430d914',
            'X-RapidAPI-Host': 'deezerdevs-deezer.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}