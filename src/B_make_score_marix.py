import sys
import numpy as np
from src.wordle import Wordle

#-------------------------------
def make_score_matrix(lang="en"):
    """
    単語集合の全ての組み合わせについてスコアを保存
    比較結果は対称ではない. e.g spallとslash
    """
    voc_file = "./{}/five.txt".format(lang)
    mat_file = "./{}/score_mat.npy".format(lang)
    
    with open(voc_file) as f:
        voc_lis = f.read().split()

    mat = np.zeros([len(voc_lis), len(voc_lis)], dtype=int)

    for i,wordi in enumerate(voc_lis):
        sys.stdout.write("\r {} / {}".format(i, len(voc_lis)))
        sys.stdout.flush()
        for j in range(i+1, len(voc_lis)):
            wordj = voc_lis[j]
            mat[i,j] = Wordle.get_score(wordi, wordj)
            mat[j,i] = Wordle.get_score(wordj, wordi)
            
    np.save(mat_file, mat)
    
    print()

    return


#-------------------------------
if __name__ == '__main__':
    make_score_matrix()
    