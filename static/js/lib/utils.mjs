/**
 * Create a counter widget that shows entity and its quantity.
 *
 * @param {string} entity - The entity name to be displayed.
 * @param {number} quantity - The quantity of the entity to be displayed.
 * @returns {object} The created span element.
 */
function createCounterWidget(entity, quantity) {
  const spanEl = document.createElement("span");
  spanEl.textContent = `${entity} (${quantity.toString()})`;
  return spanEl;
}

/**
 * Toggles the visibility of the navigation menu.
 */
function toggleNavigationMenuVisibility() {
  const iconEl = document.querySelector("div.nav-icon"),
    navEl = document.querySelector("nav.menu-tray");
  iconEl.addEventListener("click", function () {
    navEl.hidden = navEl.hidden !== true;
  });
}

/**
 * Convert a map of values into a UL element.
 *
 * @param {object} et - The entity table.
 * @param {string} displayProp - The object property to be displayed in the list.
 * @returns {object} The created UL element.
 */
function createListFromMap(et, displayProp) {
  const listEl = document.createElement("ul");
  fillListFromMap(listEl, et, displayProp);
  return listEl;
}

/**
 * Fill a list element with items from an entity table.
 *
 * @param {object} listEl - A list element.
 * @param {object} et - An entity table.
 * @param {string} displayProp - The object property to be displayed in the list.
 */
function fillListFromMap(listEl, et, displayProp) {
  const keys = Object.keys(et);
  // delete old contents
  listEl.innerHTML = "";
  // create list items from object property values
  for (const key of keys) {
    const listItemEl = document.createElement("li");
    listItemEl.textContent = et[key][displayProp];
    listEl.appendChild(listItemEl);
  }
}

/**
 * Create a list from an array.
 *
 * @param {array} array - The array of elements.
 * @returns {object} The created UL element.
 */
function createListFromArray(array) {
  const listEl = document.createElement("ul");
  for (const el of array) {
    const listItemEl = document.createElement("li");
    listItemEl.textContent = el;
    listEl.appendChild(listItemEl);
  }
  return listEl;
}

/**
 * Show a progress bar element.
 *
 * @param {string} elementId - The ID of the progress bar element.
 */
function showProgressBar(elementId) {
  const progressEl = document.querySelector(`progress#${elementId}`);
  progressEl.hidden = false;
}

/**
 * Hide a progress bar element.
 *
 * @param {string} elementId - The ID of the progress bar element.
 */
function hideProgressBar(elementId) {
  const progressEl = document.querySelector(`progress#${elementId}`);
  progressEl.hidden = true;
}

/**
 * Trigger an action by making a GET request to a URL when a button is clicked.
 *
 * @param {string} url - The URL to make a GET request to.
 * @param {string} progressId - The ID of the progress bar element.
 * @param {string} [buttonId=triggerButton] - The ID of the button to add the click event listener to.
 */
/*function triggerAction(url, progressId, buttonId = "triggerButton") {
  const button = document.getElementById(buttonId);

  button.addEventListener("click", async function () {
    showProgressBar(progressId);
    await fetch(url, {
      method: "GET",
    });
    hideProgressBar(progressId);
  });
}*/

/**
 * Create option elements with issue parents from data.
 *
 * @param {array} data - The array of data.
 * @returns {object} The created document fragment.
 */
function createOptionsWithIssuesParents(data) {
  const fragment = new DocumentFragment();
  for (const l1 of data) {
    const groupEL = document.createElement("optGroup");
    groupEL.setAttribute("label", l1["preferred_name"].trim());
    for (const l2 of l1.children) {
      const optEL = document.createElement("option");
      optEL.setAttribute("value", l2["qid"]);
      optEL.innerHTML = l2["preferred_name"];
      groupEL.appendChild(optEL);
    }
    fragment.appendChild(groupEL);
  }
  return fragment;
}

/**
 * Convert a JS Date object to Date string in format YYYY-MM-DD.
 *
 * @param {object} dateObj - A Date object.
 * @returns {string} The date string in YYYY-MM-DD format.
 */
function date2IsoDateString(dateObj) {
  let y = dateObj.getFullYear(),
    m = "" + (dateObj.getMonth() + 1),
    d = "" + dateObj.getDate();
  if (m.length < 2) m = "0" + m;
  if (d.length < 2) d = "0" + d;
  return [y, m, d].join("-");
}

/**
 * Fetch data from an API endpoint and show a progress bar while the data is being fetched.
 *
 * @param {string} apiEndpoint - The API endpoint to fetch data from.
 * @param {string} progressBarId - The ID of the progress bar element.
 * @returns {object} The fetched data.
 * @throws Will throw an error if the fetch operation fails.
 */
async function fetchData(apiEndpoint, progressBarId) {
  showProgressBar(progressBarId);
  try {
    const response = await fetch(apiEndpoint);
    return await response.json();
  } catch (error) {
    console.error(`Error fetching data from ${apiEndpoint}:`, error);
    hideProgressBar(progressBarId);
    throw error;
  } finally {
    hideProgressBar(progressBarId);
  }
}

export {
  createCounterWidget, toggleNavigationMenuVisibility, createListFromMap,
  createListFromArray, showProgressBar, hideProgressBar,
  createOptionsWithIssuesParents, date2IsoDateString, fetchData
};
