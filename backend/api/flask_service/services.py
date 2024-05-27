from bs4 import BeautifulSoup
import requests
from .models import products_collection

def scrape_product(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        product_name = soup.find('h1', class_='product-title').text.strip()
        product_price = soup.find('span', class_='product-price').text.strip()
        product_image = soup.find('img', class_='product-image')['src']

        product = {
            "name": product_name,
            "price": product_price,
            "image": product_image
        }

        products_collection.insert_one(product)
        return product
    except AttributeError:
        return None
