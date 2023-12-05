import {fetchData} from "./lib/utils.mjs";

// Initiate the table of user agents
async function populateUserAgentsTable() {
  const tableBody = document.getElementById("websites-table").getElementsByTagName("tbody")[0];
  const numWebsitesEl = document.querySelector("h1 > span");
  try {
    const userAgents = await fetchData('/api/user-agents', "progress1");
    numWebsitesEl.textContent = userAgents.length;
    for (const user_agent of userAgents) {
      const row = tableBody.insertRow();
      row.insertCell().innerText = user_agent["name"];
    }
  } catch (error) {
    console.error('Error fetching user agents data:', error);
  }
}

export { populateUserAgentsTable };
