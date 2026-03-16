from src.display.print_matrix import print_matrix, print_matrix_frac
from src.matrix_operations.operation_functions import *

def q_4_3_4(tab_amount = "\t"):
    """
    Let
    A = \
    [
        [3,-2,4,-3,2],
        [4,2,-3,-2,3],
        [2,1,2,-5,4]
    ]
    give a nonzero vector x in the null space of A.
    x = \
    [
        [ _ ],
    [ _ ],
    [ _ ],
    [ _ ],
    [ _ ],
    ]

    idk bro


    :param tab_amount:
    :return:
    """
    matrix_in_question = \
        [
            [3, -2, 4, -3, 2],
            [4, 2, -3, -2, 3],
            [2, 1, 2, -5, 4]
        ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=4,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=6,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    #weird but ok
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/12,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/14,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1/21,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=25/14)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=14/25,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2/3,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=4/3,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=3/2,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=3/4,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)

if __name__ == "__main__":
    q_4_3_4(tab_amount="\t")