import requests
import pandas as pd
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL of the website to scrape
TARGET_URL = "http://books.toscrape.com/"

# --- Main Functions ---

def fetch_page_content(url: str) -> str:
    
    try:
        logging.info(f"Fetching content from {url}...")
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        logging.info("Successfully fetched page content.")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching the page: {e}")
        return None

def extract_book_info(html_content: str) -> list:
    
    extracted_data = []
    if not html_content:
        logging.warning("HTML content is empty. No data to extract.")
        return extracted_data

    logging.info("Parsing HTML and extracting book information...")
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all product 'pods' which contain the book information
    books = soup.find_all('article', class_='product_pod')

    # Mapping of star rating text to numbers
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    for book in books:
        # Extract the title from the 'h3' tag's 'a' element
        title = book.h3.a['title']

        # Extract the price from the 'p' tag with the 'price_color' class
        price_text = book.find('p', class_='price_color').text
        # Remove the currency symbol and convert to float
        price = float(price_text.replace('£', ''))

        # Extract the rating from the class of the 'p' tag with 'star-rating'
        rating_classes = book.find('p', class_='star-rating')['class']
        # The rating is the second class in the list (e.g., ['star-rating', 'Three'])
        rating_text = rating_classes[1] if len(rating_classes) > 1 else 'N/A'
        rating = rating_map.get(rating_text, 0) # Default to 0 if not found

        extracted_data.append({
            'Title': title,
            'Price (GBP)': price,
            'Rating (out of 5)': rating
        })

    logging.info(f"Finished extracting information for {len(extracted_data)} books.")
    return extracted_data

def save_to_csv(data: list, filename: str = "books.csv"):
   
    if not data:
        logging.warning("No data to save. CSV file will not be created.")
        return

    try:
        # Create a pandas DataFrame from the list of dictionaries
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file without the pandas index
        df.to_csv(filename, index=False, encoding='utf-8')
        logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to CSV: {e}")

# --- Execution ---

if __name__ == "__main__":
    page_html = fetch_page_content(TARGET_URL)

    book_details = extract_book_info(page_html)

    save_to_csv(book_details)