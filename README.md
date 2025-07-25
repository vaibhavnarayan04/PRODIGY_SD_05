# Book Information Scraper

This Python script scrapes book information—specifically titles, prices, and ratings—from the website [books.toscrape.com](http://books.toscrape.com/). It then saves the extracted data into a structured CSV file named `books.csv`.

This project serves as a practical example of web scraping using Python with the `requests` and `BeautifulSoup` libraries for data extraction and `pandas` for data handling and storage.

## Features

-   Fetches HTML content from a live website.
-   Parses HTML to extract specific data points (title, price, rating).
-   Handles potential character encoding issues.
-   Saves the scraped data neatly into a CSV file.
-   Includes logging to monitor the script's execution progress and status.

## Requirements

To run this script, you need to have Python 3 installed, along with the following libraries:

-   `requests`: For making HTTP requests to fetch the webpage.
-   `pandas`: For creating a DataFrame and saving it as a CSV file.
-   `beautifulsoup4`: For parsing the HTML content.

## Installation

1.  **Clone the repository or download the script.**

2.  **Install the required libraries using pip:**
    Open your terminal or command prompt and run the following command:
    ```bash
    pip install requests pandas beautifulsoup4
    ```

