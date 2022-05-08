import datetime as date
import warnings
warnings.filterwarnings("ignore")


class Product:
    def __init__(self, display_name: str, color: str, price: str, product_url: str, image_links: list, brand_name: str,
                 low_level: str, product_material: str = None, size: list = None, description: str = None,
                 scrapped_date: date = None, gender: str = "Man", secondhand: bool = "False"):
        # Set it private
        self.__display_name = display_name
        self.__product_material = product_material
        self.__color = color
        self.__size = size
        self.__price = price
        self.__product_url = product_url
        self.__image_links = image_links
        self.__brand_name = brand_name
        self.__description = description
        self.__scrapped_date = scrapped_date
        self.__low_level = low_level
        self.__gender = gender
        self.__secondhand = secondhand

    # Some get methods
    def get_name(self):
        return self.__display_name

    def get_product_material(self):
        return self.__product_material

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    def get_product_url(self):
        return self.__product_url

    def get_image_links(self):
        return self.__image_links

    def get_brand_name(self):
        return self.__brand_name

    def get_description(self):
        return self.__description

    def get_scrapped_date(self):
        return self.__scrapped_date

    def get_low_level(self):
        return self.__low_level

    def get_gender(self):
        return self.__gender

    def get_secondhand(self):
        return self.__secondhand