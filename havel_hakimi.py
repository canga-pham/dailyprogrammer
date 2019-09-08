# source https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

ACQUAINTANCE_LIST = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]


def havel_hakimi(list):
    """
    Algorithm:

    1. If the sequence is now empty (no elements left), stop and return true.

    2. Sort the sequence in descending order (i.e. warmup2).

    3. Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call
    it N. The sequence is now 1 shorter than it was after the previous step.

    4. If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.

    5. Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).

    6. Continue from step 1 using the sequence from the previous step.

    :param list: number of acquaintances in a group
    :return: True, if List is according to havel-hakimi algorithm
            False, is it's not
    """

    # 1. removing zeros
    if list.count(0) == len(list):
        return True
    for i in range(list.count(0)):
        list.remove(0)
    # 2. sort list descending
    list.sort(reverse = True)

    # 3. remove the first answer
    n = list[0]
    list.remove(n)

    # 4.  If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
    if n > len(list):
        return False




