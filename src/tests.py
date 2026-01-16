import inspect
import unittest

from src.operation_functions import *
from src.print_matrix import print_matrix

"""
def manual_test_swapping_rows(matrix, tab_amount="\t"):
    # swapping rows test.
    print(tab_amount,"swapping_rows_test")
    tab_amount += "\t"
    swap_rows(matrix,0, 1,tab_amount=tab_amount)
    print(tab_amount,"swapped row 1 and 2 in the matrix: ")
    print_matrix(matrix, tab_amount)
    return matrix

def manual_test_scale_row_from_number(matrix, tab_amount="\t"):
    #scale row from number test
    print(tab_amount,"scale_row_from_number_test")
    tab_amount += "\t"
    scale_row_from_number(matrix,0,2,tab_amount)
    print_matrix(matrix)
    return matrix

def manual_test_scale_row_from_row_and_number(matrix, tab_amount="\t"):
    # scale_row_from_row_and_number test
    print(tab_amount,"scale_row_from_row_and_number_test")
    tab_amount += "\t"
    # r2 <- r2 + -4r1
    scale_row_from_row_and_number(matrix,1, 0, -4, tab_amount=tab_amount)
    print_matrix(matrix,tab_amount)
    return matrix
"""

class UnitTest_Operation_Functions(unittest.TestCase):

    def test_swap_rows(self, tab_amount=""):
        #this line is taking the title of the function and shouting it out.
        #it has nothing to do with the unit tests.
        print(tab_amount,inspect.currentframe().f_code.co_name)
        tab_amount += "\t"
        original_matrix = \
        [
            [1, -3, 2, "|", -4],
            [4, -11, -3, "|", 1],
            [-4, 8, -3, "|", -6]
        ]
        correct_matrix = \
        [
            [4, -11, -3, '|', 1],
            [1, -3, 2, '|', -4],
            [-4, 8, -3, '|', -6]
        ]
        print_matrix(matrix=original_matrix, tab_amount=tab_amount)
        print_matrix(matrix=correct_matrix, tab_amount=tab_amount)
        print()
        self.assertTrue( swap_rows(matrix=original_matrix,row_1=0,row_2=1,tab_amount=tab_amount) == correct_matrix)

    def test_scale_row_from_number(self, tab_amount=""):
        print(tab_amount,inspect.currentframe().f_code.co_name)
        tab_amount += "\t"
        original_matrix = \
            [
                [1, -3, 2, "|", -4],
                [4, -11, -3, "|", 1],
                [-4, 8, -3, "|", -6]
            ]
        correct_matrix = \
            [
                [2, -6, 4, '|', -8],
                [4, -11, -3, '|', 1],
                [-4, 8, -3, '|', -6]
            ]
        print_matrix(matrix=original_matrix, tab_amount=tab_amount)
        print_matrix(matrix=correct_matrix, tab_amount=tab_amount)
        print()
        self.assertTrue(
            scale_row_from_number(matrix=original_matrix,row_in_question=0,number=2,tab_amount=tab_amount)
            == correct_matrix
        )

    def test_scale_row_from_row_and_number(self, tab_amount=""):
        print(tab_amount, inspect.currentframe().f_code.co_name)
        tab_amount += "\t"
        original_matrix = \
            [
                [1, -3, 2, "|", -4],
                [4, -11, -3, "|", 1],
                [-4, 8, -3, "|", -6]
            ]
        correct_matrix = \
            [
                [1, -3, 2, '|', -4],
                [0, 1, -11, '|', 17],
                [-4, 8, -3, '|', -6]
            ]
        print_matrix(matrix=original_matrix, tab_amount=tab_amount)
        print_matrix(matrix=correct_matrix, tab_amount=tab_amount)
        print()
        self.assertTrue(
            scale_row_from_row_and_number(matrix=original_matrix,row_modified=1,row_to_be_added=0,number=-4, tab_amount=tab_amount)
            == correct_matrix
        )
