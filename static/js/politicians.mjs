import {createListFromArray, fetchData} from "./lib/utils.mjs";

async function populatePoliticianTable() {
  const tableBody = document.getElementById("politicians-table").getElementsByTagName("tbody")[0];
  const numPoliticiansEl = document.querySelector("h1 > span");
  try {
    const politicians = await fetchData('/api/politicians', "progress1");
    numPoliticiansEl.textContent = politicians.length;
    for (const politician of politicians) {
      const row = tableBody.insertRow();
      row.insertCell().innerText = politician["qid"];
      row.insertCell().innerText = politician["name"];
      row.insertCell().append(createListFromArray(politician["aliases"]));
    }
  } catch (error) {
    console.error('Error fetching politicians data:', error);
  }
}

export {populatePoliticianTable};


