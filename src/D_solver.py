import os
from src.wordle import Wordle
from math import log2
import pickle
import numpy as np
import collections

#-----------------------------------
def solver(lang="en", feedback = False):
    """
    エントロピー最大の単語を提案しながらwordleをとく
    """

    #各種ファイル読み込み
    voc_file = "./{}/five.txt".format(lang)
    score_mat_file = "./{}/score_mat.npy".format(lang)
    first_entropy = "./{}/first_entropy.data".format(lang)

    voc = open(voc_file).read().split()
    voc_original = voc.copy()
    first_entropy = pickle.load(open(first_entropy, "rb"))
    score_mat = np.load(score_mat_file)
    word_to_index = {word:i for i,word in enumerate(voc)}

    #ゲームを作成
    game = Wordle(voc, 6)
    word_entropy = list(zip(voc, first_entropy))

    #表示項目の宣言
    hint_hist = []
    notice = ""
    usr_input_lis = []
    
    while game.try_num > 0:
        
        #ユーザによる入力
        print_ui(notice, hint_hist, word_entropy, voc, usr_input_lis)
        usr_input = input("{} guess > ".format(game.correct_word, len(voc_original), len(voc)))
        score, message = game.guess(usr_input)

        if feedback:
            score = 0
            feedback_string = input("input feedback e.g, gbybb > ")
            for c in feedback_string:
                if c == "g":
                    score = score*3 + 2
                elif c == "y":
                    score = score*3 + 1
                else:
                    score = score*3 + 0


        if score >= 0:
            #色のヒントをもとに単語絞り込み
            voc = filter_possible(voc, usr_input, score)
            entropy = compute_entropy(voc_original, voc, score_mat, word_to_index)
            word_entropy = list(zip(voc_original, entropy))
            hint_hist.append(message)
            usr_input_lis.append(usr_input)
            if score == 3**5-1:
                break
        else:
            notice = message

    notice = "correct answer was: {}".format(game.correct_word)
    
    print_ui(notice, hint_hist, word_entropy, voc, usr_input_lis)
    input("press any key to end > ")

    return

#-----------------------------------
def print_ui(notice, hint_hist, word_entropy, voc, usr_input_lis):
    os.system("clear")
    moveto = "\033[{};{}H"

    usr_input_pos = (4, 1)
    tile_pos = (4, 8)
    suggest_pos = (4,22)
    possible_ans_pos = (4, 47)

    print(moveto.format(1,1), end="")
    print(notice)

    for i,usr_input in enumerate(usr_input_lis):
        print(moveto.format(i+usr_input_pos[0], usr_input_pos[1]), end="")
        print(usr_input)

    for i, hint in enumerate(hint_hist):
        print(moveto.format(i+tile_pos[0], tile_pos[1]), end="")
        print(hint)
    
    print(moveto.format(suggest_pos[0], suggest_pos[1]), end="")
    print("{:>5}: entropy".format("word"))
    for i, tpl in enumerate(sorted(word_entropy, key=lambda tpl:-tpl[1])[:10]):
        word, entropy = tpl
        print(moveto.format(i+1+suggest_pos[0], suggest_pos[1]), end="")
        print("{}: {:.4f} bit".format(word, entropy))
    print(moveto.format(i+2+possible_ans_pos[0], possible_ans_pos[1]), end="")

    print(moveto.format(possible_ans_pos[0], possible_ans_pos[1]), end="")
    print("candidates for answers")
    for i,word in enumerate(voc):
        print(moveto.format(i+1+possible_ans_pos[0], possible_ans_pos[1]), end="")
        if i>8:
            print("...")
            break
        print(word)
    
    print(moveto.format(2,1), end="")

    

#-----------------------------------
def compute_entropy(voc_original, voc, score_mat, word_to_index):
    """エントロピーをvoc内全ての単語について計算"""
    
    #単語ごとにスコアの分布を保存
    # possible_score_dic[i][j]... 単語iでスコアjとなる単語の数
    possible_score_lis = [collections.defaultdict(int) for _ in range(len(voc_original))]
    for i in range(len(voc_original)):
        for j in range(len(voc)):
            mati,matj = i, word_to_index[voc[j]]
            possible_score_lis[i][score_mat[mati, matj]] += 1
    
    #単語ごとに，分布をもとにエントロピーを求める．
    entropy_lis = []
    for ddict in possible_score_lis:
        freq_lis = ddict.values()
        s = sum(freq_lis)
        s_normalize = map(lambda x:x/s, freq_lis)
        s_informations = map(lambda x: -x * log2(x), s_normalize)
        entropy = sum(s_informations)

        entropy_lis.append(entropy)
    
    return entropy_lis

#-----------------------------------
#TODO
#lares-⬛️⬛️⬛️🟨⬛️
#denie-⬛️🟨⬛️⬛️⬛️
#のとき， "eを含む単語"がはじかれてしまう．　denieの最後の一マスが黒いため．
#しかし，このとき弾くのは，"eをふたつ以上含む単語"のみである．　
def filter_possible(voc, usr_input, score):

    #scoreによって得られる情報を整理
    bhint = set()
    yhint = set()
    ghint = set()

    for i in reversed(range(5)):
        digit_hint = score%3
        score //= 3

        if digit_hint == 0:
            bhint.add(usr_input[i])
        elif digit_hint == 1:
            yhint.add(usr_input[i])
        else:
            ghint.add((i, usr_input[i]))
    
    #語彙リストをフィルタリング
    new_voc = []
    for word in voc:
        if word == usr_input:
            continue
        word_lis = list(word)

        green_match = True
        for i,c in ghint:
            if word_lis[i] != c:
                green_match = False

        yellow_match = True
        for c in yhint:
            if not(c in word_lis):
                yellow_match = False
        
        black_contain = False
        for c in bhint:
            if c in word_lis:
                black_contain = True
        
        if green_match and yellow_match and (not black_contain):
            new_voc.append(word)

    return new_voc

#-----------------------------------
if __name__ == '__main__':
    solver()
    