let search_results

document.getElementById("search_click").onclick = function () {
    search_value = String(document.getElementById("search_box").value)
    console.log(search_value)
    callInfoAPI(search_value)
}


const callInfoAPI = async function (value) {
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
        search_results = result
    } catch (error) {
        console.error(error);
    }
}

