def print_out(a):
    print("Outer: {}".format(a))

    def print_in():
        print("\tInner: {}".format(a))

    # print_in()
    # return print_in()
    return print_in


test2 = print_out("test")

del print_out

test2()
