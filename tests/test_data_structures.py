import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_generate_random_list(self):
        result = generate_random_list(5)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(0 <= num <= 100 for num in result))

    def test_find_max(self): 
        self.assertEqual(find_max[1,3,6,2,5,4], 6)
        with self.assertRaises(ValueError):
            find_max([])
        self.assertEqual(find_max([-1,-2,-3,-4]), -1)
        self.assertEqual(find_max[96], 96)
        self.assertEqual(find_max([81, 96, 77, 64, 49]), 96)

    def test_find_min(self): 
        self.assertEqual(find_min([1, 2, 3, 4, 5]),1)
        self.assertEqual(find_min([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(find_min([5]), 5)
        with self.assertRaises(ValueError):
            find_min([])

    def test_find_average(self):
        self.assertEqual(find_average(sum(list) / len(list)), 3.0)
        with self.assertRaises(ValueError):
            find_average([])
        self.assertEqual(find_average([3]), 3.0)

    def test_find_all_even_numbers(self): 
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
        self.assertEqual(find_even_numbers([1, 3, 5]), ())
    
    def test_find_all_odd_numbers(self): 
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(find_odd_numbers([2, 4, 6]), ())

    def test_find_total_number_of_even_numbers(self): pass

    def test_find_total_number_of_odd_numbers(self): pass

    def test_return_list_stats(self): 
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)
        self.assertEqual(stats["average"], 3.0)
        self.assertEqual(stats["number_of_even_numbers"], 2)
        self.assertEqual(stats["number_of_odd_numbers"], 3)
        self.assertEqual(stats["even_numbers"], (2, 4))
        self.assertEqual(stats["odd_numbers"], (1, 3, 5))
    
    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_generate_squared_dict(self):
        self.assertEqual(generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
        self.assertEqual(generate_squared_dict(0), {})

    def test_convert_word_list_sentence(self): 
        result = convert_to_word_list("There is only one to fear and his name is Death.")
        self.assertEqual(result, ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 'his', 'name', 'is', 'death'])
 
    def test_convert_word_list_spaces(self): pass

    def test_letters_count_sentence(self): pass

    def test_alphanumeric_1(self): pass
    
    def test_alphanumeric_2(self): pass
    
    def test_alphanumeric_3(self): pass
    

