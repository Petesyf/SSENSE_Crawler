import requests
from bs4 import BeautifulSoup
import ast
import warnings
from Product import Product

warnings.filterwarnings("ignore")


def get_products(nums_of_pages: int):
    """
    :param nums_of_pages: The total number of pages that are scrapped
    :return: A list of products and their information
    """
    product_list = []

    for i in range(nums_of_pages + 1):
        # We observe that the differences between urls are only the page numbers
        # So we can use a for loop to create the urls
        url = "https://www.ssense.com/en-us/men?page=" + str(i)
        # Use a complex header in case of website access denied
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/47.0.2526.80 Safari/537.36 '
        }
        """

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1",
                   "Connection": "close", "Upgrade-Insecure-Requests": "1"}
        r = requests.get(url, verify=False, headers=headers)
        r.encoding = "utf-8"
        page = BeautifulSoup(r.text, "html.parser")

        # Get useful info
        content = page.find("div", attrs={"class": "s-column plp-products-column__wrapper"})
        samples = content.find_all("div", attrs={"class": "plp-products__product-tile"})

        for sample in samples:
            # For every sample, find its information
            info = sample.find("script")
            # Convert string to dictionary
            info_dict = ast.literal_eval(info.contents[0])

            # Get product status
            display_name = info_dict["name"]
            # The first word of name always represents its color(e.g. "White Cotton T-Shirt")
            color = info_dict["name"].split(" ")[0]
            price = info_dict["offers"]["price"]
            # The url is not complete, need to add address before
            product_url = "https://www.ssense.com/en-us" + info_dict["url"]
            image_links = [info_dict["image"]]
            brand_name = info_dict["brand"]["name"]
            # The last word of name always represents its color(e.g. "White Cotton T-Shirt")
            low_level = info_dict["name"].split(" ")[-1]

            # Initialize this product
            product = Product(display_name, color, price, product_url, image_links, brand_name, low_level)
            product_list.append(product)
        return product_list


if __name__ == '__main__':
    nums_of_pages = 5
    product_list = get_products(nums_of_pages)
