import unittest
from client3 import get_data_point, get_ratio


class ClientTest(unittest.TestCase):
    def test_get_data_point_calculate_price(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock = quote['stock']
            bid_price = quote['top_bid']['price']
            ask_price = quote['top_ask']['price']
            price = (bid_price + ask_price) / 2
            self.assertEqual(get_data_point(quote), (stock, bid_price, ask_price, price))

    def test_get_data_point_calculate_price_bid_greater_than_ask(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            bid_price = quote['top_bid']['price']
            ask_price = quote['top_ask']['price']
            _, calc_bid_price, calc_ask_price, _ = get_data_point(quote)
            self.assertEquals(bid_price > ask_price, calc_bid_price > calc_ask_price)

    """ ------------ Add more unit tests ------------ """

    def test_get_ratio(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        ratio = 1.0005426841995408
        price_dict = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = get_data_point(quote)
            price_dict[stock] = price

        self.assertEquals(get_ratio(price_dict['ABC'], price_dict['DEF']), ratio)


if __name__ == '__main__':
    unittest.main()
