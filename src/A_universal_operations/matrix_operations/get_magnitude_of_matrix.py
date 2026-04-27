import math

def get_magnitude_of_matrix(matrix, tab_amount="\t"):
    print(tab_amount,"get_magnitude_of_matrix")
    tab_amount += "\t"

    print(tab_amount,matrix)

    matrix_sum = 0
    print(tab_amount,"matrix_sum -> ",matrix_sum)

    for row in matrix:
        for col in row:
            print(tab_amount+"\t+",col)
            matrix_sum += math.pow(col, 2)

    print(tab_amount,"matrix_sum -> ",matrix_sum)
    print(tab_amount,"math.sqrt(matrix_sum) -> ",math.sqrt(matrix_sum))
    #print(tab_amount,"convert_to_divided_by_sqrt(math.sqrt(matrix_sum)) -> ",convert_to_divided_by_sqrt(math.sqrt(matrix_sum),tab_amount=tab_amount+"\t"))

    return math.sqrt(matrix_sum)

if __name__ == "__main__":
    vector = \
        [
            [1,2,3]
        ]
    tab_amount = "\t"
    get_magnitude_of_matrix(matrix=vector, tab_amount=tab_amount)