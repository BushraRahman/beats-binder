// Creating XMLHttpRequest object
const request_countries = new XMLHttpRequest();

// Open the given file
request_countries.open( "GET", "https://restcountries.com/v3.1/all?fields=name,flag,capital,population,languages,population,currencies,flags");

// Sending the request
request_countries.send();
let countries_list;

// Creating a callback function
request_countries.addEventListener("load", function () {
    countries_list = JSON.parse(this.responseText);
    populateSelectCountries(countries_list);
});

const selectCountriesContainer = document.querySelector(".countries_select");


const populateSelectCountries = function (data) {
    for (const country of data.sort((a, b) => a.name.common > b.name.common)) {
        let optionHtml = `<option value="${country.name.common}">${country.flag}
        ${country.name.common}</option>`;
        selectCountriesContainer.insertAdjacentHTML("beforeend", optionHtml);
    }
};


selectCountriesContainer.addEventListener("change", function() {
    const selectedCountry = this.value;
    fetch(`https://restcountries.com/v3.1/name/${selectedCountry}`)

    .then(function(response) {
        const countryInfo = response.json;
        displayCountryInfo(countryInfo);
    })
});

const displayCountryInfo = function (country) {
    const countryInfoContainer = document.querySelector(".result");
    countryInfoContainer.innerHTML = `
        <h2>Name: ${country.name.common}</h2>
        <p>Capital: ${country.capital[0]}</p>
        <p>lanugage: ${Object.values(country.languages).join(', ')}</p>
        <p>Population: ${country.population}</p>
        <p>Currency: ${Object.values(country.currencies).map(cur => cur.name).join(', ')}</p>
        <img src="${country.flags.png}">
    `
}
