import random
from algorithm_manager import get_algorithm # type: ignore
from visualizer import SortingVisualizer # type: ignore

def main():
    n = int(input("Introduce tamaño del vector: "))

    print("Selecciona el algoritmo:")
    print("1- Bubble Sort")
    print("2- Cocktail Sort")
    print("3- Insertion Sort")

    choice = input("Opción: ")

    name, alg = get_algorithm(choice)
    if alg is None:
        print("Opción inválida")
        return

    arr = list(range(1, n + 1))
    random.shuffle(arr)

    generator = alg(arr)
    visualizer = SortingVisualizer(arr, name, generator)
    visualizer.run()

if __name__ == "__main__":
    main()
