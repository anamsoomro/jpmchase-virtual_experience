import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      from_data = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2)
      from_function = getDataPoint(quote)
      self.assertEqual(from_data, from_function)

  # def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
  #   quotes = [
  #     {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
  #     {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
  #   ]
  #   self.assertEqual(1,1)

  def test_getRatio(self):
    stock_compares = [
      {'priceA': 10, 'priceB': 5, 'ratio': 0.5},
      {'priceA': 0, 'priceB': 5, 'ratio': 0},
      {'priceA': 5, 'priceB': 0, 'ratio': 0},
    ]
    for stock_compare in stock_compares:
      from_function = getRatio(stock_compare['priceA'], stock_compare['priceB'])
      self.assertEqual(from_function, stock_compare['ratio'])


if __name__ == '__main__':
    unittest.main()
