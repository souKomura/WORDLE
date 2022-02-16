import random

class Wordle:
    """minimal class for Wordle game"""

    def __init__(self, vocabulary, try_number):
        self.voc_set = set(vocabulary)
        self.try_num = try_number
        self.correct_word = random.choice(vocabulary)
    
    def guess(self, word):
        
        if len(word) != 5:
            return -1, "guess word with 5 characters."

        if not(word in self.voc_set):
            return -1, "guess with existing word."

        self.try_num -= 1
        score = Wordle.get_score(word, self.correct_word)
        return score, Wordle.score_to_string(score)
    
    @staticmethod
    def get_score(w1, w2):
        score1 = 0
        score2 = 0
        w1 = list(w1)
        w2 = list(w2)

        for i in range(len(w1)):
            if w1[i] == w2[i]:
                score1 = score1*3 + 2
                w1[i] = -1
                w2[i] = -2
            else:
                score1 *= 3

        for i in range(len(w1)):
            if w1[i] in w2:
                score2 = score2*3 + 1
                w2.remove(w1[i])
            else:
                score2 = score2*3

        return int(score1 + score2)
    
    def score_to_string(score):
        s = ""
        for _ in range(5):
            bit = score%3
            s = ("⬛️", "🟨", "🟩")[bit] + s
            score //= 3

        return s

def main():
    voc = open("./en/five.txt").read().split()

    game = Wordle(voc, 6)
    print(game.correct_word)

    while game.try_num > 0:
        usr_input = input("guess > ")
        end, score, message = game.guess(usr_input)
        print(message)
        if end:
            break
    else:
        print("game over")
        
    return

if __name__ == '__main__':
    # main()
    f = Wordle.score_to_string
    g = Wordle.get_score

    print(f(g("slash", "spell")))
    print(f(g("spell", "slash")))