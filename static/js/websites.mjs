import {fetchData} from "./lib/utils.mjs";

// Initiate the table of websites
async function populateWebsitesTable() {
  const tableBody = document.getElementById("websites-table").getElementsByTagName("tbody")[0];
  const numWebsitesEl = document.querySelector("h1 > span");
  try {
    const websites = await fetchData('/api/websites', "progress1");
    numWebsitesEl.textContent = websites.length;
    for (const website of websites) {
      const row = tableBody.insertRow();
      const linkEl = document.createElement("a");
      linkEl.href = website["url"];
      linkEl.innerText = website["name"];
      row.insertCell().append(linkEl);
      row.insertCell().innerText = website["url"];
    }
  } catch (error) {
    console.error('Error fetching websites data:', error);
  }
}

export { populateWebsitesTable };
