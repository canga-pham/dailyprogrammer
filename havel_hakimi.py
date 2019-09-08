# source https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/


def integer_list(list):
    """
    The function returns an error if elements of the list are not integers
    :param list: list which is supposed to have  integer elements only
    :return: error if any element is not an positive integer or zero
    """

    # raises an error if list contains a negative number
    for i in list:
        if not float(i).is_integer():
            raise ValueError("List {list} can contain only integers!".format(list=list))


def non_negative_list(list):
    """
    The function returns an error if elements of the list are negative
    :param list: list which is supposed to have negative elements only
    :return: error if element is not an positive number or zero
    """

    # raises an error if list contains a negative number
    for i in list:
        if i < 0:
            raise ValueError("List {list} can contain only non negative numbers!".format(list=list))


def havel_hakimi(list):
    """
    Havel-hakimi algorithm answers if the given list is a degree sequence of any simple graph. Degree sequence is a list
     of neighbors of all vertices in a graph.

    Algorithm:

    1. Remove all 0's from the sequence (i.e. warmup1).

    2. If the sequence is now empty (no elements left), stop and return true.

    3. Sort the sequence in descending order (i.e. warmup2).

    4. Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call
    it N. The sequence is now 1 shorter than it was after the previous step.

    5. If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.

    6. Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).

    7. Continue from step 1 using the sequence from the previous step.

    :param list: number of acquaintances in a group
    :return: True, if List is according to havel-hakimi algorithm
            False, if it's not
    """
    integer_list(list)
    non_negative_list(list)

    while True:
        # 1. removing zeros
        for i in range(list.count(0)):
            list.remove(0)

        # 2. list is empty => return true
        if len(list) == 0:
            return True

        # 3. sort list descending
        list.sort(reverse = True)

        # 4. remove the first answer
        n = list[0]
        list.remove(n)

        # 5.  If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
        if n > len(list):
            return False

        # 6. Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
        list[:] = [x - 1 for x in list]



