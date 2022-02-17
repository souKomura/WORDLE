import os
from src import (
    A_make_five,
    B_make_score_marix,
    C_make_first_entropy_lis,
    D_solver
)

def main():
    lang = "en"
    path = "./{}/".format(lang)

    if not os.path.exists(path + "five.txt"):
        print("filter words with five characters...")
        A_make_five.make_five(lang)

    if not os.path.exists(path + "score_mat.npy"):
        print("making score matrix...")
        B_make_score_marix.make_score_matrix(lang)
    
    if not os.path.exists(path + "first_entropy.data"):
        print("culculating first entropies...")
        C_make_first_entropy_lis.make_first_entropy(lang)
    
    D_solver.solver(lang, False)
    
    return

if __name__ == "__main__":
    main()
