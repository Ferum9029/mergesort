import sorting
import iostream

if __name__ == "__main__":
    iostream.console_output(sorting.merge_sort([2, 11, 13, 5, 6, 7]))
    iostream.console_output(sorting.merge_sort([2, 11, 13, 5, 6, 7, 23]))
    iostream.console_output(sorting.merge_sort((lambda x: print(x) or x)(iostream.random_input(15))))
