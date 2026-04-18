import math

from src.A_universal_operations.calc_3_like_funcitons.convert_to_divided_by_sqrt import convert_to_divided_by_sqrt


def get_magnitude(vector , tab_amount="\t"):
    print(tab_amount,"get_magnitude")
    tab_amount += "\t"

    vector_sum = 0
    print(tab_amount,"vector_sum -> ",vector_sum)

    for element in vector:
        print(tab_amount+"\t", "+ ", element)
        vector_sum += math.pow(element , 2)

    print(tab_amount,"vector_sum -> ",vector_sum)
    print(tab_amount,"math.sqrt(vector_sum) -> ",math.sqrt(vector_sum))
    print(tab_amount,"convert_to_divided_by_sqrt(math.sqrt(vector_sum)) -> ",convert_to_divided_by_sqrt(math.sqrt(vector_sum),tab_amount=tab_amount+"\t"))

    return math.sqrt(vector_sum)

if __name__ == "__main__":
    vector = [1,2,3]
    tab_amount = "\t"
    get_magnitude(vector=vector, tab_amount=tab_amount)