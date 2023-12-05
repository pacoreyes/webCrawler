import {fetchData} from "./lib/utils.mjs";

async function initiateCrawler() {
  document.getElementById("triggerButton").addEventListener("click", async function () {
    try {
      const result = await fetchData("/start-crawler", "progress1");
      console.log(result)
    } catch (error) {
      console.log(error.message);
    }
  });
}

export {initiateCrawler};

