# source https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/


def max_box_count(room_width, room_length, box_width, box_length, rotate = False):
    """
    Function computes a maximum amount of boxes, which can be fit in the room.
    If boxes are turned, all of them have to be turned

    :param room_width: width of the room, positive int
    :param room_length: length of the room, positive int
    :param box_width: with of a box, positive int
    :param box_length: length of a box, positive int
    :param rotate: default = False - boxes can;t be rotated, True - all boxes has to be rotated
    :return: maximum amount of boxes fit in the room
    """
    if rotate:
        count_width = room_width // box_length
        count_length = room_length // box_width
    else:
        count_width = room_width // box_width
        count_length = room_length // box_length

    return count_width * count_length


def n_max_box_count(room_size, box_size):
    """
    Function computes a maximum amount of boxes, which can be fit in the room.
    If boxes are turned, all of them have to be turned

    :param room_size: measures of a n-dimensional room, measures are positive int
    :param box_size: measures of a n-dimensional box, measures are positive int
    :return: maximum amount of boxed fit in the room
    """
    count_axis = []
    for i in range(len(room_size)):
        count_axis.append(room_size[i] // box_size[i])

    box_count = 1
    for axis in count_axis:
        box_count = box_count * axis
        
    return box_count
