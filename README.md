# webCrawler: Web Crawler Application

This Python application is a web crawler that systematically browses websites, processing the URLs and storing relevant data. It's particularly focused on extracting information related to politicians from the sites it visits.

## Features

The web crawler provides the following key features:

- **Website Crawling**: It visits each URL of a website and processes the content to extract useful data. 
- **Customizable User Agents**: Randomly selects user agents from a list for each request. This is done to prevent blocking by websites that limit requests from the same user agent.
- **URL Filtering**: It filters out suspicious URLs and URLs that are not allowed by `robots.txt` of the website. It also ensures that it only visits new URLs and does not revisit already visited ones.
- **Data Extraction**: Extracts page content, including the page title and text within paragraph tags. 
- **Politician Information Extraction**: It specifically looks for politician names in the title of each page visited and classifies the page as potentially useful if it contains a politician's name.
- **Data Storage**: Stores data in a SQLite database and Firestore. It saves all URLs visited, but only includes additional data for potentially useful pages (those that contain politician names).
- **Error Handling**: The application handles various exceptions that may arise during the web crawling process, such as timeouts and WebDriver exceptions.

## Tech Stack

- **Python**: The application is written entirely in Python.
- **SQLite**: A relational database used for storing URL data.
- **Firestore**: Google's NoSQL cloud database used for storing more extensive data for potentially useful pages.
- **Selenium**: A tool for automating browsers. This application uses Selenium to fetch web pages.
- **BeautifulSoup**: A library for extracting data from HTML and XML files. It is used for parsing HTML content of web pages.
- **urllib**: A Python module used for fetching URLs.

## Prerequisites

- Python 3
- Selenium WebDriver
- SQLite
- Firestore

## Installation

1. Clone the repository: `git clone https://github.com/pacoreyes/webCrawler.git`
2. Navigate to the project directory: `cd web-crawler`
3. Install the required Python modules: `pip install -r requirements.txt`

## Usage

1. To run the crawler, execute `python3 main.py`
2. The crawler will start from the position saved in the `POSITION_FILE`. If this is the first time running the crawler, it will start from the beginning.

Note: Make sure to respect the policies outlined in `robots.txt` of the websites you're crawling. Some sites do not allow certain pages to be crawled, and others limit the frequency of requests.