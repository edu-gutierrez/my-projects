import random
from algorithm_manager import get_algorithm # type: ignore
from visualizer import SortingVisualizer # type: ignore

def main():
    n = int(input("Introduce tamaño del vector: "))
    if n <= 0:
        print("Tamaño inválido")
        return

    print("Selecciona el algoritmo:")
    print("1- Bubble Sort")
    print("2- Cocktail Sort")
    print("3- Insertion Sort")
    print("4- Merge Sort")
    print("5- Gnome Sort")
    print("6- Selection Sort")
    print("7- Quick Sort")
    print("8- Bogo Sort")
    print("9- Random Sort")

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
