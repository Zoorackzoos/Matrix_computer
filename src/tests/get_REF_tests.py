import inspect
import unittest

from src.matrix_operations.get_REF import *

class UnitTest_get_REF(unittest.TestCase):

    def test_no_list_matrix_edge_case(self, tab_amount=""):
        print(tab_amount,inspect.currentframe().f_code.co_name)
        tab_amount += "\t"

        original_matrix = \
        [

        ]

        matrix_output = get_REF(matrix_in_question=original_matrix,tab_amount=tab_amount)

        correct_matrix = \
        [

        ]

        self.assertEqual(matrix_output, correct_matrix)

    def test_matrix_all_zeros_edge_case(self, tab_amount=""):
        print(tab_amount,inspect.currentframe().f_code.co_name)
        tab_amount += "\t"
        original_matrix = \
        [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        correct_matrix = \
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        matrix_output = get_REF(matrix_in_question=original_matrix,tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)

    def test_one_two_three_matrix(self, tab_amount=""):
        print(tab_amount,inspect.currentframe().f_code.co_name)
        tab_amount += "\t"

        """
        1 2 3 -> 4 8 12 -> 4 8 12 ->28  56  84-> 28 56 84-> 20 56  84-> 20 56 84
        4 5 6    -4 -5 -6  0 3 6    0   3   6    0  3  6    0  72  144  0  72 144
        7 8 9    7 8 9     7 8 9    -28 -32 -36  0  24 48   0 -72 -144  0  0  0
        """

        original_matrix = \
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        correct_matrix = \
            [
                [28, 56, 84],
                [0, 72, 144],
                [0, 0, 0]
            ]
        matrix_output = get_REF(matrix_in_question=original_matrix,tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)