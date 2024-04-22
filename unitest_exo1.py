"""Activités
Écrivez un programme Python qui prend une liste de tuples et 
affiche le tuple avec le plus d'éléments."""

def tuple_max_elements(list_tuple):   #define the max element in the list of tuple
    max_len = 0    # now if the maximum length corresponds to zero
    max_tuple = ()   # the maximum tuple is  empty 
    for e in list_tuple:   # for element in the list of tuples,
        if len(e) > max_len:    # if the length of element is > the maximum length
            max_len = len(e)    # maximum length is affected to len(e)
            max_tuple = e       # maximum tuple is affected to element
    return max_tuple        # return the maximum tuple
# Exemple d'utilisation
list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
result = tuple_max_elements(list)
print("The max element in the tuple is :", result)





# ####### Unitest #######
import unittest


class TestTupleMaxElements(unittest.TestCase):

    def test_tuple_max_elements(self):
        self.assertEqual(tuple_max_elements([(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]), (7, 8, 9, 10))
    
    def test_tuple_max_elements2(self):
        self.assertEqual(tuple_max_elements([(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10), (11, 12, 13, 14, 15)]), (11, 12, 13, 14, 15))
        self.assertEqual(tuple_max_elements([(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,2)]), (8,2))

if __name__ == '__main__':
    unittest.main()
