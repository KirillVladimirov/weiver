
def reverse_list_v0(max_el):
    g = (x for x in range(-max_el, 0))
    return list(map(abs, g))


def plus_two(num: int):
    print("start function plus_two")
    return num + 2


if __name__ == "__main__":
    print(plus_two("5"))
    print(plus_two(5))
