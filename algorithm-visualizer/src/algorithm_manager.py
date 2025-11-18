import sorting_algorithms

ALGORITHMS = {
    "1": ("Bubble Sort", sorting_algorithms.bubble_sort),
    "2": ("Cocktail Sort", sorting_algorithms.cocktail_sort),
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))
    