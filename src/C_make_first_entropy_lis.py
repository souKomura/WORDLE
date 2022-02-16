from math import log2
import sys
import numpy as np
import collections
import pickle

def make_first_entropy(lang):
    """
    絞り込みを何もしていない語彙でO(n^2)のエントロピー計算を行うと大変重いため.
    あらかじめ計算/ファイルへ保存しておく.
    """

    #各種ファイル展開
    voc_file = "./{}/five.txt".format(lang)
    score_mat_file = "./{}/score_mat.npy".format(lang)
    entropy_file = "./{}/first_entropy.data".format(lang)

    voc = open(voc_file).read().split()
    score_mat = np.load(score_mat_file)
    l = len(voc)

    #エントロピーを全ての単語について計算
    #1. possible_score_dic[i][j]... 単語iでスコアjとなる単語の数
    possible_score_lis = [collections.defaultdict(int) for _ in range(l)]
    for i in range(l):
        sys.stdout.write("\r{}/{}".format(i, l))
        for j in range(i+1, l):
            possible_score_lis[i][score_mat[i, j]] += 1
            possible_score_lis[j][score_mat[j, i]] += 1
    
    # 2. 単語ごとに情報量の期待値を算出
    entropy_lis = []
    for ddict in possible_score_lis:
        freq_lis = ddict.values()
        s = sum(freq_lis)
        freq_normalize = map(lambda x:x/s, freq_lis)
        informations = map(lambda x: -x * log2(x), freq_normalize)
        entropy = sum(informations)

        entropy_lis.append(entropy)
    
    #リストを保存
    with open(entropy_file, "wb") as f:
        pickle.dump(entropy_lis, f)
    
    print()

    return

if __name__ == '__main__':
    make_first_entropy("en")
    