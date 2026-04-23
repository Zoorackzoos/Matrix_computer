def q_7_2_1(tab_amount = "\t"):
    """
    Suppose v1, v2,v3 is an orthogonal set of vectors in R^5.
     Let w be a vector in span( v1, v2, v3, ) such that
    v1 * v1 = 6 , v2 * v2 = 2 , v3 * v3 = 36
    w * v1 = 6 , w * v2 = -10 , w * v3 = -144

    :param tab_amount:
    :return:
    """
    product_v1_v1 = 6
    product_v2_v2 = 2
    product_v3_v3 = 36

    product_w_v1 = 6
    product_w_v2 = -10
    product_w_v3 = -144

    results_list = []

    results_list.append(product_w_v1/product_v1_v1)
    results_list.append(product_w_v2/product_v2_v2)
    results_list.append(product_w_v3/product_v3_v3)
    print(results_list)

if __name__ == "__main__":
    q_7_2_1()