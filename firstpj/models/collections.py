class Collections:
    def add_sequence(sequence):
        sequence = sequence * 2
        print(sequence * 2)

    def add_el_list_in_tuple(sequence: tuple):
        sequence[0].append(10)

    def slicing(self):
        my_list = [3, 43, (94, 5)]
        print("slice 1" + str(my_list[1:3]))
        print("slice 2" + str(my_list[1:3:1]))

    if __name__ == "main":
        test_list = [1, 3, 23, 43]
        print("before:" + str(test_list))
        add_sequence(test_list)
        print("after:" + str(test_list))

        if (2 in test_list):
            print("i am sad")
        add_sequence(("first", "sec"))
        # create tuple with lists
        new_tuple = ([1, 2], [3, 4])
        print("before:" + str(new_tuple))
        add_el_list_in_tuple(new_tuple)
        print("after:" + str(new_tuple))
