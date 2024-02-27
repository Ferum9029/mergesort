from utils import merge


def merge_sort(original: list) -> list:
    # if the size is 1 or lower, we leave it as it is
    if len(original) <= 1:
        return original

    # finding the middle index
    # odd amounts are left to the second slice
    middle_index = len(original) // 2

    # splitting the slices again and then merging them
    return merge(merge_sort(original[0: middle_index]), merge_sort(original[middle_index:]))

