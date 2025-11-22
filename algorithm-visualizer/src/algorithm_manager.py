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
    "10": ("Bucket Sort", sorting_algorithms.bucket_sort),
    "11": ("Counting Sort", sorting_algorithms.counting_sort),
    "12": ("Radix Sort", sorting_algorithms.radix_sort),
    "13": ("Heap Sort", sorting_algorithms.heap_sort),
    "14": ("Shell Sort", sorting_algorithms.shell_sort),
}

ALGORITHMS_QT = {
    "Bubble Sort": "1",
    "Cocktail Sort": "2",
    "Insertion Sort": "3",
    "Merge Sort": "4",
    "Gnome Sort": "5",
    "Selection Sort": "6",
    "Quick Sort": "7",
    "Bogo Sort": "8",
    "Random Sort": "9",
    "Bucket Sort" : "10",
    "Counting Sort" : "11",
    "Radix Sort" : "12",
    "Heap Sort" : "13",
    "Shell Sort" : "14",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))
    