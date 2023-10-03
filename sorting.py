from utils import merge


def merge_sort(original: list) -> list:
    if len(original) <= 1:
        return original
    half = len(original) // 2
    return merge(merge_sort(original[0: half]), merge_sort(original[half:]))

