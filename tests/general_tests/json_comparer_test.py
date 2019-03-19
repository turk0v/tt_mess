import unittest
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/utils/')
from json_comparer import equals_json


class UtilsTest(unittest.TestCase):

    def test_compare_json(self):

        equalJSONS = [
            {'a': 1, 'b': 2, 'c': [1, 2],'d':[1,2,3,4]},
            {'a': 1, 'b': 2, 'c': [1, 2],'d':[1,2,3,4]}
            ]
        unequal_pairs = [
            ({'a': 1, 'b': 2,'c': [1, 2]}, {'a': 1, 'b': 2}),
            ({'a': 1, 'b': 2, 'c': [1, 2]}, {'a': 1, 'b': 2, 'c': [2, 2]})
            ]
        with self.subTest('Equal'):
            for i, json1 in enumerate(equalJSONS):
                for j, json2 in enumerate(equalJSONS[i:]):
                    self.assertTrue(equals_json(json1, json2))
        with self.subTest('Unequal'):
            for (json1, json2) in unequal_pairs:
                self.assertFalse(equals_json(json1, json2))


if __name__ == '__main__':
   unittest.main()