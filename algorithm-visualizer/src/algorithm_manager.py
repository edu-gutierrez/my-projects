import sorting_algorithms

ALGORITHMS = {
    "1": ("Bubble Sort", sorting_algorithms.bubble_sort),
    "2": ("Cocktail Sort", sorting_algorithms.cocktail_sort),
    "3": ("Insertion Sort", sorting_algorithms.insertion_sort),
    "4": ("Merge Sort", sorting_algorithms.merge_sort),
    "5": ("Gnome Sort", sorting_algorithms.gnome_sort),
    "6": ("Selection Sort", sorting_algorithms.selection_sort),
    "7": ("Quick Sort", sorting_algorithms.quick_sort),
    "8": ("Bogo Sort", sorting_algorithms.bogo_sort),
    "9": ("Random Sort", sorting_algorithms.random_sort),
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))
    