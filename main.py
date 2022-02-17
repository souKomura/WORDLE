import os
import argparse
from src import (
    A_make_five,
    B_make_score_marix,
    C_make_first_entropy_lis,
    D_solver
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--feedback", help="turn on user-typed feedback.", action="store_true")
    parser.add_argument("-l", "--language", help="set wordle language", choices=["en", "jp"], default="en")

    args = parser.parse_args()

    lang = args.language

    path = "./{}/".format(lang)

    if not os.path.exists(path + "words.txt"):
        print("make words.txt file.")
        return

    if not os.path.exists(path + "five.txt"):
        print("filter words with five characters...")
        A_make_five.make_five(lang)

    if not os.path.exists(path + "score_mat.npy"):
        print("making score matrix...")
        B_make_score_marix.make_score_matrix(lang)
    
    if not os.path.exists(path + "first_entropy.data"):
        print("culculating first entropies...")
        C_make_first_entropy_lis.make_first_entropy(lang)
    
    D_solver.solver(lang, args.feedback)
    
    return

if __name__ == "__main__":
    main()
