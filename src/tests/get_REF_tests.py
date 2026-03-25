import inspect
import unittest

from src.matrix_operations.get_REF import *

class UnitTest_get_REF(unittest.TestCase):

    def test_no_list_matrix_edge_case(self, tab_amount=""):
        print(tab_amount, inspect.currentframe().f_code.co_name)
        tab_amount += "\t"

        original_matrix = \
            [

            ]

        matrix_output = get_REF(matrix_in_question=original_matrix, tab_amount=tab_amount)

        correct_matrix = \
            [

            ]

        self.assertEqual(matrix_output, correct_matrix)

    def test_matrix_all_zeros_edge_case(self, tab_amount=""):
        print(tab_amount, inspect.currentframe().f_code.co_name)
        tab_amount += "\t"
        original_matrix = \
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        correct_matrix = \
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

        matrix_output = get_REF(matrix_in_question=original_matrix, tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)

    def test_one_two_three_matrix(self, tab_amount=""):
        print(tab_amount, inspect.currentframe().f_code.co_name)
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
        matrix_output = get_REF(matrix_in_question=original_matrix, tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)

    def test_q_5_2_4_a(self, tab_amount="\t"):
        print(tab_amount, inspect.currentframe().f_code.co_name)
        tab_amount += "\t"

        original_matrix = \
            [
                [-5, 1, 11, 3],
                [-4, -5, 3, 3],
                [2, 3, -1, 4],
                [-5, -1, 9, 4]
            ]

        correct_matrix = \
            [
                [-200, 40, 440, 120],
                [0, 157760, 157760, -16320],
                [0, 0, 0, -201443200],
                [0, 0, 0, 0]
            ]

        matrix_output = get_REF(matrix_in_question=original_matrix, tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)

    def test_q_5_2_4_b(self,tab_amount="\t"):
        print(tab_amount, inspect.currentframe().f_code.co_name)
        tab_amount += "\t"

        original_matrix = \
            [
                [-3, 9, 18, 36],
                [5, -13, -24, -45],
                [-1, 1, -2, -7],
                [-1, 3, 6, 12]
            ]
        """
        i got the correct matrix from here:
        https://www.symbolab.com/solver/matrix-row-echelon-calculator/row%20echelon%20%5Cbegin%7Bpmatrix%7D-3%269%2618%2636%5C%5C%205%26-13%26-24%26-45%5C%5C%20-1%261%26-2%26-7%5C%5C%20-1%263%266%2612%5Cend%7Bpmatrix%7D?or=input
        that's why it's all weird. 
        """
        correct_matrix = \
            [
                [-3*5, 9*5, 18*5, 36*5],
                [0, 2*-90, 6*-90, 15*-90],
                [0, 0, -2*-90, -4*-90],
                [0, 0, 0, 0]
            ]
        matrix_output = get_REF(matrix_in_question=original_matrix, tab_amount=tab_amount)
        self.assertEqual(matrix_output, correct_matrix)