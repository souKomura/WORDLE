from src.wordle import Wordle
import numpy as np
import random

def main():
    voc_file = "./en/five.txt"
    mat_file = "./en/score_mat.npy"

    words = open(voc_file).read().split()
    mat = np.load(mat_file)

    print(len(words))

    for _ in range(50):
        i = random.randint(0, len(words)-1)
        j = random.randint(0, len(words)-1)
        
        print(mat[i, j] == Wordle.get_score(words[i], words[j]))

    return

if __name__ == '__main__':
    main()
    