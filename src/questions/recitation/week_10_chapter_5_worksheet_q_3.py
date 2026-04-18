from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.matrix_operations.REF_and_RREF_getters.get_REF import get_REF

def week_10_chapter_5_worksheet_q_3(tab_amount="\t"):
    print(tab_amount,"week_10_chapter_5_worksheet_q_3")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1,-5,-3],
        [2,5,1],
        [4,12,3]
    ]
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix(matrix_in_question)
    # idk. fact check this maybe. I confused the 8 with a 0.
    # here's look.
    # matrix_in_question = set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    # print_matrix(matrix_in_question)

if __name__ == "__main__":
    tab_amount = "\t"
    week_10_chapter_5_worksheet_q_3(tab_amount=tab_amount)