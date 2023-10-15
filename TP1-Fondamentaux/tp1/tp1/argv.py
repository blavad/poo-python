import sys

def show_arguments():
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print(f"Nombre d'arguments : {num_args}")
    print(f"Liste des arguments : {args}")

if __name__ == "__main__":
    show_arguments()