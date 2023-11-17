//worked with tyler chan (feeling sick, will fix this later)

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
    const requestResult = new XMLHttpRequest();
    requestResult.open("GET", `https://restcountries.com/v3.1/name/${selectedCountry}`);
    requestResult.send();

    requestResult.addEventListener("load", function() {
        const countryInfo = JSON.parse(this.responseText)[0];
        displayCountryInfo(countryInfo);
    })
    // let name, capital, language, population, currencies;
    // let flag = new Image();
    // for (const country of countries_list.sort((a, b) => a.name.common > b.name.common)) {   
    //     if (country.name.common == info.value) {
    //         console.log(country)
    //         name = country.name.common;
    //         capital = country.capital;
    //         language = country.languages;
    //         population = country.population;
    //         currencies = country.currencies;
    //         flag.src=`${country.flags.png}`;
    //     }
    // }
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
