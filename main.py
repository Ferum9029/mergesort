import sorting
import iostream

if __name__ == "__main__":
    print(sorting.merge_sort([2, 11, 13, 5, 6, 7]))
    print(sorting.merge_sort([2, 11, 13, 5, 6, 7, 23]))
    iostream.console_output(sorting.merge_sort(iostream.file_input()))

