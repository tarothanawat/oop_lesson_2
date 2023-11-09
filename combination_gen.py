def gen_comb_list(list_set):
    if not list_set:
        return [[]]
    else:
        lst = []
        for i in list_set[0]:
            for j in gen_comb_list(list_set[1:]):
                lst.append([i] + j)
        return lst
