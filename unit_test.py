import unittest
import main


class MyTestCase(unittest.TestCase):

    def test_name(self):
        self.assertEqual(type(main.get_products(1)[0].get_name()), str)
        self.assertEqual(type(main.get_products(1)[-1].get_name()), str)

    def test_price(self):
        self.assertGreater(int(main.get_products(1)[0].get_price()), 0)
        self.assertGreater(int(main.get_products(1)[-1].get_price()), 0)
        self.assertLess(int(main.get_products(1)[0].get_price()), 100000)
        self.assertLess(int(main.get_products(1)[-1].get_price()), 100000)

    def test_color(self):
        self.assertLess(len(main.get_products(1)[0].get_color()), 20)
        self.assertLess(len(main.get_products(1)[-1].get_color()), 20)

    def test_product_url(self):
        self.assertEqual(main.get_products(1)[0].get_product_url()[0:22], 'https://www.ssense.com')
        self.assertEqual(main.get_products(1)[-1].get_product_url()[0:22], 'https://www.ssense.com')

    def test_image_links(self):
        self.assertEqual(main.get_products(1)[0].get_image_links()[0][0:28], 'https://img.ssensemedia.com/')
        self.assertEqual(main.get_products(1)[-1].get_image_links()[0][0:28], 'https://img.ssensemedia.com/')

    def test_brand_name(self):
        self.assertEqual(type(main.get_products(1)[0].get_brand_name()), str)
        self.assertEqual(type(main.get_products(1)[-1].get_brand_name()), str)
        self.assertLess(len(main.get_products(1)[0].get_brand_name()), 15)
        self.assertLess(len(main.get_products(1)[-1].get_brand_name()), 15)

    def test_low_level(self):
        self.assertEqual(type(main.get_products(1)[0].get_low_level()), str)
        self.assertEqual(type(main.get_products(1)[-1].get_low_level()), str)
        self.assertLess(len(main.get_products(1)[0].get_low_level()), 10)
        self.assertLess(len(main.get_products(1)[-1].get_low_level()), 10)

if __name__ == '__main__':
    unittest.main()
