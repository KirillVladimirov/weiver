
def reverse_list_v0(max_el):
    g = (x for x in range(-max_el, 0))
    return list(map(abs, g))
